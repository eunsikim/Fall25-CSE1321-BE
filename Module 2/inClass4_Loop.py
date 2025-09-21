import random

def main():
    user_score = 0
    comp_score = 0

    anotherGame = "yes"

    # CHALLENGE: Make sure the game stops ONLY when the user enters "no"
    while anotherGame == "yes":
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
                user_score += 1
            elif user_choice == "PAPER" and comp_choice == "ROCK":
                print("WIN")
                user_score += 1
            elif user_choice == "SCISSORS" and comp_choice == "PAPER":
                print("WIN")
                user_score += 1
            # DRAW
            elif user_choice == comp_choice:
                print("DRAW")
            # LOST
            else:
                print("LOST")
                comp_score += 1
            
        print(f"SCORE:\nUSER:{user_score}\nCOMPUTER:{comp_score}")

        anotherGame = input("Do you want to play again (yes/no): ").lower()

        while anotherGame != "yes" and anotherGame != "no":
            print("Please enter yes or no")
            anotherGame = input("Do you want to play again (yes/no): ").lower()


if __name__ == "__main__":
    main()