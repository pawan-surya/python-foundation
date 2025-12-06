import time
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


a = 12
b = 15

if a == b:
    print("TRUE")
else:
    print("false")

def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    time.sleep(2)
    countdown(n - 1)

countdown(5)