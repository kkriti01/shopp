# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


def image_upload_path(instance, filename):
    return filename


class Category(models.Model):
    """
    Product category table
    """
    parent = models.ForeignKey('self', null=True, blank=True)
    name = models.CharField(max_length=225, null=True)
    title = models.CharField(max_length=225, null=True)
    description = models.CharField(max_length=225, null=True)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    """
    product specification table
    """

    name = models.CharField(max_length=225, null=True)
    title = models.CharField(max_length=225, null=True)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=225, null=True)
    image = models.ImageField(null=True, blank=True, upload_to=image_upload_path)
    price = models.FloatField()

    def __unicode__(self):
        return self.name


class Cart(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
