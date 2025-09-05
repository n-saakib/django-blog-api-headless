from rest_framework.routers import DefaultRouter

from blog import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')


urlpatterns = router.urls