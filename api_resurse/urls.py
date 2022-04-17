from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_resurse.views import TitleViewSet, GenreViewSet, CategoryViewSet

router = DefaultRouter()

router.register('titles', TitleViewSet)
router.register('genres', GenreViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]