from django.contrib.gis import serializers
from rest_framework import serializers

from people.models import Customer
from people.models import InternalUser
from production_system.serializers import OrderSerializer


class CustomerSerializer(serializers.ModelSerializer):
    order_set = OrderSerializer(many=True, exclude_fields=('customer', ))

    def validate_phone_number(self, val):
        if len(str(val)) != 10:
            raise serializers.ValidationError('The phone number must be 10 digits long')
        return val

    class Meta:
        model = Customer
        fields = '__all__'


class InternalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalUser
        fields = '__all__'
