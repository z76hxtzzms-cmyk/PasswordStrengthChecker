# Import getpass module to securly get user input without displaying it on the screen.
import getpass
# Import regex so we can count if there is an occurence in password.
import re

# Create a counter, will be used to determine strength of password
counter = 0

# List of common passwords to avoid. Found using sources from NordPass.
common_passwords = ["123456", "admin", "12345678", "123456789", "12345", "password", "Aa123456", "Pass@123", "admin123"]

# Ask user for password. The getpass module will hide the input for security reasons.
password = getpass.getpass("Enter Password: ")

# If password found in common_passwords, print message and terminate program.
if password in common_passwords:
    print("The password you entered is too common. Please choose a stronger password.")
    exit()


# Moved length check higher. Should be priortized to at least have 8 characters
if len(password) >= 12:
    print("Password is 12+ characters, +2")
    counter+=2
elif 8 <= len(password) < 12:
    print("Password is 8+ characters, +1")
    counter+=1
else:
    print("Password must be at least 8 characters!")
    exit()

# Check if password has at least one number, if so increment


if re.search(r'\d', password):
    print("Password has a number, +1")
    counter+=1
else:
    print("Password is missing a number")

# Check if password has at least one capital letter, if so, increment

if re.search(r"[A-Z]", password):
    print("Password has a capital letter, +1")
    counter+=1
else:
    print("Password is missing a capital letter")


# Now check if we have at least one lowercase

if re.search(r"[a-z]", password):
    print("Password has a lowercase letter, +1")
    counter+=1
else:
    print("Password is missing a lowercase letter")


# Search for special characters
if re.search(r"[!@#$%^&*]", password):
    print("Password has a special character, +1")
    counter+=1
else:
    print("Password is missing a special character")
