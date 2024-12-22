"""
URL configuration for saudemental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

import sys
sys.path.append("..saudemental_app.views")
from django.urls import path
from saudemental_app.views import register, index

urlpatterns = [
    path('register/', register, name='register'),
    path('', index, name='index'),
]

# urls.py
from django.urls import path
from saudemental_app.views import register, index, custom_login # type: ignore
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('', index, name='index'),  
    path('login/', custom_login, name='login'),  # Usando a view personalizada
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
