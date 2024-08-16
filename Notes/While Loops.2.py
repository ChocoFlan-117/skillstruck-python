#Notes:
#While loops are used while something is true
#It keeps looping until the condition is no longer being met so it's a must to include a way to stop the loop.

#If statements are allowed within a while loop just like any other code.

#people_in_line = 20
#while people_in_line > 0:
#   print("There are " + str(people_in_line) + " people in line. Keep the coaster running!")
#   people_in_line = people_in_line - 1

#This loop will run until while there are people in line.
#Every run of the loop, it subtracts 1 from the variable "people_in_line"
#Every time the loop runs it checks for people in line but if the line is empty then the "people_in_line" condition is no longer met which means the while loop ends.

####################
#DECREMENT OPERATOR#
####################
#people_in_line = people_in_line - 1
#Everytime the loop runs the variable will be subtracted by one. This means the variable will become a smaller and smaller integer unti; the condition is met. (This situation the condition is people_in_line == 0)
#A simpler way to write this is "people_in_line -= 1"

####################
#INCREMENT OPERATOR#
####################
#people_in_line = people_in_line + 1
#people_in_line += 1

#To increment a variable you would do: "variable += 1"
#That's the shorter form of "variable = variable + 1"
#(variable + 1 will not work because it only performs the addition operation and then discards the result instead of modfying the value of the variable. It doesn't store the value.)

