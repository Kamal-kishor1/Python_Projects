# Actually use inventory and health

# Right now they’re declared but unused. You could append items (inventory.append("sword")) and deduct health (health -= 20) during fights.

# Then check conditions later (e.g., if no sword in inventory → lion fight is harder).



import time
import os 
import sys
import random


health = 100
inventories = ['dagger']
user_choices = []

def clear_screen():
    # only works on window and linuz
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def lion_encounter():
    outcomes = [
        "The lion roars but suddenly flees into the jungle!",
        "The lion attacks fiercely — you lose 50 health.",
        "The lion hesitates, giving you a chance to strike first.",
        "The lion charges harder than expected — you lose 80 health."
    ]

    event = random.choice(outcomes)
    return event


def starting_logs():

    clear_screen()

    print("Game is starting.....")
    time.sleep(3)
    clear_screen()
    starting_point()


def retry_game(press):
    global health, inventories, user_choices
    # Reset state for a new run
    health = 100
    inventories = ['dagger']
    user_choices = []

    clear_screen()
    starting_point()


def game_sequal_1(username):

    clear_screen()

    typewriter(f"{username} wakes up in a small village: ")
    time.sleep(1)

    typewriter("what do you want do? ")
    user_input = input("type: (save village/keep sleeping) ").lower()
    time.sleep(1)

    if user_input not in ["save village", "keep sleeping"]:
        print("Invalid choice,")
        retry = input("press r to play again.. " )
        retry_game(retry)
        
    elif user_input == "keep sleeping":
        typewriter("you were covered with darkness and killed yourself..")
        retry = input("press r to play again.. " )
        retry_game(retry)

    else:
        user_choices.append(user_input)
        typewriter("where do you want to go? ")
        user_input = input("Brothel or Quest : ").lower()
        time.sleep(1)
        game_sequal_2(user_input)       
            


def game_sequal_2(user_choice):

    clear_screen()

    if user_choice not in ["brothel", "quest", "q"]:
        print("Invalid choice, ")
        retry = input("press r to play again.. " )
        retry_game(retry)

    elif user_choice == "quest" or user_choice == 'q':
        user_choices.append(user_choice)
        typewriter("You meet with wise elder...")
        time.sleep(2)
        typewriter("Explain the quest: recover the crytal before the land falls into eternal..")
        time.sleep(1)
        typewriter("hint: go to jungle...")
        time.sleep(1.5)
        user_input = input("Which direction you want to go: (right/left) : ").lower()
        time.sleep(1)
        game_sequal_3(user_input)
             
    else:
        typewriter("You got killed at brothel..")
        retry = input("press r to play again..")
        retry_game(retry)



def game_sequal_3(user_choice):

    clear_screen()

    if user_choice not in ["right", "left"]:
        print("invalid choice, ")
        time.sleep(1)
        retry = input("press r to play again..") 
        retry_game(retry)

    elif user_choice == "right":
        typewriter("wrong! you die retry.. ")
        retry = input("press r to play again.. " )
        retry_game(retry)

    else:
        user_choices.append(user_choice)
        typewriter("reached to the jungle.. ")
        time.sleep(.7)

        typewriter("your eyes shine due to metal blade")
        status = input("pick up the sword or move without it: (pick/leave) : ").lower()
        time.sleep(1)
        user_input = input("where to go?\n over the mountains or lake... (mountain/lake) : ").lower()
        time.sleep(1)
        game_sequal_4(user_input, status)



def game_sequal_4(user_choice, status):
    global health, inventories, user_choices   # declare globals

    clear_screen()
    
    # inventory = inventory.append(weapon)
    # print(inventory.item(0))
    # print("reach to new level")

    if user_choice == "mountain" and status == "pick":
        user_choices.append(status)
        user_choices.append(user_choice)
        inventories.append("sword")

        typewriter('after a few miles over the mountain you encountered by lion')
        time.sleep(1)
        typewriter("protect yourself take your weapon in hand")
        time.sleep(1)

        user_input = input("press d to hold your dagger or s to hold sword : ")
        time.sleep(1)

        if user_input not in ["d", "s"]:
            if user_input == 's':
                health += 50 
            else:
                health += 10

            typewriter("You loss your weapon behind so ran")
            time.sleep(1)
            typewriter("but chased and killed by lion..")
            time.sleep(1)
            retry = input("press r to play again.. " )
            retry_game(retry)

        else:
            user_choices.append(user_input)
            encounter = lion_encounter()

            if  "charges harder" in encounter:
                typewriter(f"{encounter}")
                time.sleep(1)
                typewriter("hold your will to fight")
                time.sleep(1)
                fight_input = input("press f seven times to kill... ").lower()
                time.sleep(1)
                health -= 65
                fight_sequal(fight_input)

            elif "attacks fiercely" in encounter:
                health -= 40
                typewriter(f"{encounter}")
                time.sleep(1)
                typewriter("hold your will to fight")
                time.sleep(1)

                fight_input = input("press f seven times to kill... ").lower()
                time.sleep(1)
                clear_screen()
                fight_sequal(fight_input)

            else:
                time.sleep(2)
                typewriter(f"\n {encounter} but sees your weapon and ran")
                time.sleep(2)
                final_sequal()

    else:
        time.sleep(.5)
        print("after you were attacked by lion and died..")
        retry = input("press r to play again.. " )
        retry_game(retry)



