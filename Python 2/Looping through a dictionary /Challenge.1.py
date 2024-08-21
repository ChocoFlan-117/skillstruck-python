#Secret Beach Day#

amanda = int(input("How many people is Amanda bringing? "))
jane = int(input("How many people is jane bringing? "))

group = { "Fred" : 12, "Jackson" : 15, "Sophie" : 20, "Amanda" : amanda, "Jane" : jane, }

total = 0

for x in group.values():
    total += x

print(total)