from django.views.generic import ListView, DetailView, TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class СontactsView(TemplateView):
    template_name = 'contacts.html'

class TestView(TemplateView):
    template_name = 'test.html'

class ProductsView(ListView):
    template_name = 'products/list.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        return ['Продукт 1', 'Продукт 2', 'Продукт 3']

class ProductDetailView(DetailView):
    template_name = 'products/detail.html'
    
    def get_object(self):
        return f"Продукт {self.kwargs['pk']}"