"""libray_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from library_app import views 
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sview,name='sview'),
    path('add',views.add,name='add'),
    path('update',views.update,name='update'),
    path('update/<int:id>',views.update,name='update1'),
    path('delete/',views.delete,name='delete'),
    path('delete/<int:id>',views.delete,name='delete1'),
    path('sview',views.sview,name='sview'),
    path('login',views.login,name='login'),
    path('home',views.view,name='home'),
    path('signup',views.signup,name='signup')
]
