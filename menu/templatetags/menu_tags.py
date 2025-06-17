from django import template
from django.urls import resolve, Resolver404
from ..models import Menu

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    
    try:
        menu = Menu.objects.prefetch_related('items__children').get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu': None}
    
    def build_tree(items, current_path):
        tree = []
        for item in items:
            try:
                resolved = resolve(item.get_url())
                current = resolve(current_path)
                is_active = (resolved.url_name == current.url_name)
            except Resolver404:
                is_active = (item.get_url() == current_path)
            
            children = item.children.all()
            if children:
                child_tree, has_active_child = build_tree(children, current_path)
                is_expanded = is_active or has_active_child
            else:
                child_tree = []
                is_expanded = False
            
            tree.append({
                'item': item,
                'children': child_tree,
                'is_active': is_active,
                'is_expanded': is_expanded,
            })
        
        has_active = any(i['is_active'] or i['is_expanded'] for i in tree)
        return tree, has_active
    
    menu_tree, _ = build_tree(menu.items.filter(parent=None).order_by('order'), request.path_info)
    
    return {
        'menu': menu,
        'menu_tree': menu_tree,
    }