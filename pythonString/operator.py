sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# The Walrus Operator
numbers = [1, 2, 3, 4, 5]
count = len(numbers)

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

   
# identity Operators
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)
print(x is x)

# Membership Operators
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
fruit = ["apple", "banana", "cherry"]
print("pineapple" not in fruit)