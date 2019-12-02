from django.contrib import admin
from django.urls import path,include
from .views import (
BlogHomeListView,
BlogDetailView,
BlogCreateView,
BlogUpdateView,
BlogDeleteView,
BlogUserListView,
BlogCategoryListView,
BlogSearchListView)


urlpatterns = [
    path('blog/', BlogHomeListView.as_view(),name='blog-home'),
    path('blog/user/<str:username>/', BlogUserListView.as_view(),name='blog-user'),
    path('blog/search/<str:search>', BlogSearchListView.as_view(),name='blog-search'),
    path('blog/categorie/<str:categoryname>/', BlogCategoryListView.as_view(),name='blog-category'),
    path('blog/<int:pk>/', BlogDetailView.as_view(),name='blog-detail'),
    path('blog/new/',BlogCreateView.as_view(),name='blog-create'),
    path('blog/update/<int:pk>/',BlogUpdateView.as_view(),name='blog-update'),
    path('blog/delete/<int:pk>/',BlogDeleteView.as_view(),name='blog-delete'),
]
