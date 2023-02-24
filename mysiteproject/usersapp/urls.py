from django.urls import path
from usersapp import views


app_name='usersapp'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('u_login/',views.u_login,name='u_login'),
    path('home_page/',views.home_page,name='home_page'),   
    path('articles/',views.articles,name='articles'), 
    path('create_user/',views.create_user,name='create_user'),
    
]