import random
import time

total_points = 0
total_moves = 0

player1_history = []

points = 0


def roll():
    pass


def score_calculation(value):
    global points

    if value <= 1:
        points = 0
        return points

    else:
        points = points + value
        return points


while True:
    players = input("Enter the number of player (2-4): ")

    if players.isdigit():

        players = int(players)

        if 2 <= players <= 4:
            break
        else:
            print("try again! atleast (2-4) ")

    else:
        print("Invalid, try again! ")

max_score = 50
player_scores = [0 for _ in range(players)]


while max(player_scores) < max_score:

    for idx in range(players):
        print(f"players {idx} turn started")
        print(f"your initial score is {player_scores[idx]} ")

        current_score = 0

        while True:

            user_input = input("Enter 'r' to roll dice | 's' to stop : ").lower()

            dice = random.randrange(1, 6)

            try:
                if user_input == "s":
                    total_points = total_points + current_score

                    print("your total_points: ", total_points)
                    print("your moves :", total_moves)
                    print("History: ", player1_history)
                    break

                if user_input == "r":
                    total_moves += 1

                    print("rolling...")
                    time.sleep(2)
                    print("you got number: ", dice)

                    points = score_calculation(dice)

                    player1_history.append(dice)

                    print("your current points:", points)
                    print("your moves :", total_moves)

            except ValueError:
                print("Invalid keyword.")
