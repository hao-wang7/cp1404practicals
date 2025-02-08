def get_password(min_length):
    """Function to get a password with minimum length."""
    while True:
        password = input(f"Enter a password (minimum {min_length} characters): ")
        if len(password) >= min_length:
            return password
        print(f"Error: Password must be at least {min_length} characters long.")

def print_asterisks(password):
    """Function to print asterisks equivalent to the password length."""
    print('*' * len(password))

def main():
    """Main function to run the password validation process."""
    min_length = 8
    password = get_password(min_length)
    print_asterisks(password)

# Call the main function
main()
