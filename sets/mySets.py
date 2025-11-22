# Set items are unchangeable, but you can remove items and add new items. No Duplicated

myset = {"apple", "banana", "cherry"}


# Access set item
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


  # add item in sets
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# remove item from sets\
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#loop\
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


  #Unioun of sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#forzen set
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))