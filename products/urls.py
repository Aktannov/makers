from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ProductViewSet, CategoryViewSet, OtthvViewSet, LikeViewSet, FavoritesViewSet, KorzinaViewSet, \
    ChatViewSet

router = SimpleRouter()
router.register('products', ProductViewSet)
router.register('category', CategoryViewSet)
router.register('otthv', OtthvViewSet)
router.register('like', LikeViewSet)
router.register('favorite', FavoritesViewSet)
router.register('korzina', KorzinaViewSet)
router.register('chat', ChatViewSet)

urlpatterns = [
    path('', include(router.urls))
]
