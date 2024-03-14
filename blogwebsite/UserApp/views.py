# from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
# from.forms import UserRegisterForm
from.forms import UserRegisterationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blogapp.forms import BlogPostForm
# Create your views here.



def register(request):
    form=UserRegisterationForm()
    context={
        "form":form
    }
    if request.method == 'POST':
        form_data= UserRegisterationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"USER ACCOUNT CREATED SUCCESSFULLY")
            return redirect("user-login")
    return render(request,"Accounts/register.html" ,context)

# def signup_page(request):   
#     return render(request, "Accounts/signup.html")



# def register(request):
#     user_form=UserReg

@login_required
def user_profile(request):
    return render (request,"Accounts/profile.html")

@login_required
def home_page(request):
     return render (request,"Accounts/homepage.html")


def logout_confirm(request):
    return render (request,"Accounts/logout_confirm.html")


@login_required
def add_blog_post(request):
    user=request.user
    post_form=BlogPostForm()
    context={
        'form':post_form
    }
    if request.method == "POST":
        form=BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form_data=form.save(commit=False)
            form_data.author=user
            form_data.save()
            return redirect("home")

    return render(request, "posts/add_post.html", context)