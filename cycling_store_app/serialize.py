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

    def create(self, validated_data):
        vehicle = validated_data.get('order')
        handlebar = validated_data.get('handlebar')

        if vehicle.number_in_stock > 0 and handlebar.handlebars_in_stock > 0:
            vehicle.number_in_stock -= 1
            handlebar.handlebars_in_stock -= 1

            vehicle.save()
            handlebar.save()

            order = CustomerOrder.objects.create(**validated_data)
            return order
        
        else:
            raise serializers.ValidationError('Insufficient Stock')

class HandlebarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handlebar
        fields = ['id', 'name', 'handlebars_in_stock']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name']