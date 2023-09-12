import random

num1 = random.randint(1, 100)
a = 1
while a <= 3:
    num2 = int(input("Enter your Guess:"))
    if num1 == num2:
        print("YOUR GUESS IS CORRECT")
        break
    else:
        print("WRONG GUESS")
        if num1 > num2:
            print("Your Guess is Lower than My Guess")
        else:
            print("Your Guess is Higher than My Guess")
    a += 1
    if a == 3:
        print("-------Last chance to guess-------")
    if a > 3:
        print(f"my guess number is {num1}")
