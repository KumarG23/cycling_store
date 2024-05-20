# vehicle_type = Vehicle(type='unicycle', number_in_stock=10)
# vehicle_type.save()

# customer = Customer.objects.get(name='John Doe')
# vehicle = Vehicle.objects.get(type='bicycle')

# customer = Customer.objects.get(name='John Doe')
# customer.name = 'Neal Sharma'
# customer.save()

# order_id = 1
# order = CustomerOrder.objects.get(pk=order_id)
# order.paid = True
# order.save()



# vehicle_type = Vehicle.objects.filter(type='unicycle').first()
# vehicle_type.delete()

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

# customer = Customer.objects.filter(name='Neal Sharma').first()
# customer.delete()

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