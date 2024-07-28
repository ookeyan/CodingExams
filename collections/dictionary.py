#dictionary: a collection of key value pairs {key:value}
# ordered and changeable NO DUPLICATES
people = {"cop": "gun", "fireman": "hose", "nurse": "needle", "teacher": "ruler"}

# print(dir(people)) #get all attributes
# print(help(people))
# print(people.get("cop")) #get value from key
# if/else statement: if people.get("clown") else... #conditions if something does(n't) exist
# people.update({"clown": "balloon"}) #add a new entry or UPDATES an existing one
# people.pop("cop") #retrieve and remove a key value pair
# people.popitem() #remove the latest key value pair
# people.clear() #clear the dictionary
# keys = people.keys() # get all the keys
# values = people.values() #get all the values
items = people.items() # returns A LIST OF TUPLES [(), (), ()] of key val pairs
for key, value in people.items():
    print(f"{key}: {value}")

# print(values)
# print(people)
