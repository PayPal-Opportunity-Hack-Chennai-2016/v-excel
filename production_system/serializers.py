import json

from rest_framework import serializers

from people.models import Customer
from production_system.models import Task
from production_system.models import Order
from production_system.models import Item
from production_system.models import Inventory
from production_system.models import Purchase
from production_system.models import Production
from production_system.models import ProductInventory
from production_system.models import MasterRawMaterial
from production_system.models import MasterTag
from service_and_process.serializers import MasterServiceSerializer, MasterProductSerializer
from v_excel_inventory.lib.base_serializers import DynamicFieldsModelSerializer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

    service = MasterServiceSerializer(read_only=True)
    product = MasterProductSerializer(read_only=True)

    class Meta:
        model = Item
        fields = '__all__'


class BasicCustomerSerializer(serializers.ModelSerializer):
    # phone_number = serializers.BiIntegerField()

    def validate_phone_number(self, val):
        if len(str(val)) != 10:
            raise serializers.ValidationError('The phone number must be 10 digits long')
        return val

    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(DynamicFieldsModelSerializer):
    item_set = ItemSerializer(many=True, read_only=True)
    customer = BasicCustomerSerializer()

    class Meta:
        model = Order
        fields = ('item_set', 'id', 'amount', 'customer', 'expected_timestamp', 'completed_timestamp')


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = '__all__'


class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = '__all__'


class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterRawMaterial
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterTag
        fields = '__all__'
