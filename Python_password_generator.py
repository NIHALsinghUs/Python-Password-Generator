# Importing random module
import random

# List containing alphabets, numbers and special characters
char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        '0','1','2','3','4','5','6','7','8','9',
        '!','@','#','$','%','^','&','*']

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