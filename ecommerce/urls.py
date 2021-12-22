import debug_toolbar
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from ecommerce.drf import views

router = routers.DefaultRouter()
router.register(r"api", views.AllProductsViewset, basename="allproducts")

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("demo/", include("ecommerce.demo.urls", namespace="demo")),
    path("__debug__/", include(debug_toolbar.urls)),
]
