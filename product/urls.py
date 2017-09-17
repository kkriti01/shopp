from django.conf.urls import url, include
from rest_framework import routers

from product import views

from views import CategoryListingViewSet, ProductListingViewSet, CartListingViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryListingViewSet)
router.register(r'product', ProductListingViewSet)
router.register(r'cart', CartListingViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^$', views.home, name="home"),
    url(r'^add_cart/$', views.add_cart, name="add_cart"),
    #url(r'^get_cart/$', views.get_cart, name="get_cart"),
]