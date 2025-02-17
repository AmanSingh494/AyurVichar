from django.contrib import admin
from django.urls import path, include

# connecting views.py
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("services/", views.services, name='services'),
    path("contact/", views.contact, name='contact' ),
    path("prakruti/", views.prakruti, name="prakruti"),
    path("login/", views.loginUser, name="login"),
    path("register/", views.registerUser,  name = "register"),



]
