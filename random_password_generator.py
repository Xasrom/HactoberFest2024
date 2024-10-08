import random
import string

def generate_password(length=12):
    # Define the characters that the password can contain
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password contains at least one lowercase, one uppercase, one digit, and one special character
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list into a string and return
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    generated_password = generate_password(password_length)
    print("Generated password:", generated_password)
