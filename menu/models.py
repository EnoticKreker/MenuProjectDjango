from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse, NoReverseMatch

class Menu(models.Model):
    name = models.CharField('Название меню', max_length=50, unique=True)
    title = models.CharField('Заголовок меню', max_length=100)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, 
                             related_name='children', null=True, blank=True)
    title = models.CharField('Название пункта', max_length=100)
    url = models.CharField('URL', max_length=200, blank=True)
    named_url = models.CharField('Именованный URL', max_length=100, blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return self.url or '#'
        return self.url or '#'