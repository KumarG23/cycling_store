import os
import django
from django.conf import settings
# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "cycling_store.settings"
django.setup()

print('SCRIPT START *************************')
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
# WORK BELOW
from datetime import date
from cycling_store_app.models import *


# vehicle_type = Vehicle(type='unicycle', number_in_stock=10)
# vehicle_type.save()

# vehicle_type = Vehicle.objects.filter(type='unicycle').first()
# vehicle_type.delete()

# print(vehicle_type)

# customer_name = Customer(name='John Doe')
# customer_name.save()

# customer_name = Customer(name='Marina Sharma')
# customer_name.save()

# vehicle_type = Vehicle(type='bicycle', number_in_stock=20)
# vehicle_type.save()

# vehicle_type = Vehicle(type='tricycle', number_in_stock=15)
# vehicle_type.save()

# customer = Customer.objects.get(name='John Doe')
# customer.name = 'Neal Sharma'
# customer.save()

# vehicle = Vehicle.objects.get(type='bicycle')




# customer = Customer.objects.get(name='Neal Sharma')

# order = CustomerOrder.objects.get(customer=customer)
# order_id = order.id

# print('id:', order.id)

# order_id = 1
# order = CustomerOrder.objects.get(pk=order_id)
# order.paid = True
# order.save()

# orders = CustomerOrder.objects.all()
# for order in orders:
#     print('Order: ', order)

# customers = Customer.objects.all()
# for customer in customers:
#     print('Customer: ', customer)

# vehicles = Vehicle.objects.all()
# for vehicle in vehicles:    
#     print('Vehicle: ', vehicle)

print('**********MENU**********')
print()
choice = input('What would you like to do? \nAdd to vehicles stock (1)  \nOrder a vehicle (2) \nDisplay inventory (3) \nCancel a customer order (4) \nMark order as paid (5) \nShow all orders (6)\n')

while choice not in ['1', '2', '3', '4', '5', '6']:
    choice = input('Please select the number associated with the action you would like to take.')

if choice == '1':
    choice = input('Which type of vehicle would you like to add?\nUnicycle (1) \nBicycle (2) \nTricycle (3) ')
    while choice not in ['1', '2', '3']:
        choice = input('Please select the number associated with the type of vehicle you want to add to stock (1, 2, or 3)')
    if choice == '1':
        unis = input('How many Unicycles would you like to add?   ')
        while not unis.isdigit():
            unis = input('Please enter a valid number: ')

        unis = int(unis)

        unicycles = Vehicle.objects.filter(type='unicycle')
        for unicycle in unicycles:
            unicycle.number_in_stock += unis
            unicycle.save()

        print(f'{unis} Unicycles added to stock successfully!')
    if choice == '2':
        bikes = input('How many bicycles would you like to add? ')
        while not bikes.isdigit():
            bikes = input('Please enter a valid number: ')

        bikes = int(bikes)

        bicycles = Vehicle.objects.filter(type='bicycle')
        for bicycle in bicycles:
            bicycle.number_in_stock += bikes
            bicycle.save()

        print(f'{bikes} Bicycles added to stock successfully!')

    if choice == '3':
        tri = input('How many tricycles would you like to add? ')

        while not tri.isdigit():
            tri = input('Please enter a valid number: ')

        tri = int(tri)

        tricycles = Vehicle.objects.filter(type='tricycle')
        for tricycle in tricycles:
            tricycle.number_in_stock += tri
            tricycle.save()


if choice == '2':        

    customer_name = input('Enter your name: ')
    customer, created= Customer.objects.get_or_create(name=customer_name)


    choice = input('What type of vehicle would you like? / Unicycle(1) / Bicycle(2) / Tricycle(3): ')
    while choice not in ['1', '2', '3']:
        choice = input('Please enter the number associated with your vehicle choice (1, 2, or 3)')
    if choice == '1':
        vehicle_type = 'unicycle'
    elif choice == '2':
        vehicle_type = 'bicycle'
    elif choice == '3':
        vehicle_type = 'tricycle'

    vehicle, created = Vehicle.objects.get_or_create(type=vehicle_type)

    vehicle.number_in_stock -=1
    vehicle.save()



    CustomerOrder.objects.create(
        customer=customer,
        order=vehicle,
        created_date=date.today(),
        paid=False
    )

    print('Order created successfully!')
    print('_' * 30)

if choice == '3':
    print()
    print('**********STOCK**********')
    vehicles = Vehicle.objects.all()

    for vehicle in vehicles:
        print(f'{vehicle.type}: {vehicle.number_in_stock}')

if choice == '4':
    order_to_cancel = input('Which order would you like to cancel (order ID): ')
    
    while not order_to_cancel.isdigit():
        order_to_cancel = input('Please enter your order ID number: ')

    order = CustomerOrder.objects.filter(id=order_to_cancel).first()
    
    if order:
        order.order.number_in_stock += 1
        order.order.save()
        order.delete()
        print('Order successfully deleted and stock updated!')
    else:
        print('No order found with that ID')

if choice == '5':
    paid = input('What order would you like to mark as paid (order ID)? ')

    while not paid.isdigit():
        input('Please enter your order ID')

    orders = CustomerOrder.objects.filter(id=paid)

    if orders.exists():
        for order in orders:
            order.paid = True
            order.save()
        print('Order successfully marked as paid')
    else:
        print('No order found with that ID')

if choice == '6':
        orders = CustomerOrder.objects.all()

        for order in orders:
            print('Order id: ', order.id)
            print('Customer: ', order.customer.name)
            print('Vehicle type: ', order.order.type)
            print('Order date: ', order.created_date)
            print('Paid', order.paid)
            print('-' * 30)

    





# orders = CustomerOrder.objects.all()

# for order in orders:
#     print('Order id: ', order.id)
#     print('Customer: ', order.customer.name)
#     print('Vehicle type: ', order.order.type)
#     print('Order date: ', order.created_date)
#     print('Paid', order.paid)
#     print('-' * 30)

# vehicles = Vehicle.objects.all()

# for vehicle in vehicles:
#     print(f'{vehicle.type}: {vehicle.number_in_stock}')










