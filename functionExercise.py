
first_name = input("What is your first name?")
last_name = input("What is your last name?")
domain = input("What company do you work for?")

# user greeter
def greeting():
    print("Top of the morning to you, " + first_name + " " + last_name)

# greeting()

# email generator
def email():
    print(first_name[0].lower() + "." + last_name.lower() + "@" + domain.lower() + ".com")

# email()

# username generator
def username():
    print(first_name[0:3] + "_" + last_name[0:5])


# new user contact info
def contact():
    greeting()
    print("Email:") + email()
    
    username()

contact()