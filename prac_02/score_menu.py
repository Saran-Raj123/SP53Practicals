"""
CP1404 - Practical - Saranraj Saravanan
Score Menu
"""

def determine_result_from_score(score):
    pass

def get_valid_score():
    while True:
        try:
            score = int(input("Enter a valid score (0-100 inclusive): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid input. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def print_result(score):
    result = determine_result_from_score(score)
    print(f"The result is: {result}")

def show_stars(score):
    print("Stars: " + "*" * score)

def main():
    # Get a valid score before entering the menu loop
    score = get_valid_score()

    choice = ""
    while choice.lower() != 'q':
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ")

        if choice.lower() == 'g':
            score = get_valid_score()
        elif choice.lower() == 'p':
            print_result(score)
        elif choice.lower() == 's':
            show_stars(score)
        elif choice.lower() == 'q':
            print("Farewell! Thank you for using the program.")
        else:
            print("Invalid input. Please enter a valid option.")

if __name__ == "__main__":
    main()
