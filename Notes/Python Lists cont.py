#Notes:
#my_list = [int(n) for n in input().split()]
#is used to create a list of integers with input
#(variable "n" can be changed to anything, whether that be a letter or word. Numbers cannot be entered alone, will cause syntax error.)
#Input should be seperated by spaces. No commas, parenthesis, or brackets are needed.
#Input example: 2 6 8 33 24 2
#String can be put within input()
#Example: my_list = [int(n) for n in input("Insert here").split()]

######
#STEP#
######
#smells = ["skunk", "lilac", "rain", "ocean", "garbage", "cleaner", "cookies"]
#print(smells[0:6:2])
#['skunk', 'rain', 'garbage']

#0 is the starting index ("skunk")
#6 is the ending index, it goes up but does not include 6. That is why it doesn't print "cleaner" or "cookies" because "cleaner" is the 6th index but isn't included so it's not printed (neither is "cookies because it's the 7th index)
#2 is the step of the slice which means that it prints every second item within the list ranging from 0 to 6

#steps can be other values beside 2, which means they would print every (insert number) item within the list ranging through any decided range
#example:
#smells = ["skunk", "lilac", "rain", "ocean", "garbage", "cleaner", "cookies", "roses", "perfume", "grass", "grapes"] 
#("skunk" = 0 | "cookies" = 6 | "cleaner" = 5)
#print(smells[0:6:5])
#['skunk', 'cleaner']

#when [] is involved it counts through indexing (starts at 0)
#len(listName) doesn't abide by this, instead starting at 1

############
#REPLACMENT#
############
#smells = ["skunk", "lilac", "rain", "ocean", "garbage", "cleaner", "cookies"]
#smells[3] = "perfume"
#print(smells)
#["skunk", "lilac", "rain", "perfume", "garbage", "cleaner", "cookies"]

#With the index value being 3 it will replace that list item with the new given item so "ocean" was replaced by "perfume"

########
#LENGTH#
########
#Can find out how many items are in a list by calling:
#len(listName)

#smells = ["skunk", "lilac", "rain", "ocean", "grabage", "cleaner", "cookies"]
#print(len(smells))
#7

#this will count how many items there are in the list (doesn't count through indexing, starts counting at 1 instead of 0)

######
#SORT#
######
#.sort() method will sort the given list alphabetically (A - Z)

#smells = ["skunk", "lilac", "rain", "ocean", "garbage", "cleaner", "cookies"]
#smells.sort()
#print(smells)
#['cleaner', 'cookies', 'garbage', 'lilac', 'ocean', 'rain', 'skunk']

#can also be used to sort numerically (lowest - highest)
#cookies [3, 55, 9, 12, 13]
#cookies.sort()
#print(cookies)
#[3, 9, 12, 13, 55]

#to sort in reverse: (reverse=True)
#cookies = [3, 55, 9, 12, 13]
#cookies.sort(reverse=True)
#print(cookies)
#[55, 13, 12, 9, 3]