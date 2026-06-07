print("Hello!, welcome to a game, you choose a rock, paper or scissors!")

user_choice = input("Please enter your choice (rock, paper, scissors): ").lower()
import random

choices = ["rock", "paper", "scissors"]
bot_choice = random.choice(choices)
print(f"The bot chose: {bot_choice}")

if user_choice == bot_choice:
    print("It's a tie!")
elif (user_choice == "rock" and bot_choice == "scissors") or \
     (user_choice == "paper" and bot_choice == "rock") or \
     (user_choice == "scissors" and bot_choice == "paper"):
    print("Congratulations! You win!")
else:    print("Sorry, you lose. Better luck next time!")
 