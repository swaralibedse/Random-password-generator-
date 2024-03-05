import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not any([use_letters, use_numbers, use_symbols]):
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_valid_input(prompt, type_):

    while True:
        try:
            value = type_(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid value.")

def main():
    print("Welcome to the Password Generator!")

    length = get_valid_input("Enter the length of the password: ", int)
    use_letters = get_valid_input("Include letters? (y/n): ", lambda x: x.lower() == 'y')
    use_numbers = get_valid_input("Include numbers? (y/n): ", lambda x: x.lower() == 'y')
    use_symbols = get_valid_input("Include symbols? (y/n): ", lambda x: x.lower() == 'y')

    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
