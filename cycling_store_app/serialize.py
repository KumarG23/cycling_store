from rest_framework import serializers
from .models import *

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id','type', 'number_in_stock', 'handlebar', 'color']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name']

class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = ['id', 'customer', 'order', 'created_date', 'paid']

class HandlebarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handlebar
        fields = ['id', 'name', 'handlebars_in_stock']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name']