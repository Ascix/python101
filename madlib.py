# Ask the user for three inputs (a noun, a present-tense verb, and a name) and store the values in appropriately named variables.

# Next, write a function called madlib that takes three parameters: a noun, a present-tense verb, and a name. The function should print a story that uses these parameters to the console.

# Lastly, pass the three user inputs to the madlib function, so that when you execute the script, it asks the user for input, and then prints out the madlib story.

noun = input("Enter a noun: ")
verb = input("Enter a present-tense verb: ")
name = input("Enter a name: ")

def madlib():
    print(f"""There once was a {noun} that suddenly came to life, called themselves {name} and starting {verb} around the town.
{name} decided that {verb} was unacceptable and decided to move to the countryside an live a life of solitude.""")

madlib()