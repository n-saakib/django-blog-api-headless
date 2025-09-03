from django.urls import path

from blog import views

urlpatterns = [
    path('posts/', views.post_list, name='list_create_post'),
    path('post/<int:post_id>/', views.post_detail, name='post-detail')
]