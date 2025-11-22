from random import random, randint, uniform

products = dict() # collection of key-value pair order and changeable Duplicates not allowed - Faster access
product_list = list() # Ordered and chnageable Duplicates allowed
suppliers = set() # Unordered and unchangeable Duplicates not allowed
brand_year = tuple() # Ordered and unchangeable Duplicates allowed - Faster access

# print(dir(products))
# print(help(products))


def add_product(product_id,name,price,stock,supplier,brandyear):
    products[product_id] = {
        "name": name,
        "price": price,
        "stock": stock,
        "available": stock > 0,
        "supplier": supplier,
        "brand_year": brandyear
    }
    product_list.append(products[product_id])
    return products

def remove_product(product_id):
    try:
        del products[product_id]
        print(f"Product ID {product_id} removed.")
        return products
    except KeyError:
        print(f"Error: Product ID {product_id} not found.")

#cheap_products = dict(filter(lambda item: item[1] and item[1]["price"] < 200, products.items()))
def search_product(name):
    for product_id, details in products.items():
        if details["name"] == name:
            return details
    return "Product not found."

def total_inventory_value():
    total_value = 0.0
    for details in products.values():
        total_value += details["price"] * details["stock"]
    return total_value        


stock = randint(0,9)
price = round(uniform(100.0, 1100.0), 2)
product_name = f"Lantern {chr(65) + str(randint(3,6))}{chr(80) + str(randint(0,4))}"
available = stock > 0 
supplier = f"Supplier{chr(65) + str(randint(0,8))}"
brandyear = (f"Brand  {chr(65) + str(randint(1,6))}{chr(80) + str(randint(0,2))}", 2020 + randint(0,4))
discontinued = None if available else "Discontinued"
product_id = randint(25,100)

for i in range(30):
    add_product(product_id,product_name,price,stock,supplier,brandyear)

# print("\n Current Products:", products)
# print("\n Search Product:", search_product(product_name))
# print("\n Total Inventory Value:", total_inventory_value())
# print("\n Delete Product:", remove_product(product_id))

print(len(product_list), products)
#cheap_products = dict(filter(lambda item: item[1] and item[1]["price"] < 200, products.items()))
cheap_items = list(p for p in product_list if  p["price"] < 560)

    



print(f"\n cheap_items of Products:", cheap_items, len(cheap_items))
