# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse

from product import models

from serializers import ProductListingSerializer, CategoryListingSerializer, CartListingSerializer


def home(request):
    return render(request, 'index.html')


class ProductListingViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = ProductListingSerializer

    def get_queryset(self):
        """
        This view should return a list of all the products for
        the category as determined by the category id portion of the URL.
        """
        category_id = self.request.query_params.get('category_id', None)
        return models.Product.objects.filter(category_id=category_id)


class CategoryListingViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategoryListingSerializer


class CategoryProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductListingSerializer


def add_cart(request):
    body_data = json.loads(request.body)
    product_id = body_data['product_id']
    print product_id
    #product = models.Product.objects.get(id=int(product_id))
    cart_obj = models.Cart.objects.create(quantity=1, product_id=int(product_id))
    #cart_obj.product.id = product.id
    cart_obj.save()
    return JsonResponse({'results': 'success'})


def get_cart(request):
    cart = models.Cart.objects.all()
    count = cart.count()
    return JsonResponse({'cart': cart, 'count': count})


class CartListingViewSet(viewsets.ModelViewSet):
    queryset = models.Cart.objects.all()
    serializer_class = CartListingSerializer