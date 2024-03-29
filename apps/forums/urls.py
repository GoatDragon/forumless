from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('post/<post_id>', views.post),
    path('newcomment/<post_id>', views.newcomment),
    path('newpost/', views.newpost),
    path('upvote/<post_id>', views.upvote),
    path('downvote/<post_id>', views.downvote)
]
