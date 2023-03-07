
from django.shortcuts import render, redirect
from .forms import UserEditForm, UserForm,UserProfileInfoForm
from usersapp.models import Article,Comment


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request,'usersapp/index.html')

def special(request):
    return render(request,'usersapp/home_page.html')

def article_list(request):
    articles=Article.objects.all().order_by('date')
    return render(request,'usersapp/article_list.html',{'Article':articles})

def articles(request):
    art=Article.objects.all().order_by('date')
    return render(request,'usersapp/articles.html',{'Article':art})

def home_page(request):
    return render(request,'usersapp/home_page.html')

def info(request):
    comment=Comment.objects.all()
    return render(request,'usersapp/info.html',{'Comment':comment})

def info_view(request):
    if request.method=='POST':
        if request.POST.get('commenter') and request.POST.get('body') :
            com=Comment()
            com.commenter=request.POST.get('commenter')
            com.body=request.POST.get('body')
            com.save()
   
    return redirect('/info')

#logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))




def register(request):
    registered=False

    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user


            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            
            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)
   
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm

    return render(request,'usersapp/user_register.html',
                            {'user_form':user_form,
                               'profile_form':profile_form,
                               'registered':registered})


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('special'))

            else:
                return HttpResponse("ACCOUNTS NOT ACTIVE")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supplied!")

    else:
        return render(request,'usersapp/user_login.html',{})

def u_login(request):
    return render(request, 'usersapp/user_login.html')

# def registration(request):
#     registered=False
#     if request.method == 'POST':
        
#     else:
#         return UserForm()
#     return render(request, 'usersapp/user_register.html',context={'user_form':user_form,
#                                'profile_form':profile_form,
#                                'registered':registered})

def u_create(request):
    return render(request, 'usersapp/Create.html')


def create_user(request):
    if request.method=='POST':
        if request.POST.get('user') and request.POST.get('title') and request.POST.get('slug') and request.POST.get('body') and request.POST.get('date'):
            saveus=Article()
            saveus.user=request.POST.get('user')
            saveus.title=request.POST.get('title')
            saveus.slug=request.POST.get('slug')
            saveus.body=request.POST.get('body')
            saveus.date=request.POST.get('date')
            saveus.save()
            
            return HttpResponseRedirect(reverse('article_list'))

        else:
            return render(request,'usersapp/Create.html')

# def user_edit(request,id):
#     getuserarticles=Article.objects.get(id=id)
#     return render(request,'edit.html',{'Article':getuserarticles})

# def user_update(request,id):
#     user_update=Article.objects.get(id=id)
#     form=UserForm(request.POST,instance=user_update)

#     if form.is_valid():
#         form.save()
#         messages.success(request,"The user record is updated successfully..!")
#         return render(request,"edit.html",{"Article":user_update})
def edit(request, id):  
    article = Article.objects.get(id=id)  
    return render(request,'usersapp/edit.html', {'article':article})  
    
def update(request, id):  
    article = Article.objects.get(id=id) 
    form = UserEditForm(request.POST, instance = article)  
    if form.is_valid():  
        form.save()  
        return redirect("/articles")  
    return render(request, 'usersapp/edit.html', {'article':article})  

def destroy(request, id):  
    article = Article.objects.get(id=id) 
    article.delete()  
    return redirect("/articles")
