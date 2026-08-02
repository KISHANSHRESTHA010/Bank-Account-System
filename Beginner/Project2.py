def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def remainder(x,y):
    return x%y

while True:
    print("=========WELCOME TO SIMPLE CALCULATOR=========")
    
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    choice=input("Enter a operator: ").lower()

    if choice=='+':
        print(f"{x}+{y} = {add(x,y)}")
    elif choice=='-':
        print(f"{x}-{y}={subtract(x,y)}")
    elif choice=='*':
        print(f"{x}*{y}={multiply(x,y)}")
    elif choice=='/':
        print(f"{x}/{y}={divide(x,y)}")
    elif choice=='%':
        print(f"{x}%{y}={remainder(x,y)}")
    elif choice=='exit':
        print("Exiting........")
        break
    else:
        print("Invalid operator")
