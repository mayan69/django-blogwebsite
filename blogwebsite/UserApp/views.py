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
from blogapp.models import BlogPost
from blogapp.forms import CommentPostForm
from blogapp.models import CommentPost
# Create your views here.



def register(request):
    cart=request.POST.get("cart")
    request.session["cart_items"]= "some cart information"
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
    cart=request.session.get("cart_items")
    posts=BlogPost.objects.filter(author=request.user)


    context={
        "cart":cart,
        "user_post":posts
    }
    return render (request,"Accounts/profile.html",context)

@login_required
def home_page(request):
     return render (request,"Accounts/homepage.html")


def logout_confirm(request):
    return render (request,"Accounts/logout_confirm.html")


@login_required
def add_blog_post(request):
    cart_data=request.session.get("cart_items")
    print(cart_data)
    user=request.user
    post_form=BlogPostForm()
    context={
        'form':post_form,
        "cart":cart_data
    }
    if request.method == "POST":
        form=BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form_data=form.save(commit=False)
            form_data.author=user
            form_data.save()
            return redirect("home")

    return render(request, "posts/add_post.html", context)




def add_comment_post(request):
    comment_form=CommentPostForm()
    context={
        'form':comment_form
        
    }
    if request.method == "POST":
        form=BlogPostForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment_form=form.save(commit=False)
            comment_form.save()
            return redirect("home")