from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from products.filters import ProductFilter
from products.models import Product, Category, Comment, Like, Favorite, Chat
from products.permissions import IsAdmin, IsAuthor
from products.serializer import ProductSerializer, CategorySerializer, OtthvSerializer, LikeSerializer, \
    FavoritesSerializer, ChatSerializer


class ProductViewSet(ModelViewSet):
    # permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = ['name', 'price']
    ordering_fields = ['name', 'price']

    @action(['GET'], detail=True)
    def comments(self, request, pk):
        product = self.get_object()
        comments = product.comments.all()
        serializer = OtthvSerializer(comments, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        return [AllowAny()]



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OtthvViewSet(CreateModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin,
                     ListModelMixin,
                     GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = OtthvSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        if self.action == 'retrieve':
            return [AllowAny()]
        else:
            return [IsAuthor()]




class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        if self.action == 'list':
            return [IsAuthenticated()]
        return [IsAuthor()]


class FavoritesViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoritesSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        if self.action == 'list':
            return [IsAuthenticated()]
        return [IsAuthor()]

class ChatViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated()]
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer









