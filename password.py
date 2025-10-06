import random
import string

def generate_password(length=12, include_upper=True, include_lower=True, include_digits=True, include_symbols=True):
    """
    Generate a secure random password based on user preferences.
    
    Args:
    - length (int): Length of the password (default 12).
    - include_upper (bool): Include uppercase letters.
    - include_lower (bool): Include lowercase letters.
    - include_digits (bool): Include digits.
    - include_symbols (bool): Include special symbols.
    
    Returns:
    - str: The generated password.
    """
    # Define character sets
    characters = ''
    if include_lower:
        characters += string.ascii_lowercase
    if include_upper:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation  # Includes !@#$%^&* etc.
    
    if not characters:
        raise ValueError("At least one character type must be included.")
    
    # Use random.SystemRandom for better security (cryptographically secure)
    secure_random = random.SystemRandom()
    password = ''.join(secure_random.choice(characters) for _ in range(length))
    
    # Ensure at least one of each selected type (for better strength)
    if include_lower and string.ascii_lowercase not in password:
        password = password[:-1] + secure_random.choice(string.ascii_lowercase)
    if include_upper and string.ascii_uppercase not in password:
        password = password[:-1] + secure_random.choice(string.ascii_uppercase)
    if include_digits and string.digits not in password:
        password = password[:-1] + secure_random.choice(string.digits)
    if include_symbols and string.punctuation not in password:
        password = password[:-1] + secure_random.choice(string.punctuation)
    
    return password

def assess_password_strength(password):
    """
    Simple assessment of password strength.
    
    Returns:
    - str: 'Weak', 'Medium', 'Strong', or 'Very Strong'.
    """
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    
    score = length // 4  # Base score from length
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_symbol: score += 1
    
    if score >= 5:
        return "Very Strong"
    elif score >= 3:
        return "Strong"
    elif score >= 2:
        return "Medium"
    else:
        return "Weak"

def main():
    print("=== Secure Password Generator ===")
    print("Generate strong, random passwords for your accounts.")
    
    while True:
        try:
            length = int(input("\nEnter password length (8-50, default 12): ") or 12)
            if not 8 <= length <= 50:
                print("Length must be between 8 and 50. Using default 12.")
                length = 12
        except ValueError:
            print("Invalid input. Using default 12.")
            length = 12
        
        include_upper = input("Include uppercase letters? (y/n, default y): ").lower() != 'n'
        include_lower = input("Include lowercase letters? (y/n, default y): ").lower() != 'n'
        include_digits = input("Include numbers? (y/n, default y): ").lower() != 'n'
        include_symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'
        
        num_passwords = input("How many passwords to generate? (1-10, default 1): ") or 1
        try:
            num_passwords = int(num_passwords)
            if not 1 <= num_passwords <= 10:
                num_passwords = 1
        except ValueError:
            num_passwords = 1
        
        print(f"\n--- Generated Passwords (Length: {length}) ---")
        for i in range(num_passwords):
            password = generate_password(length, include_upper, include_lower, include_digits, include_symbols)
            strength = assess_password_strength(password)
            print(f"{i+1}. {password} (Strength: {strength})")
        
        if input("\nGenerate more? (y/n): ").lower() != 'y':
            break
    
    print("Stay secure! Remember to store passwords safely (e.g., in a manager).")

if _name_ == "_main_":
    main()