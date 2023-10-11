def math_add (x,y):
    print (x+y)
def math_sub (x,y):
    print (x-y)
def math_dev (x,y):
    if x or y == 0:
     print("Can't divide by zero")
    elif x and y !=0 :
     print(x/y)
def math_mult (x,y):
    print(x*y)

opperation = input("Calculator add, multiply, divsion, or subtract ").lower()
if opperation.lower() == "add":
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    result = math_add(x,y)
elif opperation.lower() == "subtract":
     x = float(input("Enter the first number: "))
     y = float(input("Enter the second number: "))
     result = math_sub(x,y)
elif opperation.lower() == "multiply":
     x = float(input("Enter the first number: "))
     y = float(input("Enter the second number: "))
     result = math_mult(x,y)
elif opperation.lower() == "divsion":
     x = float(input("Enter the first number: "))
     y = float(input("Enter the second number: "))
     result = math_dev(x,y)
else:
    print("invald Input")
