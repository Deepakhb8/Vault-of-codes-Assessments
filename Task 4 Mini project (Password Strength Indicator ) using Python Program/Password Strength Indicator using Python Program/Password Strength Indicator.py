import re

def password_strength(password):
                                      
    length = len(password)   # Initialize variables to track different aspects of password strength
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))  # You can modify the special character list as needed

                                    
    if length > 8:# Check password length
        return "strong"
    elif 6 < length <= 8:
        return "medium"
    elif length <= 5:
        return "weak"

    if has_upper and has_lower and has_digit and has_special:# Check other criteria
        return "strong"
    elif (has_upper or has_lower) and has_digit:
        return "medium"

    return "weak"


user_password = input("Enter your password: ")# Get the user's password from the login page (you need to implement this


strength = password_strength(user_password)# Check the strength of the password


if strength == "strong":# Display the strength indicator
    print("Password is strong.")
elif strength == "medium":
    print("Password is medium.")
else:
    print("Password is weak.")
