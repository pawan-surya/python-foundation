"""
Title: Smart Lantern Inventory System (Python Syntax & Data Types Practice)
Objective
Build a small inventory management system for lanterns and oils that forces you to use all major Python data types, syntax constructs
, and core features. The goal is to practice Python fundamentals in a realistic scenario before moving on to frameworks like FastAPI.

Requirements
1. Data Types to Use
- Numbers (int, float): Track product prices and stock counts.
- Strings: Store product names and descriptions.
- Lists: Maintain a collection of available products.
- Tuples: Store immutable metadata (e.g., brand, year).
- Sets: Track unique suppliers.
- Dictionaries: Map product IDs to product details.
- Booleans: Flag whether a product is in stock.
- None: Represent discontinued or unavailable products.

2. Syntax Constructs
- Conditionals: Use if/elif/else to check stock levels.
- Loops:
- for loop to iterate over products.
- while loop to simulate daily sales until stock runs out.
- Functions:
- Add a product.
- Remove a product.
- Search for a product by name.
- Calculate total inventory value.
- List Comprehensions: Filter products under a certain price.
- Exception Handling: Gracefully handle errors (e.g., product not found).
- Formatted Output: Use f‑strings for clean printing

3. Features to Implement
- Add Product
- Accept product ID, name, price, stock, and metadata.
- Store in dictionary.
- Remove Product
- Delete product by ID.
- Handle case where product doesn’t exist.
- Search Product
- Find product by name.
- Return details or “not found.”
- Inventory Value
- Calculate total value of all products in stock.
- Out‑of‑Stock List
- Return all products with stock = 0.
- Daily Sales Simulation
- Use a while loop to reduce stock until empty.
- Print daily status.


4. Stretch Goals
- Add user input (e.g., input() for product search).
- Add sorting (e.g., by price or stock).
- Add file I/O (save/load inventory from a text file).
- Add basic class (Product) to practice OOP.

 Deliverables
- A single Python script that demonstrates:
- All major data types.
- Core syntax (loops, conditionals, functions).
- Error handling.
- Clean, formatted output.

Next Step
Once you complete this script, we’ll upgrade it into a FastAPI backend:
- Each function (add, remove, search, etc.) becomes an API endpoint.
- Inventory data can be served via JSON responses.
- You’ll practice request handling, routing, and response models.

"""
from random import *

"Project Theme: Smart Lantern Inventory System"
"""Level 1 Basic Data Types and Syntax Practice

- Use integers for stock counts.
- Use floats for prices.
- Use strings for product names.
- Use booleans to mark availability (True/False).
- Use None to represent discontinued products.
Tasks:
- Create 5 products with these attributes.
- Print them using formatted strings (f"...").
- Practice arithmetic (e.g., total stock, average price).

"""

for i in range(5):
    product_id = i + 1
    name = f"Lantern Model {chr(65 + i)}"
    price = round(uniform(10.00,100.00),2)
    stock = randint(0,20)
    available = stock > 0
    discontinued = None if available else "Discontinued"
    supplier = f"Supplier {chr(88 + i)}"
    brand_year = (f"Brand {chr(77 + i)}", 2020 + i)
    # print(f"Product ID: {product_id}, Name: {name}, Price: ${price}, Stock: {stock}, Available: {available}, Status: {discontinued}")


"""" Level 2 Collections

- Lists: Store all product names.
- Tuples: Store immutable metadata like (brand, year).
- Sets: Track unique suppliers.
- Dictionaries: Map product IDs to details.
Tasks:
- Build a dictionary of products with nested details.
- Extract product names into a list.
- Add supplier names into a set.
- Store brand/year in tuples.

"""   

products = dict()
product_names = list()
suppliers = set()
brand_year = tuple()


for i in range(5):
    product_id = i + 1 
    name = f"Lantern Model {chr(65 + i)}{chr(80 + i + 1)}"
    price = round(uniform(10.00,100.00),2)
    stock = randint(0,9)
    available = stock > 0
    supplier = f"Supplier{chr(65 + i*2)}"
    brandyear = (f"Brand  {chr(65 + i)}{chr(80 + i + 1)}", 2020 + i)
    products[product_id] = {
        "name": name,
        "price": price,
        "stock": stock,
        "available": available,
        "supplier": supplier,
        "brand_year": brandyear
    }
    product_names.append(name)
    suppliers.add(supplier)
    brand_year += brandyear



# print("\n Map product IDs to details:", products)
# print("\n Lists: Store all product names:", product_names)
# print("\n Sets: Track unique suppliers:", suppliers)
# print("\n Tuples: Store immutable metadata like (brand, year):", brand_year)



""""
Level 3: Control Flow
Goal: Use loops and conditionals.
- For loops: Iterate over products.
- While loops: Simulate daily sales until stock runs out.
- Conditionals: Check if stock is low, out, or healthy.
Tasks:
- Print all products with stock > 0.
- Simulate selling 1 unit per day until stock = 0.
- Print “Out of stock” when finished

"""

for product_id, details in products.items():
     if details["stock"] > 0:
        print(f"Product ID: {product_id}, Name: {details['name']}, Stock: {details['stock']} - In Stock")
     else:
        print(f"Product ID: {product_id}, Name: {details['name']} - Out of Stock")

# Simulate daily sales
for product_id, details in products.items():
    print(f"\nSimulating sales for Product ID: {product_id}, Name: {details['name']}")
    while details["stock"] > 0:
        details["stock"] -= 1
        print(f" Sold 1 unit. Remaining stock: {details['stock']}")
    print(" Out of stock!")

