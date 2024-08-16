#Notes:

##############
#ADDING ITEMS#
##############
#You can add new items to the dictionary.

#Example:
classmates = {
    "Billy": 8,
    "Vance": 15, 
    "Alice": 10
}

classmates["Lily"] = 6

print(classmates)
#{'Billy': 8, 'Vance': 15, 'Alice': 10, 'Lily': 6}


#You can also create an empty dictionary and add items to that as well.

#Example:
friends = {}

friends["Lily"] = 6
friends["James"] = 10

print(friends)
#{'Lily': 6, 'James': 10}



################
#REMOVING ITEMS#
################
#You can remove items from the dictionary by using the pop method.

#Example:
classmates = {
    "Billy": 8,
    "Vance": 15,
    "Alice": 10,
    "Lily": 6,
    "Xavier": 12
}

print(classmates)

classmates.pop("Alice")

print(classmates)
#{'Billy': 8, 'Vance': 15, 'Alice': 10, 'Lily': 6, 'Xavier': 12}
#Alice is then removed due to the pop method
#{'Billy': 8, 'Vance': 15, 'Lily': 6, 'Xavier': 12}

