"""mysiteproject URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from usersapp import views
#from django.contrib import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('usersapp/',include('usersapp.urls')),
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special,name='special'),
    path('create/',views.u_create,name='u_create'),
    path('articles/',views.article_list,name='article_list'),    
    path('edit/<int:id>', views.edit),      
    path('update/<int:id>', views.update),      
    path('delete/<int:id>', views.destroy),
    
]
