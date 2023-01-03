"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'demo'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('regist/', views.regist),
    path('login/', views.login_auth),
    path('logout/', views.my_logout),
    path('index/', views.index),
    path('createuser', views.createSingleUser),
    path('createmultiple_user', views.createMutipleUser),
    path('insert/', views.insert_data),
    path('delete/', views.delete_data),
    path('update/', views.update_data),
    path('query/', views.query_data),
    path('download/bigfile', views.download_big_file),
    path('download/smallfile', views.download_small_file),
    path('download/', views.download_page),
    path('upload/', views.upload_file),
    path('multipleInsert/', views.insertMultipleBook),
]
