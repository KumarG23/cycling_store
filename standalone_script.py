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

# handlebar_type = Handlebar(name='Golden Handlebar', handlebars_in_stock=20)
# handlebar_type.save()

# handlebar_type = Handlebar(name='Frilly Handlebar', handlebars_in_stock=20)
# handlebar_type.save()

# handlebar_type = Handlebar(name='Chopper Handlebar', handlebars_in_stock=20)
# handlebar_type.save()

# parts = Vehicle.objects.filter(number_in_stock='20').first()
# parts.delete()

# color_type = Color(name='Blue')
# color_type.save()

# green, red, orange, blue





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
    choice = input('Which type of vehicle would you like to add?\nUnicycle (1) \nBicycle (2) \nTricycle (3) \nGolden Handlebar (4) \nFrilly Handlebar (5) \nChopper Handlebar (6): ')
    while choice not in ['1', '2', '3','4', '5', '6']:
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

        print(f'{tri} Tricycles added to stock successfully!')
    
    if choice == '4':
        gold = input('How many Golden Handlebars would you like to add? ')

        while not gold.isdigit():
            gold = input('Please enter a valid number: ')
        
        gold = int(gold)

        golden_handles = Handlebar.objects.filter(name='Golden Handlebar')
        for golden_handle in golden_handles:
            golden_handle.handlebars_in_stock += gold
            golden_handle.save()

        print(f'{gold} Golden Handlebars added to stock successfully!')

    if choice == '5':
        frilly = input('How many Frilly Handlebars would you like to add? ')

        while not frilly.isdigit():
            frilly = input('Please enter a valid number: ')

        frilly = int(frilly)

        frilly_handles = Handlebar.objects.filter(name='Frilly Handlebar')
        for frilly_handle in frilly_handles:
            frilly_handle.handlebars_in_stock += frilly
            frilly_handle.save()

        print(f'{frilly} Frilly Handlebars added to stock successfully!')

    if choice == '6':
        chopper = input('How many Chopper Handlebars would you like to add? ')

        while not chopper.isdigit():
            chopper = input('Please enter a valid number: ')

        chopper = int(chopper)

        chopper_handles = Handlebar.objects.filter(name='Chopper Handlebar')
        for chopper_handle in chopper_handles:
            chopper_handle.handlebars_in_stock += chopper
            chopper_handle.save()

        print(f'{chopper} Chopper Handlebars added to stock successfully!')

        



elif choice == '2':        

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

    color_choice = input('What color would you like? Green(1), Red(2), Orange(3), Blue(4): ')
    while color_choice not in ['1', '2', '3', '4']:
        color_choice = input('Please choose the number associated with your color choice (1, 2, 3, 4)')
    if color_choice == '1':
        color_choice = 'Green'
    elif color_choice == '2':
        color_choice = 'Red'
    elif color_choice == '3':
        color_choice = 'Orange'
    elif color_choice == '4':
        color_choice  = 'Blue'

    handles = input('What type of handlebar would you like? Golden Handlebar(1), Frilly Handlebar(2), Chopper Handlebar(3): ')
    while handles not in ['1', '2', '3']:
        handles = input('Please choose the number associated with your handlebar choice (1, 2, 3)')
    if handles == '1':
        handles = 'Golden Handlebar'
    elif handles == '2':
        handles = 'Frilly Handlebar'
    elif handles == '3':
        handles = 'Chopper Handlebar'

    handlebar = Handlebar.objects.get(name=handles)

    handlebar.handlebars_in_stock -=1
    handlebar.save()

    
    color = Color.objects.get(name=color_choice)

    vehicle, created = Vehicle.objects.get_or_create(type=vehicle_type)

    vehicle.number_in_stock -=1
    vehicle.save()



    CustomerOrder.objects.create(
        customer=customer,
        order=vehicle,
        color=color,
        handlebar=handlebar,
        created_date=date.today(),
        paid=False
    )

    print('Order created successfully!')
    print('_' * 30)

elif choice == '3':
    print()
    print('**********STOCK**********')
    vehicles = Vehicle.objects.all()
    handles = Handlebar.objects.all()

    for vehicle in vehicles:
        print(f'{vehicle.type}: {vehicle.number_in_stock}')
    for handle in handles:
        print(f'{handle.name}: {handle.handlebars_in_stock}')

elif choice == '4':
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

elif choice == '5':
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

elif choice == '6':
        orders = CustomerOrder.objects.all()

        for order in orders:
            print('Order id: ', order.id)
            print('Customer: ', order.customer.name)
            print('Vehicle type: ', order.order.type)
            print('Color choice: ', order.color)
            print('Handlebar choice: ', order.handlebar)
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










