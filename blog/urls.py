from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')


urlpatterns = [
    *router.urls,
    path('api-auth', include('rest_framework.urls')),
]