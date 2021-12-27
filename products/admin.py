from django.contrib import admin
from .models import Category, Product, Comment, Like, Favorite, Chat

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Favorite)
admin.site.register(Chat)