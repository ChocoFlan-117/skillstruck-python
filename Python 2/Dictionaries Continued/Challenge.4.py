#Fruit shopping list

shopping = {}

apples = 5
bananas = 7
strawberries = 3

apples1 = int(input("How many apples do you need? "))
bananas1 = int(input("How many bananas do you need? "))
strawberries1 = int(input("How many strawberries do you need? "))

if apples1 > 5:
    apples2 = apples1 - 5
    shopping["apples"] = apples2

if bananas1 > 7:
    bananas2 = bananas1 - 7
    shopping["bananas"] = bananas2

if strawberries1 > 3:
    strawberries2 = strawberries1 - 3
    shopping["strawberries"] = strawberries2


print(shopping)