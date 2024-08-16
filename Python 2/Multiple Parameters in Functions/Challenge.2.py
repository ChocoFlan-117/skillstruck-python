#Find the smallest integer function

num1 = int(input("Integer 1: "))
num2 = int(input("Integer 2: "))

def func(num1, num2):
    if num1 > num2:
        print(num2)
    else:
        print(num1)

func(num1, num2)