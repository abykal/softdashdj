from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.home, name='dashboard'),
    path('billing/', views.billing, name='billing'),
    path('profile/', views.profile, name='profile'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('tables/', views.tables, name='tables'),
    path('vr/', views.vr, name='virtualreality'),
]