# Importing random module
import random

# List containing alphabets, numbers and special characters
char = list(string.ascii_letters + string.digits + "!@#$%^&*")

# Empty list to store password characters
password = []

# Taking password length input from user
length = int(input("Enter the Length : "))

# Loop runs according to the entered length
for i in range(length):

    # Selecting random character and adding to password list
    password.append(random.choice(char))

# Converting list into string
pass_list = "".join(password)

# Printing heading
print("----- Generated Password -----")

# Printing generated password
print("Your generated password is:",pass_list)

# Success message
print("Successfully Generated")
