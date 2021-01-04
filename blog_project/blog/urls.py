from django.urls import path, include
from .views import HomePageView, PostsView, PostsDetailsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('posts', PostsView.as_view(), name='de'),
    path('posts/<int:pk>', PostsDetailsView.as_view(), name='post_details'),
]