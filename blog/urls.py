from django.urls import include, path
from rest_framework.authtoken import views as authtoken_views
from rest_framework.routers import DefaultRouter

from blog import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')


urlpatterns = [
    *router.urls,
    path('api-auth', include('rest_framework.urls')),
    path('api-token-auth/', authtoken_views.obtain_auth_token, name='auth-token'),
]