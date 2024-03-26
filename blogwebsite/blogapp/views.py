from django.shortcuts import render

from django.shortcuts import render,redirect
from .models import BlogPost,Category
from.forms import CommentPostForm
from.forms import CommentPost
from django.contrib import messages
# Create your views here.
def home_page_view(request):

    all_data=BlogPost.objects.all()
    context={
        "posts":all_data
    }
    response= render(request, "main/index.html",context)
    response.set_cookie("visitor","some server value")
    return response

def about_page_view(request):
    return render(request, "main/about.html")

def contact_page_view(request):
    return render(request, "main/contact.html")


def blog_details_view(request, blog_id):
    form=CommentPostForm()
    blog_post= BlogPost.objects.get(id=blog_id)
    categories= Category.objects.all()
    print(request.COOKIES)
    similar_posts= BlogPost.objects.filter(category=blog_post.category).exclude(id=blog_post.id)
    comment=CommentPost.objects.filter(blog=blog_post)

    context= {
        "post": blog_post,
        "categories": categories,
        "similar_posts": similar_posts,
        "form":form,
        "comments":comment,
    }
    if request.method == "POST":
        form=CommentPostForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.blog=blog_post
            comment.save()
            
            messages.success(request,"comment added successfully")
            return redirect("post_detail",blog_id=blog_post.id) 

    return render(request, "main/post.html", context)

def posts_by_category(request, category_name):
    post=BlogPost.objects.filter(category__name=category_name)
    context={
        "post": post
    }
    return render(request, "main/category_post.html", context)
