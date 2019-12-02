from django.urls import path
from .views import ProfileDetailView

urlpatterns = [
    # path('', views.blog_home,name='profile-list'),
    path('<username>/', ProfileDetailView.as_view(),name='profile-detail'),
]
