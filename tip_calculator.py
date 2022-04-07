# Write a function called percentage_plus that takes a bill total and a tip percentage and returns (not prints) the total plus tip. 
# Create a second function called tip_calculator that asks the user for the bill total and the tip percentage. 
# Pass those values through to the tip_calculator function and then print the result in a nice format.

bill = input("What is the total bill? ")
percent = input("What percentage would you like to tip? ")
total = (float(bill) * (1 + float(percent) / 100))

def percentage_plus(bill, percent):
    return total

def tip_calculator(): 
    print(f"Total bill is ${total:0.2f}.")

tip_calculator()