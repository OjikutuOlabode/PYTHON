import random
import string

def generate_password():
    # Define possible characters
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits  # 0-9
    symbols = string.punctuation  # !@#$%^&*() etc.

    # Ask the user for the length of the password
    while True:
        try:
            length = int(input("Enter the length of the password (minimum 8 characters): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Ask the user for the number of letters in the password
    while True:
        try:
            num_letters = int(input("Enter the number of letters in the password: "))
            if num_letters > length:
                print("The number of letters cannot be more than the total length of the password.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Ask the user for the number of numbers in the password
    while True:
        try:
            num_numbers = int(input("Enter the number of numbers in the password: "))
            if num_letters + num_numbers > length:
                print("The sum of letters and numbers cannot be more than the total length of the password.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Calculate the number of symbols
    num_symbols = length - num_letters - num_numbers

    # Generate random characters
    password_letters = random.choices(letters, k=num_letters)
    password_numbers = random.choices(digits, k=num_numbers)
    password_symbols = random.choices(symbols, k=num_symbols)

    # Combine all characters
    password_list = password_letters + password_numbers + password_symbols

    # Shuffle the combined list to ensure randomness
    random.shuffle(password_list)

    # Convert the list to a string
    password = ''.join(password_list)

    return password

# Generate and print the password
generated_password = generate_password()
print(f"Your generated password is: {generated_password}")


     
