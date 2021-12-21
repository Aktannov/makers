
from django.urls import path, include
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls))
]