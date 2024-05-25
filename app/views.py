from django.shortcuts import redirect, render
from urllib.parse import unquote
from django.shortcuts import redirect
# from app1.email_utils import send_email
from .models import * 
from django.core import serializers
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect


def index(request):
    print('in index')
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about-us.html')

def services(request):
    return render(request, 'services.html')

def app_development(request):
    return render(request, 'app-development.html')

def blog(request):
    return render(request, 'blog.html')

def events(request):
    return render(request, 'event.html')

def our_products(request):
    return render(request, 'our-product.html')

def contact(request):
    return render(request, 'contact.html')

