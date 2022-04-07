# Write a function called group_tip_calculator that asks the user for the bill total, the tip percentage, and the number of people. 
# Pass the total and percentage values to the percentage_plus function and then divide the result by the number of people in the group. 
# Print the total including the tip as well as the cost per person.

bill = input("What is the total bill? ")
percent = input("What percentage would you like to tip? ")
people = input("How many people are in the group? ")
total = (float(bill) * (1 + float(percent) / 100))
final = total / float(people)

def percentage_plus(bill, percent):
    return total

def group_tip_calculator(): 
    print(f"Total bill is ${total:0.2f}.")
    print(f"Each person should pay ${final:0.2f}.")

group_tip_calculator()