import random
import string

# Function to ask yes/no questions
def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print("Only 'y' and 'n' are accepted as answers.")

def main():

    # Ask user for password length
    length = int(input("Enter the desired password length: "))

    # Validate password length
    if length < 1:
        print("Password length must be at least 1.")
        exit(1)
    if length > 100:
        print("Password length must not exceed 100 characters.")
        exit(1)

    # Ask user for character types to include
    include_uppercase = ask_yes_no("Include uppercase letters? (y/n): ")
    include_lowercase = ask_yes_no("Include lowercase letters? (y/n): ")
    include_digits = ask_yes_no("Include digits? (y/n): ")
    include_special = ask_yes_no("Include special characters? (y/n): ")


    # Define character sets based on user input
    characters = '' 
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    # Ensure at least one character type is selected
    if not characters:
        print("You must select at least one character type.")
        exit(1)

    # Guarantee that at least one character is used from each selected type
    password_chars = []
    if include_uppercase:
        password_chars.append(random.choice(string.ascii_uppercase))
    if include_lowercase:
        password_chars.append(random.choice(string.ascii_lowercase))
    if include_digits:
        password_chars.append(random.choice(string.digits))
    if include_special:
        password_chars.append(random.choice(string.punctuation))

    # Ensure the password has at least one character from each selected type
    if len(password_chars) > length:
        print("The number of selected character types exceeds the desired password length.")
        exit(1)

    # Fill the rest of the password length with random characters from the selected set
    while len(password_chars) < length:
        password_chars.append(random.choice(characters))

    # Shuffle the password characters to ensure randomness
    random.shuffle(password_chars)
    
    # Generate password
    password = ''.join(password_chars)

    # Print the generated password
    print(f"Generated Password: {password}")

# Standard entry point
if __name__ == "__main__":
    while True:
        main()
        again = ask_yes_no("Generate another password? (y/n): ")
        if not again:
            print("Goodbye!")
            break