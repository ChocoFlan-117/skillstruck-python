#Notes:

#Looping through a dictionary is done similarly to looping through a list


#####################
#PRINT OUT KEY NAMES#
#####################
#Example: (This will print out the keys in the dictionary)
classmates = {
    "Billy": 8,
    "Vance": 12,
    "Alice": 10,
    "Eliza": 15,
    "Xavier": 6,
}

for x in classmates:
    print(x)
#Billy
#Vance
#Alice
#Eliza
#Xavier



######################
#PRINT OUT THE VALUES#
######################
#Example: (This will print out the values in the dictionary)
classmates = {
    "Billy": 8,
    "Vance": 12,
    "Alice": 10,
    "Eliza": 15,
    "Xavier": 6,
}

for x in classmates.values():
    print(x)
#8
#12
#10
#15
#6



################################
#PRINT OUT BOTH KEYS AND VALUES#
################################
#Example: (This will print out both the keys and the values in the dictionary.)
classmates = {
    "Billy": 8,
    "Vance": 12,
    "Alice": 10,
    "Eliza": 15,
    "Xavier": 6,
}

for x,y in classmates.items():
    print(x,y)
#Billy 8
#Vance 12
#Alice 10
#Eliza 15
#Xavier 6



########################################
#LOOPING THROUGH A DICTIONARY CONTINUED#
########################################
#Loops can be particularly useful when you combine them with other code, such as an IF statement.
#Example:
classmates = {
    "Billy": 8,
    "Vance": 12,
    "Alice": 10,
    "Eliza": 15,
    "Xavier": 6,
}

for x in classmates: 
    if x == "Eliza":
        print("This person want to be anonymous")
    else:
        print(x)
#Billy
#Vance
#Alice
#This person want to be anonymous
#Xavier

#This for loop runs through each student's name and checks to see if the name is Eliza. If it is Eliza, it will print out the string, "This person wants to be anonymous" instead of the name ELiza. If it is not Eliza, it will print x. (The x in this example is the keys in the dictionary)



##########################################
#USING A FOR LOOP TO CREATE A DICTIONARY#
##########################################
#For loops can also be used to create dictionaries.

#Example:
periods = int(input("How many class periods do you have? "))
schedule = {} 
#^ Empty dictionary 
for i in range(periods):
    #^ Using range(), it creates a for loop that will run as many times as the input named periods. (For example, it will run 4 times if periods input was 4)
    subject = input("What subject? ")
    num_people = input("How many people are in your " + subject + " class?")
    #^ For each loop through the range named periods, it will ask for two inputs: a subject and the number of people in that class.
    if subject not in schedule:
        schedule[subject] = num_people
        #^ Python dictionaries cannot have duplicate keys so there's an if statement to see if that key already exists in the dictionary. 
        #If it doesn't, it's added to the dictionary.
print(schedule)
#^ After the for loop has run as many times within the range(), the dictionary is then printed.