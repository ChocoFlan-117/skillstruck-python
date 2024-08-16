#How many are equal function

num1 = int(input("Integer 1: "))
num2 = int(input("Integer 2: "))
num3 = int(input("Integer 3: "))

def func(num1, num2, num3):
    if num1 == num2 and num1 == num3:
        print(3)
    elif num1 == num2 or num2 == num3 or num1 == num3:
        print(2)
    else:
        print(0)

func(num1, num2, num3)