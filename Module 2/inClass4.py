import random

def main():
    # User input & validation
    user_choice = input("Choose Rock, Paper, or Scissors: ")

    # Sanitizing user input into UPPER CASE
    user_choice = user_choice.upper()

    if user_choice != "ROCK" and user_choice != "PAPER" and user_choice != "SCISSORS":
        print("Invalid choice")
    else:
        # Computer choice
        option = ["ROCK", "PAPER", "SCISSORS"]
        comp_choice = random.choice(option)
        print(comp_choice)

        # Game Logic
        # WIN
        if user_choice == "ROCK" and comp_choice == "SCISSORS":
            print("WIN")
        elif user_choice == "PAPER" and comp_choice == "ROCK":
            print("WIN")
        elif user_choice == "SCISSORS" and comp_choice == "PAPER":
            print("WIN")
        # DRAW
        elif user_choice == comp_choice:
            print("DRAW")
        # LOST
        else:
            print("LOST")


if __name__ == "__main__":
    main()