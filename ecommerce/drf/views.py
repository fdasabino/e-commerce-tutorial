from ecommerce.drf.serializer import AllProducts
from ecommerce.inventory.models import Product
from rest_framework import mixins, permissions, viewsets


class AllProductsViewset(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    """
    Serialize the permission set.
    """

    queryset = Product.objects.all()
    serializer_class = AllProducts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"
