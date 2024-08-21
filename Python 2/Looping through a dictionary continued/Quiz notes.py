#############
#When an IF statement is inside a FOR loop, how many times will the IF statement run?    
#The IF statement will run each time the program loops.
#############



##############
#True or False: You can create an empty dictionary.
#True
##############



#############
#True or False: Dictionaries can have duplicate keys
#False
#########



###############
#What will the following code print out?
classmates = {
    "Billy" : 8,
    "Vance" : 12,
    "Alice" : 10,
    "Eliza" : 15,
    "Xavier" : 6,
}

for x in classmates:
    if x == "Kate":
        print("This person wants to be anonymous")
    else:
        print(x)

#Billy Vance Alice Eliza Xavier
##################



################
#What will the following code print out?
classmates = {
    "Billy" : 8,
    "Vance" : 12,
    "Alice" : 10,
    "Eliza" : 15,
    "Xavier" : 6,
}

for x in classmates:
    if x == "Billy":
        print("This person wants to be anonymous")
    else:
        print(x)

#This person wants to be anonymous Vance Alice Eliza Xavier
###################