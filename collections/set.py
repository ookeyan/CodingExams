# set = {} unordered and immutable NO DUPLICATES. Can add or remove GOOD FOR CONSTANTS

fruits = {"apple", "orange", "banana", "pear", "grape", "peach"}
fruits2 = {"apple", "orange", "kiwi", "pear", "grape", "cherry"}
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits)) #get len of set
# print("pineapple" in fruits) # does it exist
# fruits.add("blueberry") #add to set
# fruits.remove("grape") #remove
# a = fruits.pop("grape") # remove and retrieve
# fruits.pop() #remove random element
# fruits.clear() #delete everything
# fruits.discard("pear") #the same as remove
# b = fruits.difference(fruits2) # return difference in set 1
# fruits.difference_update(fruits2) # update THE difference in set 2 to original
# b = fruits.intersection(fruits2) # get everthing IN COMMON from both sets
# b = fruits.symmetric_difference(fruits2) # get ALL UNCOMMON THINGS from both sets
# fruits.symmetric_difference_update(fruits2) #update to ALL UNCOMMON THINGS from both sets
# print(fruits.union(fruits2)) # combine both

# print(b)
print(fruits)