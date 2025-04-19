import re

# Common weak passwords to reject
WEAK_PASSWORDS = {"admin@123", "password", "password@123", "123456", "qwerty", "letmein", "welcome", "abc123", "monkey", "football", "123123", "password1", "1234", "passw0rd"}

# Function to check if the password is in our custom weak password list
def is_in_custom_list(password: str) -> bool:
    """
    Check if the given password exists in the custom weak password list.
    Returns True if found, False otherwise.
    """
    try:
        with open("custom_password_list.txt", "r", encoding="utf-8") as file:
            for line in file:
                if password.strip() == line.strip():
                    return True
    except FileNotFoundError:
        print("Warning: Custom password list not found. Skipping check.")
    return False

# Function to check the strength of a given password
def check_password_strength(password: str) -> int:
    """
    Check if the given password meets security criteria and return a strength score:
    - At least 8 characters long (20%)
    - Contains both uppercase and lowercase letters (20%)
    - Contains at least one digit (20%)
    - Contains at least one special character (20%)
    - Extra complexity (length > 12) (20%)
    
    Returns:
        int: Strength score from 0 to 100.
    """
    # Reject weak passwords
    if password.lower() in WEAK_PASSWORDS:
        return 0
    
    # Reject passwords found in custom password list
    if is_in_custom_list(password):
        return 0
    
    strength = 0
    
    # Check minimum length
    if len(password) >= 8:
        strength += 20
    
    # Check for at least one uppercase letter
    if re.search(r"[A-Z]", password):
        strength += 20
    
    # Check for at least one lowercase letter
    if re.search(r"[a-z]", password):
        strength += 20
    
    # Check for at least one digit
    if re.search(r"\d", password):
        strength += 20
    
    # Check for at least one special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 20
    
    return strength

# Main function to take user input and validate password strength
def main():
    """
    Prompts the user to enter a password and checks its strength using the check_password_strength function.
    Displays appropriate feedback based on the validation result.
    """
    print("""
    Password Creation Guidelines:
    - At least 8 characters long ✅
    - Contains both uppercase and lowercase letters 🔠
    - Includes at least one number 🔢
    - Has at least one special character (!@#$%^&* etc.) 🔐
    - Avoid common passwords like 'password', 'admin@123', etc. 🚫
    """)
    
    # Prompt user for password input
    password = input("Enter a password to check strength: ")
    
    # Get password strength score
    strength = check_password_strength(password)
    
    # Provide feedback based on strength score
    if is_in_custom_list(password):
        print("🚫 This password is found in our custom weak password list and is highly insecure! Please choose another. 🚫")
    elif strength == 100:
        print("🔥 Your password is very strong! (100%) 🔥")
    elif strength >= 80:
        print("✅ Strong password! (80%) ✅")
    elif strength >= 60:
        print("⚠️ Medium strength password. Consider improving it. (60%) ⚠️")
    elif strength >= 40:
        print("❗ Weak password! Try adding more complexity. (40%) ❗")
    elif strength == 0:
        print("🚫 This password is too common and insecure! Please choose another. 🚫")
    else:
        print("❌ Very weak password! (20% or less) ❌")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
