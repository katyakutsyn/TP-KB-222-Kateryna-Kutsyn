import random

player_choice = input("Your choice (rock, scissors, paper): ").lower()
computer_choice = random.choice(["rock", "scissors", "paper"])

print(f"You chose: {player_choice}")
print(f"Computer chose: {computer_choice}")


if player_choice == computer_choice:
    print("It's a tie!")
elif (
    (player_choice == "rock" and computer_choice == "scissors") or
    (player_choice == "scissors" and computer_choice == "paper") or
    (player_choice == "paper" and computer_choice == "rock")
):
    print("You win!")
else:
    print("Computer wins!")
