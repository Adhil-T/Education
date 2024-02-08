from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("404", views.notfound, name="404"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("courses", views.courses, name="courses"),
    path("", views.index, name="index"),
    path("team", views.team, name="team"),
    path("testimonial", views.testimonial, name="testimonial"),
]