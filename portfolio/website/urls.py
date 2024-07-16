from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('resume/',views.resume),
    path('projects/',views.projects),
    path('contact/',views.contact),
]