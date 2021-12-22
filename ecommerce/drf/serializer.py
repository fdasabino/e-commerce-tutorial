from ecommerce.inventory.models import Product
from rest_framework import serializers


class AllProducts(serializers.ModelSerializer):
    """
    Serialize the permission set.
    """

    class Meta:
        model = Product
        fields = "__all__"
        read_only = True
        editable = False
