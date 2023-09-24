import random

def get_user_choice():
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").strip().capitalize()
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return f"You win! {user_choice} beats {computer_choice}."
    else:
        return f"Computer wins! {computer_choice} beats {user_choice}."

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()








def get_user_choice() :
    while True :
        user_choice = input("Choose Rock, Paper, or Scissors: ").strip().capitalize()
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

def get_computer_choice() :
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_win():
    if user_choice == computer_choice:
        return "It's a tie!"
    elif(
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return f"You win! {user_choice} beats {computer_choice}."
    else:
        return f"Computer wins! {computer_choice} beats {user_choice}."
    
def play_game() :
    print("Welcome to Rock, Paper, Scissors!")
    while True :
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()