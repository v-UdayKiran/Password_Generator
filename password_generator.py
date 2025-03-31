import random
import string

def generate_password(length):
    """Generate a secure password of given length."""
    if length < 3:
        raise ValueError("Password length must be at least 3.")
    
    # Ensure the password contains at least one letter, one digit, and one special character
    characters = string.ascii_letters + string.digits + string.punctuation
    password = (
        random.choice(string.ascii_letters) +
        random.choice(string.digits) +
        random.choice(string.punctuation) +
        ''.join(random.choices(characters, k=length - 3))
    )
    
    return ''.join(random.sample(password, len(password)))

def main():
    """Main function to generate passwords without user input."""
    num_passwords = 4  # Predefined number of passwords
    password_lengths = [4, 4, 4, 4]  # Predefined lengths for each password
    
    print(f"Generating {num_passwords} passwords")
    
    passwords = [generate_password(length) for length in password_lengths]
    
    print("\nGenerated Passwords:")
    for idx, password in enumerate(passwords, start=1):
        print(f"Password #{idx}: {password}")

if __name__ == "__main__":
    main()
