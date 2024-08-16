#Find the smallest of five function

num1 = int(input("Integer: "))
num2 = int(input("Integer: "))
num3 = int(input("Integer: "))
num4 = int(input("Integer: "))
num5 = int(input("Integer: "))

def func(num1, num2, num3, num4, num5):
    if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
        print(num1)
    elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
        print(num2)
    elif num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5:
        print(num3)
    elif num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5:
        print(num4)
    else:
        print(num5)

func(num1, num2, num3, num4, num5)