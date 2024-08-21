#Boxes#

box5 = int(input("Box 5 value: "))

group = { "box1" : 5, "box2" : 2, "box3" : 10, "box4" : 3, "box5" : box5 }

total = 0

for x in group.values():
    total2 = 25 * x
    total += total2

print(total)