from django.contrib import admin
from django.urls import path,include
from . import views
from .views import AboutView

urlpatterns = [
    path('', views.home,name='home'),
    path('about/', AboutView.as_view(),name='about'),
]
