import random

# # Coin flip

print("You flipped a coin!")
if random.randint(1,100) <= 50:
    print("It is heads!")
else:
    print("It is tails!")

# # Even Odd

number = int(input("Enter a number: "))

if (number % 2) == 0:
    print("It's Even!")
else:
    print("It's Odd!")

# Dice Roller

num1 = 1

def diceRoller(num1,sides):
    return random.randint(num1,sides)

print("Let's roll a dice!")
sides = int(input("How many sides should it have? (2-20): "))
diceRoller(num1,sides)
if ? >= 2 and ? <= 20:
    print("It's rolling...")
    print(f"It's a {diceRoller(num1,sides)}!")
else:
    print("That is not a number within the range!")
