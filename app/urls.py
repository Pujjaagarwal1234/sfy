from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.templatetags.static import static
from django.views.static import serve


urlpatterns = [
    path('',views.index, name='index'),
    # path('home',views.index, name='index'),
    path('about-us',views.about_us, name='about-us'),
    path('services',views.services, name='services'),
    path('app-development',views.app_development, name='app-development'),
    path('our-products',views.our_products, name='our-products'),
    path('events',views.events, name='events'),
    path('contact',views.contact, name='contact'),
    path('blog',views.blog, name='blog'),
    
]