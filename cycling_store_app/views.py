from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

# Create your views here.

from .models import *
from .serialize import *

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerOrderViewSet(viewsets.ModelViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer

class HandlebarViewSet(viewsets.ModelViewSet):
    queryset = Handlebar.objects.all()
    serializer_class = HandlebarSerializer

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer