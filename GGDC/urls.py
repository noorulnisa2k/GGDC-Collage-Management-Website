from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import download_books, home, vision, mission, history, principal, intermediat, bsc, degree_programs, admission, faculty, about, gallery, blog_cat, blog_post, download_books, login_user, logout_user, register


urlpatterns = [
    path('',home),
    path('index',home),
    path('vision',vision),
    path('mission',mission),
    path('history',history),
    path('principal',principal),
    path('intermediat',intermediat),
    path('bsc',bsc),
    path('degree_programs',degree_programs),
    path('register',register),
    path('faculty',faculty),
    path('about',about),
    path('gallery',gallery),
    path('blog_cat',blog_cat),
    path('blog_post',blog_post),
    path('books',download_books),
    path('login',login_user),
    path('logout',logout_user),
    path('admission',admission),




]