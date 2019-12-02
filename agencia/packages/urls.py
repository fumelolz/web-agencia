from django.contrib import admin
from django.urls import path,include
from .views import (PackagesHomeView,PackagesInternationalView,PackagesNationalView,PackagesSingleView)

urlpatterns = [
    path('packages/', PackagesHomeView.as_view(),name='package-home'),
    path('packages/international/', PackagesInternationalView.as_view(),name='package-international'),
    path('packages/national/', PackagesNationalView.as_view(),name='package-national'),
    path('packages/<int:pk>/', PackagesSingleView.as_view(),name='package-detail'),
]
