from django import forms
from django.contrib.auth.models import User
from usersapp.models import UserProfileInfo,Article
from django.forms import fields



class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')

# class CommentForm(forms.ModelForm):
#     commenter=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your name'}))
#     body=forms.CharField(max_length=100,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Comment here','rows':3})) 
#     class Meta:
#         model=Comments
#         fields=['commenter','body']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"