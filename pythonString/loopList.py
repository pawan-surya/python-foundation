thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print("x " + x)


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []


# for x in fruits:
#    if "a" in x:
#       newlist.append(x)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x] #newlist = [expression for item in iterable if condition == True]


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)

print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)