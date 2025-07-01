import random
import string

def generate_password(length):
    # Define the character sets to use for the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Prompt the user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 6 characters): "))
            if length < 6:
                print("Password length should be at least 6 characters. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Generate the password
    generated_password = generate_password(length)

    # Display the generated password
    print(f"Generated Password: {generated_password}")

if __name__ == "__main__":
    main()
