"""
serializers.py: File, containing serializers for a showroom application.
"""


from typing import ClassVar
from rest_framework import serializers
from showroom.models import ShowroomModel, ShowroomHistory, ShowroomCarDiscount


class ShowroomSerializer(serializers.ModelSerializer):
    """
    ShowroomSerializer: Serializes showroom json to py-native types and vice versa.

    Args:
        serializers.ModelSerializer (_type_): Builtin superclass for a ShowroomSerializer.
    """

    class Meta:
        model: ClassVar[type[ShowroomModel]] = ShowroomModel

        fields: ClassVar[list] = [
            'created_at',
            'last_updated',
            'is_active',
            'name',
            'creation_year',
            'balance',
            'location',
            'charts',
            'appropriate_cars',
            'current_suppliers',
            'number_of_sales',
            'discount_for_unique_customers',
        ]

        read_only_fields: ClassVar[list] = [
            'created_at',
            'last_updated',
            'is_active',
            'appropriate_cars',
            'current_suppliers',
        ]


class ShowroomCarDiscountSerializer(serializers.ModelSerializer):
    """
    ShowroomCarDiscountSerializer: Serializes shroom discount json to pynative types and vice versa.

    Args:
        serializers.ModelSerializer (_type_): Builtin supclass for a ShowroomCarDiscountSerializer.
    """

    class Meta:
        model: ClassVar[type[ShowroomCarDiscount]] = ShowroomCarDiscount

        fields: ClassVar[list] = [
            'created_at',
            'last_updated',
            'is_active',
            'name',
            'description',
            'precent',
            'start_date',
            'finish_date',
            'showroom',
        ]

        read_only_fields: ClassVar[list] = [
            'created_at',
            'last_updated',
            'is_active',
        ]


class ShowroomHistorySerializer(serializers.ModelSerializer):
    """
    ShowroomHistorySerializer: Serializes showroom history json to py-native types and vice versa.

    Args:
        serializers.ModelSerializer (_type_): Builtin superclass for a ShowroomHistorySerializer.
    """

    class Meta:
        model: ClassVar[type[ShowroomHistory]] = ShowroomHistory

        fields: ClassVar[list] = [
            'created_at',
            'last_updated',
            'is_active',
            'showroom',
            'car',
            'sale_price',
            'customer',
        ]

        read_only_fields: ClassVar[list] = [
            'created_at',
            'last_updated',
            'is_active',
            'showroom',
            'car',
            'sale_price',
            'customer',
        ]