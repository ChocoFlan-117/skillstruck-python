#All the pets

pets = {
    "fish": 30,
    "dogs": 2, 
    "chickens": 5, 
    "cats": 2,
    "bunnies": 1,
}

pets["fish"] = 20
pets["bunnies"] = 7

print("Because 10 fish died, and the bunny had 6 babies, you now have " + str(pets["fish"]) + " fish and " + str(pets["bunnies"]) + " bunnies at your house.")

print(pets)