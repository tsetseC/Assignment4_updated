from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def _str_(self):
        return self.user.username

class Article(models.Model):
    user=models.CharField(max_length=100)
    title =models.CharField(max_length=100)
    slug =models.SlugField()
    body =models.TextField()
    date =models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.title

    # def snippet(self):
    #     return self.body[:50] + '...'
class Comment(models.Model):
    commenter=models.CharField(max_length=50)
    body=models.TextField()
    

    def __str__(self):
        return self.body