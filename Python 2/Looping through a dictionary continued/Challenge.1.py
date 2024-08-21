#Check for a key

dictionary = { 7: "first", 3: "second", 4: "third", 8: "fourth", 9: "fifth" }

my_list = [int(n) for n in input().split()]

for x in my_list:
    if x in dictionary:
        print("Yes")
    else:
        print("No")