#Notes:

#Dictionaries are ordered, changeable, and indexed.

#Example:
classmates = {
    "Billy" : 8,
    "Vance" : 12,
    "Alice" : 10,
}

print(classmates)
#{'Billy': 8, 'Vance': 12, 'Alice': 10}

#Notice the use of curly braces { } and how each item in the dictionary is a pair. This pairing is a big difference between dictionaries and lists. Dictionary values appear as pairs. 
#The first item in the pairing is called a key. The second item in the pairing is called a value.

#Example: (Dictionary that uses strings as the value)
names = {
    "person1" : "George",
    "person2" : "Brenda",
    "person3" : "Larry",
    "person4" : "Aaliyah",
}

print(names)
#{'person1': 'George', 'person2': 'Brenda', 'person3': 'Larry', 'person4': 'Aaliyah'}


###################################
#ACCESSING ITEMS IN THE DICTIONARY#
###################################
#To access certain items within the dictionary you must name the dictionary and use brackets around it.

#Example:(Prints just the value)
classmates = {
    "Billy" : 8,
    "Vance" : 12,
    "Alice" : 10,
}

print(classmates["Vance"])
#12

#This method accesses the value paired with the key named Vance.


###################################
#CHANGING VALUES IN THE DICTIONARY#
###################################
#Example:
classmates = {
    "Billy" : 8,
    "Vance" : 12,
    "Alice" : 10,
}

classmates["Alice"] = 15

print(classmates)
#{'Billy': 8, 'Vance': 12, 'Alice': 15}