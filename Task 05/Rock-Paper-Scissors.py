import random
def play_rock_paper_scissors():
  user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
  if user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice. Please try again.")
    return
  computer_choice = random.choice(["rock", "paper", "scissors"])
  if user_choice == computer_choice:
    print("It's a tie!")
  elif user_choice == "rock":
    if computer_choice == "scissors":
      print("You win! Rock smashes scissors.")
    else:
      print("You lose! Paper covers rock.")
  elif user_choice == "paper":
    if computer_choice == "rock":
      print("You win! Paper covers rock.")
    else:
      print("You lose! Scissors cuts paper.")
  elif user_choice == "scissors":
    if computer_choice == "paper":
      print("You win! Scissors cuts paper.")
    else:
      print("You lose! Rock smashes scissors.")
play_rock_paper_scissors()
