from rest_framework import serializers


from product import models


class ProductListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = ('id', 'name', 'title', 'quantity', 'description', 'category', 'image', 'price')


class CategoryListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ('id', 'name', 'title', 'parent', 'description')


class CartListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cart
        fields = ('id', 'product', 'quantity')