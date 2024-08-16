month = int(input("Month? "))

#supposedly invalid syntax
#works perfectly fine
def user_input(choice):
    if choice == 1 or choice == 3 or choice == 5 or choice == 7 or choice == 8 or choice == 10 or choice == 12:
        print(31)
    elif choice == 4 or choice == 6 or choice == 9 or choice == 11:
        print(30)
    elif choice == 2:
        print(28)
        print("29 during leap year")
    else:
        print("invalid")
    

user_input(month)