import random 

number=random.randint(1,101)

choice=int(input("Enter a number between 1 and 100: "))

if choice>=1 and choice<=100:
    if choice==number:
        print(f"You guessed the number🎉")
    else:
        print(f"You guessed wrong😔.The number was {number}")
else:
    print("Enter number between 1 and 100❌")
    