from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ProductViewSet, CategoryViewSet

router = SimpleRouter()
router.register('products', ProductViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
