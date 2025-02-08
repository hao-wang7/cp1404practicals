# Function to get a valid score (between 0 and 100 inclusive)
def get_valid_score():
    while True:
        try:
            score = float(input("Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric score.")


# Function to determine the result based on the score
def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


# Function to show stars corresponding to the score
def show_stars(score):
    stars = '*' * int(score)  # Show as many stars as the score (rounded down to an integer)
    print(stars)


# Main function to drive the menu and handle user choices
def main():
    print("Welcome to the Score Program!")

    # Get a valid score at the start
    score = get_valid_score()

    while True:
        # Display the menu
        menu = """Menu:
        (G)et a valid score
        (P)rint result
        (S)how stars
        (Q)uit"""
        print(menu)
        choice = input(">>> ").upper()

        if choice == 'G':
            score = get_valid_score()  # Re-ask for score if option G is selected
        elif choice == 'P':
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice, please choose from the menu.")


# Call the main function to run the program
if __name__ == '__main__':
    main()
