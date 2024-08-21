#Add it All Together#

key = int(input("Key: "))
value = int(input("Value: "))

group = { 3 : 10, 5 : 3, 10 : 6, 4 : 30, key : value }

total = 0

for x,y in group.items():
    total += x * y

print(total)