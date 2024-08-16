#Dinosaurs

#NOT FINISHED#

name = input("Name of the dinosaur? ")
height = int(input("Height of the dinosaur? "))

dino = {}

while name != "triceratops":
    dino[name] = height
	name = input("What dino do you want to add?")
	height = int(input("How tall is your dinosaur?"))
    if name == "triceratops":
        dino[name] = height
	
print(dino)