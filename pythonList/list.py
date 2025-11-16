mylist = ['apple', 'banana', 'cherry']
# print(mylist[0])
# print(mylist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# print(thislist[:4])
# print(thislist[2:3])

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"


# change the item list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]


#Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]


# Add item in list
thislist = ["apple", "banana", "cherry"]
thislist.insert(0, "surya")
thislist.append("orange")


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya", {"name": "John"}]
# thislist.extend(tropical)
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# thisdict = {"name": "John", "age": 36}
# thislist.extend(thisdict)
# print(thislist)
# print(thislist[8])

thislist.remove({'name': 'John'})
print(thislist)
thislist.pop(1)
# thislist.clear()
# del thislist

