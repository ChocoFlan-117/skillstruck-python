#Notes:
#Functions can be useful when one has written code but aren't ready to run it. So it can be written out and called upon later.
#Also incredibly useful for pieces of code that'll be repeated as it helps to make the code easier, simpler, and far more clean. (It also saves you the stress of retyping/copying and pasting the code.)

#Functions are written as "def name():"
#Example:
#def weather():
#   print("It's a soggy day outside!")

#This won't print out anything when ran, instead leaving a blank terminal.
#In order to use a function it's necessary to call it out.

#Example:
#def weather():
#   print("It's a soggy day outside!")
#weather()
#It's a soggy day outside!

##################################
#LOCAL AND GLOBAL SCOPE VARIABLES#
##################################
#Creating a variable inside a function is called a local variable. Only being used inside the function.
#Variables that are create outside of functions are called global variables. Global variables can be used anywhere in the program.

#Example:
#favorite = "I love juice"
#def myfunction():
#   fruit = "apple"
#   print(fruit)
#myfunction()
#print(favorite)
#I love juice
#apple

#"fruit" is the local variable (inside of function)
#"favorite" is the global variable (outside of function)

#To create a variable inside a function and have it as a global variable then the "global" keyword must be used.

#Example:
#favorite = "I love juice"
#def myfunction():
#   global fruit
#   fruit = "apple"
#   print(fruit)
#myfunction()
#print(favorite)
#print(fruit)
#I love juice
#apple

#The variable can now be used outside of the function due to be named "global".

############
#PARAMETERS#
############
#Function parameters is what goes within the parentheses of the function.
#Example: (Within this example the parameter is the word "type")
#def weather(type):
#  print("It's a soggy day outside because it is " + type)
#weather()
#(this will result in an error, in "arguments" it goes farther)

###########
#ARGUMENTS#
###########
#To determine what the parameter is you would have to say so when you call upon the function.

#Example:
#def weather(forecast):
#   print("It's a soggy day outside because it is " + forecast)
#weather("raining")
#It's a soggy day outside because it is raining

#In the example, the argument is the string "raining"
#The function takes that string ("raining") and puts it inside the string using concatenation. The value of "raining" is the function's argument. (The information inside the parentheses that gets passed into a function)

#Example: (When the function is called multiple times with different parameters)
#def weather(forecast):
#    print("It's a soggy day outside because it is " + forecast)
#weather("raining")
#weather("snowing")
#weather("drizzling")
#It's a soggy day outside because it is raining
#It's a soggy day outside because it is snowing
#It's a soggy day outside because it is drizzling