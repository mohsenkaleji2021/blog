from django.urls import path
from .views import BlogView, BlogDetail, AddPost, PostLike , PostUnlike

urlpatterns = [
    path('', BlogView.as_view(), name='home'),
    path('post/<pk>', BlogDetail.as_view(), name='detail'),
    path('addarticle/', AddPost, name='addarticle'),
    path('like/<postid>', PostLike, name='postlike'),
    path('unlike/<postid>', PostUnlike, name='postunlike'),
    
]