from django.contrib import admin
from usersapp.models import UserProfileInfo
from usersapp.models import Article,Comment

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Article)
 

admin.site.register(Comment)