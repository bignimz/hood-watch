from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('neighborhood-list/', views.neighborhoodView, name='neighborhood-list'),
    path('neighborhood-detail/<int:pk>', views.neighborhoodDetail, name='neighborhood-detail'),
    path('create-hood/', views.createNeighborhood, name='create-hood'),
    path('update-hood/<int:pk>', views.updateNeighborhood, name='update-hood'),
    path('delete-hood/<int:pk>', views.deleteNeighborhood, name='delete-hood'),

    path('post-list/', views.postView, name='post-list'),
    path('post-detail/<int:pk>', views.postDetail, name='post-detail'),
    path('create-post/', views.createPost, name='create-post'),
    path('update-post/<int:pk>', views.updatePost, name='update-post'),
    path('delete-post/<int:pk>', views.deletePost, name='delete-post'),
    
]