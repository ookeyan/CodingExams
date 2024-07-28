# list: ordered and changeable duplicates are OK

fruits = ["apple", "orange", "banana", "pear", "grape", "peach"]
# print(fruits[1]) #index
# print(fruits[1:4:]) #range EXCLUSIVE
# print(fruits[::2]) # skip x units from the start
# print(fruits[::-1]) #reverse
# print(fruits[::-2]) #reverse and skip from the end
# print(fruits[5:1:-1]) #reverse and range EXCLUSIVE
# print(fruits[5:0:-2]) #reverse and range EXCLUSIVE with skip

# dir(fruits) #list all functions in a collection
# help(fruits) #explain all the functions in a collection

# print(len(fruits)) #return the len
# print("kiwi" in fruits) # in sees if something exists returns boolean
# fruits[0] = "pepper" #lists are changeable, reassign values
# fruits.append("pepper") # add an element to the end
# fruits.remove("banana") # remove any element FROM ANYWHERE
# fruits.insert(0, "pepper") #list where you want to put something
# fruits.sort() # sort, default alphabetical order
# fruits.reverse() # reverses the array's listing
# fruits.clear() #remove everything
# print(fruits.index("banana")) #get the index (FIRST APPERANCE) of any item
# print(fruits.count("apple")) #get the number of times an item occurs
# a = fruits.pop(3) #remove value at that index and return that value
# a = fruits.pop() # remove last value
# print(a)
print(fruits)



