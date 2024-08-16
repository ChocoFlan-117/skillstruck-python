#A party for the letter c!

letter = "c"
letter2 = "C"
#Wouldn't allow me to go ahead with 
#letter = "C" and "c"
#even though it worked fine

snack = input("Snack or activity ")

food = str(list(snack))
def allowed(yum):
	if letter in food or letter2 in food:
		print(snack + " can be a part of the party!")
		
	elif letter not in food or letter not in food:
		print("Sorry! " + snack + " doesn't start with the letter c!")
		
		
allowed(snack)