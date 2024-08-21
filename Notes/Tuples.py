#Notes:

#For indexing, a the beginning we start counting at 0, but from the end we start counting at -1

#The main difference about tuples is that they are unchangeable

#You cannot change, add to, or remove from the tuple.

#Example: 
instruments = ("clarinet", "piano", "drum", "violin")

print(instruments)
#('clarinet', 'piano', 'drum', 'violin')

#May look like a list but notice the use of parenthesis() instead of square brackets[]



#######################
#ACCESSING TUPLE ITEMS#
#######################
instruments = ("clarinet", "paino", "drum", "violin")

print(instruments[1])
#piano
#Tuples uses indexing so that means it starts counting at 0



###################
#NEGATIVE INDEXING#
###################
#You can also start counting indexing from the end of your tuple. (Starts counting at -1)

#Example:
instruments = ("clarinet", "piano", "drum", "violin")

print(instruments[-1])
#violin



##################
#RANGE OF INDEXES#
##################
#If you want to acces multiple values that appear right in a row, you can print out a range of indexes with one simple command.

#Example:
instruments = ("clarinet", "piano", "drum", "violin", "guitar")

print(instruments[1:3])
#('piano', 'drum')

#The first number is where you start your range and the second number is where you end your range.



#######################################
#CHECK IF AN ITEM EXISTS IN THE TUPLE#
#######################################
#Sometimes if you have a very large tuple with hundreds of items inside, it cane be useful to check if a certain item can be found inside the tuple.

#Example:
instruments = ("clarinet", "piano", "drum", "violin", "guitar")

if "piano" in instruments:
    print("The tuple contains the value of piano.")
else:
    print("The tuple does not contain the value of piano.")

    