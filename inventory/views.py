from django.shortcuts import render
from .models import Location, Product, ProductMovement

def Locations(request):
    return render(request,'Locations/Locations.html')

def ProductMovements(request):
    return render(request,'Productmovements/ProductMovements.html')       


# def product_balance_report(request):
#     # Retrieve all locations
#     locations = Location.objects.all()

#     # Create a dictionary to store product balances for each location
#     product_balances = {}

#     # Calculate product balances for each location
#     for location in locations:
#         # Initialize the balance for this location
#         location_balance = 0

#         # Calculate the balance by considering both movements to and from the location
#         movements_to_location = ProductMovement.objects.filter(to_location=location)
#         movements_from_location = ProductMovement.objects.filter(from_location=location)

#         for movement in movements_to_location:
#             location_balance += movement.qty

#         for movement in movements_from_location:
#             location_balance -= movement.qty

#         # Store the balance in the dictionary
#         product_balances[location] = location_balance

#     context = {
#         'product_balances': product_balances,
#     }

#     return render(request, 'inventory_app/product_balance_report.html', context)


def product_balance_report(request):
    # Retrieve all locations and products
    locations = Location.objects.all()
    products = Product.objects.all()

    # Create a dictionary to store product balances for each location and product
    product_balances = {}
    productTotal = {}

    #Assigning 0 all the product in productTotal
    for product in products:
        productTotal[product.name] = 0
    productTotal['Total'] = 0
    # Calculate product balances for each location and product
    for location in locations:
        location_name = location.name  # Replace with the actual field name
        product_balances[location_name] = {}
        total_balance = 0

        for product in products:
            product_name = product.name  # Replace with the actual field name 

            # Initialize the balance for this product at this location
            product_balance = 0

            # Calculate the balance by considering both movements to and from the location
            movements_to_location = ProductMovement.objects.filter(to_location=location, product=product)
            movements_from_location = ProductMovement.objects.filter(from_location=location, product=product)

            for movement in movements_to_location:
                product_balance += movement.qty

            for movement in movements_from_location:
                product_balance -= movement.qty

            # Store the product balance in the dictionary
            product_balances[location_name][product_name] = product_balance
            total_balance += product_balance
            productTotal[product_name] += product_balance
        
        product_balances[location_name]['Total']=total_balance
        productTotal['Total'] =+ total_balance
    product_balances['Total'] = productTotal

    context = {
        'product_balances': product_balances,
        'locations': locations,
        'products': products,
    }

    print(context)
    return render(request, 'inventory_app/product_balance_report.html', context)

