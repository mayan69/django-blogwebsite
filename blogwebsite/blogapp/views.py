from django.shortcuts import render

from django.shortcuts import render
from .models import BlogPost,Category
# Create your views here.
def home_page_view(request):

    all_data=BlogPost.objects.all()
    context={
        "posts":all_data
    }
    return render(request, "main/index.html",context)

def about_page_view(request):
    return render(request, "main/about.html")

def contact_page_view(request):
    return render(request, "main/contact.html")


def blog_details_view(request, blog_id):
    blog_post= BlogPost.objects.get(id=blog_id)
    categories= Category.objects.all()
    similar_posts= BlogPost.objects.filter(category=blog_post.category).exclude(id=blog_post.id)

    context= {
        "post": blog_post,
        "categories": categories,
        "similar_posts": similar_posts
    }
    return render(request, "main/post.html", context)

def posts_by_category(request, category_name):
    post=BlogPost.objects.filter(category__name=category_name)
    context={
        "post": post
    }
    return render(request, "main/category_post.html", context)
