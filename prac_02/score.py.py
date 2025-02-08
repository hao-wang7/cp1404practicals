import random

def evaluate_score(score):
    if not (0 <= score <= 100):
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def get_user_score():
    try:
        score = float(input("Enter score: "))
        print(evaluate_score(score))
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

def main():
    get_user_score()
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score} - {evaluate_score(random_score)}")

if __name__ == "__main__":
    main()