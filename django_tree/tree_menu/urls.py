from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name='home.html'),
        name='home'
    ),
    path(
        'technics/',
        TemplateView.as_view(template_name='technics.html'),
        name='technics'
    ),
    path(
        'phones/',
        TemplateView.as_view(template_name='phones.html'),
        name='phones'
    ),
    path(
        'about/',
        TemplateView.as_view(template_name='about.html'),
        name='about'
    ),
    path(
        'laptops/',
        TemplateView.as_view(template_name='laptops.html'),
        name='laptops'
    ),
    path(
        'accessories/',
        TemplateView.as_view(template_name='accessories.html'),
        name='accessories'
    ),
    path(
        'iphone/',
        TemplateView.as_view(template_name='iphone.html'),
        name='iphone'
    ),
    path(
        'android/',
        TemplateView.as_view(template_name='android.html'),
        name='android'
    ),
]
