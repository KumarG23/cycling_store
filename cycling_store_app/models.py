from django.db import models

# Create your models here.

class Vehicle(models.Model):
    type = models.TextField()
    number_in_stock = models.PositiveIntegerField()

    def __str__(self):
        return f'type: {self.type}, stock: {self.number_in_stock}'


class Customer(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'name: {self.name}'


class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    created_date= models.DateField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Customer: {self.customer}, order: {self.order}, Date: {self.created_date}, Paid: {self.paid}'