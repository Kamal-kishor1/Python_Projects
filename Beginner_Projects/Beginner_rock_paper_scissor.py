import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or 'q' to Quit : ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    rand_number = random.randint(0, 2)

    computer_pick = options[rand_number]
    print("computer pick:", computer_pick)

    if user_input == "rock" and computer_pick == "scissor":
        print("user wins")
        user_wins += 1

    elif user_input == "scissor" and computer_pick == "paper":
        print("user wins")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("user wins")
        user_wins += 1

    else:
        print("you lost!")
        computer_wins += 1

print("user wins : ", user_wins)
print("computer wins : ", computer_wins)
