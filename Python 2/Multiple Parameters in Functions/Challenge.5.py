#Spot the difference function

num1 = int(input("Integer: "))
num2 = int(input("Integer: "))
num3 = int(input("Integer: "))


def func(num1, num2, num3):
    if num1 == num2:
        print(3)
    elif num1 == num3:
        print(2)
    else:
        print(1)

func(num1, num2, num3)