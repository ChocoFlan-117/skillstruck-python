#Shoes#

person = input("One more person: ")
shoes = int(input("How many shoes they have: "))

group = { "Sally" : 10, "Cameron" : 3, "Spencer" : 6, person : shoes }

for x,y in group.items():
    print(x + " has " + str(y) + " pairs of shoes.")