from django.contrib import admin
from django.urls import path

from menu.views import HomeView, AboutView, ProductsView, СontactsView, TestView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', СontactsView.as_view(), name='contacts'),
    path('products/', ProductsView.as_view(), name='products'),
    path('test/', TestView.as_view(), name='test'),
]