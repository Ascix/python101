firstname = "Brice"
lastname = "Tran"

# user greeter
greeting = "Hello " + firstname + " " + lastname
# print(greeting)

# email generator
email_generator = firstname[0] + "." + lastname + "@umbrellacorp.com"
# print(firstname[0] + "." + lastname + "@umbrellacorp.com")

# username generator
username_generator = firstname[0:3] + "_" + lastname[0:5]
# print(firstname[0:3] + "_" + lastname[0:5])

# new user contact information
print(greeting, 
    "Email: " + email_generator.lower(), 
    "Username: " + username_generator.lower(), sep='\n')

# f string
