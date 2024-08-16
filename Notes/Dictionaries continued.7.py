#Notes:


###################
#DICTIONARY LENGTH#
###################
#You can check to see how many items are in the dictionary.
#When counting the length it starts at 1

#len(name)

#Example:
classmates = {
    "Billy": 8,
    "Vance": 15,
    "Alice": 10,
    "Lily": 6,
    "Xavier": 12
}

print(len(classmates))
#5


###############################
#CHECK IF KEY IS IN DICTIONARY#
###############################
#You're also able to check a dictionary for a certan key

#Example:
classmates = {
    "Billy"
    "Vance": 15,
    "Alice": 10,
    "Lily": 6,
    "Xavier": 12
}

if "Vance" in classmates:
    print("Vance is in your dictionary")
#Vance is in your dictionary


#Also is able to use "not in" to check your dictionary

#Example:
classmates = {
    "Billy"
    "Vance": 15,
    "Alice": 10,
    "Lily": 6,
    "Xavier": 12
}

if "Shelby" not in classmates:
    print("Shelby is not in your dictionary")
#Shelby is not in yout dictionary


########################################
#CONVERTING FROM A LIST TO A DICTIONARY#
########################################
#You can change a list to a dictionary by adding values to the list items. 
#The items in the list become the keys of your dictionary.

#Example:
garden = ["pumpkins", "squash", "corn", "tomatoes"]
#The list ^

garden_dictionary = dict.fromkeys(garden, "Harvested")
#The list being converted into a dictionary ^ 
#Garden: key | "Harvested": value

print(garden_dictionary)
#{'pumpkins': 'Harvested', 'squash': 'Harvested', 'corn': 'Harvested', 'tomatoes': 'Harvested'}