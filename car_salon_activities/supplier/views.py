"""
views.py: File, containing views for a supplier application.
"""


from typing import ClassVar
from rest_framework import status, viewsets
from django.db.models.query import QuerySet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from supplier.models import SupplierModel
from supplier.services import SupplierService
from supplier.serializers import (
    SupplierSerializer,
    SupplierHistorySerializer,
    SupplierCarDiscountSerializer,
)


class SupplierViewSet(viewsets.ModelViewSet):
    """
    SupplierViewSet: Handling every action for a Supplier resource.
    Maps HTTP methods to actions:
        HEAD -> list
        HEAD -> retrieve
        GET -> list
        GET -> retrieve
        POST -> create
        PUT -> update
        PATCH -> partial_update
        DELETE -> destroy

    Args:
        viewsets.ModelViewSet (_type_): Builtin superclass for a SupplierViewSet.
    """

    queryset: ClassVar[QuerySet[SupplierModel]] = SupplierModel.objects.all()

    serializer_class: ClassVar[type[SupplierSerializer]] = SupplierSerializer

    service: ClassVar[SupplierService] = SupplierService()

    permission_classes: ClassVar[list] = [IsAdminUser]

    def destroy(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        """
        destroy: Instead of deleting from database this method set suppliers's is_active to False.

        Args:
            request (Request): Request instance.

        Returns:
            Response: HTTP 204 Response if supplier can be deleted otherwise HTTP 401/403.
        """

        self.service.delete_supplier(self.get_object())
        return Response(status=status.HTTP_204_NO_RESPONSE)

    @action(methods=['get'], detail=True, serializer_class=SupplierHistorySerializer)
    def get_statistics(self, request: Request, pk: int) -> Response:
        """
        get_statistics: Returns statistics for suppliers's operations.

        Args:
            request (Request): Request instance.
            pk (int): Supplier's pk.

        Returns:
            Response: HTTP 200 if has permissions otherwise 401/403.
        """

        supplier: SupplierModel = self.get_object()
        history = supplier.history.all()
        serializer: SupplierSerializer = self.get_serializer(history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, serializer_class=SupplierCarDiscountSerializer)
    def make_discount(self, request: Request, pk: int) -> Response:
        """
        make_discount: Creates supplier car discount.

        Args:
            request (Request): Request instance.
            pk (int): Supplier's pk.

        Returns:
            Response: HTTP 200 if has permissions otherwise 401/403.
        """

        serializer: SupplierCarDiscountSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)