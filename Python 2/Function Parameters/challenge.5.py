year = int(input("Year? "))

def leap_year(leap):
    if leap % 4 == 0 and leap % 100 != 0:
        print("Leap year!")
    else:
        print("Not a leap year.")

leap_year(year)