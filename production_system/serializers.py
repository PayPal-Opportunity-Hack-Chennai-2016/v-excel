import json

from rest_framework import serializers

from production_system.models import Task
from production_system.models import Order
from production_system.models import Item
from production_system.models import Inventory
from production_system.models import Purchase
from production_system.models import Production
from production_system.models import ProductInventory
from production_system.models import MasterRawMaterial
from production_system.models import MasterTag


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    item_set = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('item_set', 'id', 'amount', 'customer_id', 'expected_timestamp', 'completed_timestamp')


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
