from  django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import register,logout_confirm,user_profile,home_page,add_blog_post


urlpatterns=[
    path('register/',register, name="user-register"),
    path('login/',LoginView.as_view(template_name="Accounts/login.html"),name="user-login"),
    path('logout/',LogoutView.as_view(),name="user-logout"),
    path('confirm-logout/',logout_confirm, name="logout"),
    path('profile/',user_profile,name="profile"),
    path('homepage/',home_page,name="home-page"),
    path('add-post/',add_blog_post,name="add-blog-post"),
    
]