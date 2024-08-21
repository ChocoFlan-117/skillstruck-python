#Family Banquent#

seat8 = input("Who is seated at seat 8? ")

group = { 4: "Jared", 5: "McKann", 6: "Kyle", 7: "Summer", 8: seat8, }


#group[x] = group[y] + "Nelson" 
#Didn't work because I was calling for why as a key instead of as a value

for x,y in group.items():
    group[x] = y + " Nelson"

print(group)