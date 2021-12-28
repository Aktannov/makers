from django.contrib.auth import get_user_model
from rest_framework import serializers
from products.models import Product, Category, Comment, Like, Favorite, Chat, Korzina

User = get_user_model()

class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OtthvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['product', 'text', 'rating']

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValudationError('Рейтинг должен быть от 1 до 5')
        return rating

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create(validated_data)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['product', 'like']

    def validate_like(self, like):
        if like not in range(1, 2):
            raise serializers.ValudationError('Можно поставить только 1 лайк')
        return like

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create(validated_data)


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['product', 'favorite']

    def validate_favorite(self, favorite):
        if favorite == 'Избранное' or favorite == 'избранное':
            return favorite
        return serializers.ValudationError('Если хотите добавть в избранные напишите: "Избранное"')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create(validated_data)

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

class KorzinaSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Korzina
        fields = ['product', 'korzina']

    def validate_korzina(self, favorite):
        if favorite == 'в корзине':
            return favorite
        return serializers.ValudationError('Если хотите добавть в корзину напишите: "в корзине"')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create(validated_data)