def game_sequal_5(user_choice):

    clear_screen()

    if user_choice not in ["inside", "swim"]:
        print("Invalid choice,")
        retry = input("press r to play again.. " )
        retry_game(retry)
    
    elif user_choice == "swim":
        print("eaten by aligator.. ")
        retry = input("press r to play again.. " )
        retry_game(retry)
    
    else:
        user_choices.append(user_choice)
        typewriter("found crystal..")
        typewriter("save the village and became their savior")
        time.sleep(1)
        typewriter(f"Your : {health} , Inventory : {[item for item in inventories]}, Choices made : {user_choices} ")
        time.sleep(1)
        typewriter("You won the battle.")
        retry = input("press r to play again.. " )
        retry_game(retry)



def fight_sequal(fight):
    global health, inventories, user_choices   # declare globals

    clear_screen()

    if len(fight) == 7 and fight == 'fffffff':
        typewriter("the instance fight started lion attack shatter your one leg")
        time.sleep(2)
        typewriter(f"You grip your {inventories[-1]} tightly, though your health is only {health}.")
        time.sleep(2)
        health -= 50
        if health <= 0:
            typewriter("You succumbed to your wounds... Game Over.")
            retry = input("press r to play again.. ")
            retry_game(retry)

        user_input = input("press x or d to on your survival instinct : ")

        if user_input not in ['x', 'd']:
            time.sleep(1)
            typewriter("lion killed you fought well : ")
            retry = input("press r to play again.. ")
            retry_game(retry)

        else:
            time.sleep(1)
            typewriter("grabed and tear lion mouth with bear hand")
            time.sleep(1)
            typewriter("you survived by burtal fight and lion ran away")
            time.sleep(2)
            final_sequal()


    elif len(fight) == 5 and fight == 'fffff': 
        typewriter(f"You grip your {inventories[-1]} tightly, though your health is only {health}.")
        time.sleep(2)

        health -= 50
        if health <= 0:
            typewriter("You succumbed to your wounds... Game Over.")
            retry = input("press r to play again.. ")
            retry_game(retry)

        user_input = input("press x or d to on your survival instinct : ")

        if user_input not in ['x', 'd']:
            time.sleep(1)
            typewriter("lion moked you eyes and attacked from behind and killed : ")
            time.sleep(1)
            retry = input("press r to play again.. ")
            retry_game(retry)

        else:
            time.sleep(2)
            print("you fought well but killed..")
            retry = input("press r to play again.. " )
            retry_game(retry)


    elif len(fight) == 6:
        typewriter(f"You grip your {inventories[-1]} tightly, though your health is only {health}.")
        time.sleep(2)

        health -= 50
        if health <= 0:
            typewriter("You succumbed to your wounds... Game Over.")
            retry = input("press r to play again.. ")
            retry_game(retry)

        user_input = input("press x or d to on your survival instinct : ")

        if user_input not in ['x', 'd']:
            time.sleep(1)
            typewriter("lion tear your both hands and got killed : ")
            time.sleep(1)
            retry = input("press r to play again.. ")
            retry_game(retry)

        time.sleep(2)
        print("you managed to but dead by wound.. ")
        retry = input("press r to play again.. " )
        retry_game(retry)

    else:
        time.sleep(2)
        print("you were killed by the lion. ")
        retry = input("press r to play again.. " )
        retry_game(retry)   


def final_sequal():

        clear_screen()

        typewriter("you see the cave beside lake")
        new_choice = input("go to cave or swim accorss the lake.. (inside/ swim) ")
        time.sleep(.5)
        game_sequal_5(new_choice)


def starting_point():

    time.sleep(2)

    typewriter("Welcome to the adventure game.")
    time.sleep(2)
    clear_screen()

    typewriter("Title: The Lost Crystal of Nytheria ")
    time.sleep(2)
    print("Premise: ")
    time.sleep(1)

    typewriter("You are a young adventurer in a mystical land where darkness is spreading. Legends say that the Crystal of Nytheria can restore balance, but it has been stolen and hidden deep within dangerous lands.")
    time.sleep(2)

    return game_sequal_1(input("Enter your name: "))


starting_logs()





