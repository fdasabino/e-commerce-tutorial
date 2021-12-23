from ecommerce.inventory.models import *
from rest_framework import serializers


class MediaSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ["image", "alt_text"]
        read_only = True

    def get_image(self, obj):
        return self.context["request"].build_absolute_uri(obj.image.url)


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        exclude = ["id"]
        depth = 2


class BrandSerializer(serializers.ModelSerializer):
    """
    Returns brand name
    """

    class Meta:
        model = Brand
        fields = ["name"]


class AllProducts(serializers.ModelSerializer):
    """
    All products
    """

    class Meta:
        model = Product
        fields = "__all__"
        read_only = True
        editable = False


class ProductInventorySerializer(serializers.ModelSerializer):
    """
    Returns a list of items in the inventory
    """

    brand = BrandSerializer(many=False, read_only=True)
    attributes = ProductAttributeValueSerializer(
        source="attribute_values", many=True
    )
    image = MediaSerializer(source="media_product_inventory", many=True)

    class Meta:
        model = ProductInventory
        fields = [
            "sku",
            "image",
            "store_price",
            "is_default",
            "product",
            "product_type",
            "brand",
            "attributes",
        ]
        read_only = True
