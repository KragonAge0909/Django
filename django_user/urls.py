"""django_user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views

from django.views.generic import TemplateView

from core import urls as core_urls

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/', include('django_registration.backends.activation.urls')),
    # url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='login.html')),
    # url(r'^accounts/profile/$', auth_views.LoginView.as_view(template_name='home.html')),

    # path('admin/', admin.site.urls),

    # path('', include(core_urls)),

    # # Login and Logout
    # path('', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='login.html'), name='index'),
    # path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # # Main Page 
    # # path('', TemplateView.as_view(template_name='login.html'), name='login'),
    # path('profile', auth_views.LogoutView.as_view(template_name='profile.html'), name='profile'), 

    path('admin/', admin.site.urls),

    path('', include(core_urls)),

    # Login and Logout
    # path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),

    # # Main Page 
    # path('', auth_views.LoginView.as_view(template_name='login.html'), name='index'), 

    path('home', auth_views.LoginView.as_view(template_name='home.html'), name='home'),
]
