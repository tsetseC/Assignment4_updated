from django.contrib import admin
from usersapp.models import UserProfileInfo
from usersapp.models import Article

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Article)