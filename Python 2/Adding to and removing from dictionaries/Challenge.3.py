#Goals

remove = input("What goal do you not have time for? ")

goals = { "piano" : 5, "run" : 3, "paint" : 2, "serve" : 7, "homework" : 7}

goals.pop(remove)

print(goals)