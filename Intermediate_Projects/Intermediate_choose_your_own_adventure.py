import random
import time
import os 
import sys

health = 100
inventories = set(['compass'])
user_choices = []

paths = {
    "open door" : "(sam)small boy from town came to visit you and told you about the quest listed on the market with high price stake",
    "keep sleeping": "you were consumed by darkness which makes you trapped in guilt and eventually died..",
    "brothel": "you got killed at brothel",
    "temple" : "Go in search of elder's to unleash the roadmap of hidden & lost crystal",
    "alpine fields": "after a days to rumbling around fields finally you decide to rest and started searching for food nearby",
    "glaciers" : "climate suddenly changes and heavyrain fall occured",
    "wild forest" : "encountered by the lion",
    "bear cave" : "near the lake a big cave with shivering sound"
}

questions = {
    "question-1" : "what do you want to do?",
    "question-2" : "where do you want to go?",
    "question-3" : "Do you need the equipment for the hunt?",
    "question-4" : "what do you do next?",
    "question-5" : "how you would survive here?",
    "question-6" : "do wanna be savier or ruler?"
}


def typewriter(text, speed = 0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def retry_game(retry):
    clear_screen()
    global health, inventories, user_choices
    health = 100
    inventories = ["compass"]
    user_choices = []
    start_game()

def lion_encounter():
    outcomes = [
        "The lion roars but suddenly flees into the jungle!",
        "The lion attacks fiercely — you lose 50 health.",
        "The lion hesitates, giving you a chance to strike first.",
        "The lion charges harder than expected — you lose 80 health."
    ]
    event = random.choice(outcomes)
    return event


def damage(amount):
    global health
    health -= amount
    print(f"Health now: {health}")


def restore():
    global health 
    health = 100
    print(f"Health now : {health}")


def alpine_story():
    typewriter("suddenly you heard shouting, crying across lake house where thugs captured house owner")
    time.sleep(1)

    typewriter(questions.get('question-4'))
    time.sleep(1)

    choice = input("either save or hunt for your food: (save/hunt)  ")

    if choice not in ['save', 'hunt']:
        typewriter("you haven't found the food died due to low supplies")
        time.sleep(1)
        retry = input("press r to retry.. : ")
        if retry == 'r':
            retry_game(retry)

    else:
        user_choices.append(choice)
        typewriter("you help")
        time.sleep(1)
        damage(50)
        time.sleep(1)
        clear_screen()

    typewriter("after few days resting and owner gave you the old rusting armor for your protection")
    time.sleep(1)
    choice = input("take armor or not? : (armor/not) ")
    if choice == "armor":
        inventories.add('armor')
        user_choices.append(choice)
        restore()
    else:
        typewriter("invalid choice!")
        retry = input("press r to play again..  " )
        if retry == 'r':
            retry_game(retry)


def glaciers_story():
    typewriter(questions.get('question-5'))
    time.sleep(1)
    pass


def final_story():

    clear_screen()
    typewriter(paths.get('bear cave'))
    time.sleep(1)

    choice = input("go to cave or swim accorss the lake.. (inside/ swim) ")
    time.sleep(.5)

    if choice not in ["inside", "swim"]:
        print("Invalid choice,")
        retry = input("press r to play again..  " )
        if retry == 'r':
            retry_game(retry)
    
    elif choice == "swim":
        print("eaten by aligator.. ")
        retry = input("press r to play again.. " )
        if retry == 'r':
            retry_game(retry)
    
    else:
        user_choices.append(choice)
        typewriter("found crystal..")
        typewriter(questions.get("question-6"))
        time.sleep(1)

        typewriter("Next phase comming soon ... ")
        time.sleep(1)

        typewriter(f"Your : {health} , Inventory : {[item for item in inventories]}, Choices made : {user_choices} ")
        time.sleep(1)

        typewriter("You won the battle.")
        retry = input("press r to play again.. " )
        if retry == 'r':
            retry_game(retry)


def fight_story(count):
    global health, inventories, user_choices   # declare globals

    clear_screen()

    if len(count) == 7 and count == 'fffffff':
        typewriter("the instance fight started lion attack shatter your one leg")
        time.sleep(2)
        typewriter(f"You grip your {inventories[-1]} tightly, though your health is only {health}.")
        time.sleep(2)
        
        damage(50)
        if health <= 0:
            typewriter("You succumbed to your wounds... Game Over.")
            retry = input("press r to play again.. ")
            if retry == 'r':
                retry_game(retry)

        choice = input("press x or d to on your survival instinct : ")

        if choice not in ['x', 'd']:
            time.sleep(1)
            typewriter("lion killed you fought well : ")
            retry = input("press r to play again.. ")
            if retry == 'r':
                retry_game(retry)

        else:
            time.sleep(1)
            typewriter("grabed and tear lion mouth with bear hand")
            time.sleep(1)
            typewriter("you survived by burtal fight and lion ran away")
            time.sleep(2)
            final_story()


    elif len(count) == 5 and count == 'fffff': 
        typewriter(f"You grip your {inventories[-1]} tightly, though your health is only {health}.")
        time.sleep(2)

        damage(50)
        if health <= 0:
            typewriter("You succumbed to your wounds... Game Over.")
            retry = input("press r to play again.. ")
            if retry == 'r':
                retry_game(retry)

        choice = input("press x or d to on your survival instinct : ")

        if choice not in ['x', 'd']:
            time.sleep(1)
            typewriter("lion moked you eyes and attacked from behind and killed : ")
            time.sleep(1)
            retry = input("press r to play again.. ")
            if retry == 'r':
                retry_game(retry)

        else:
            time.sleep(2)
            print("you fought well but killed..")
            retry = input("press r to play again.. " )
            if retry == 'r':
                retry_game(retry)

    elif len(count) == 6:
        typewriter(f"You grip your {inventories[-1]} tightly, though your health is only {health}.")
        time.sleep(2)

        damage(30)
        if health <= 0:
            typewriter("You succumbed to your wounds... Game Over.")
            retry = input("press r to play again.. ")
            if retry == 'r':
                retry_game(retry)

        choice = input("press x or d to on your survival instinct : ")

        if choice not in ['x', 'd']:
            time.sleep(1)
            typewriter("lion tear your both hands and got killed : ")
            time.sleep(1)
            retry = input("press r to play again.. ")
            if retry == 'r':
                retry_game(retry)

        time.sleep(2)
        print("you managed to but dead by wound.. ")
        retry = input("press r to play again.. " )
        if retry == 'r':
            retry_game(retry)

    else:
        time.sleep(2)
        print("you were killed by the lion. ")
        retry = input("press r to play again.. " )
        if retry == 'r':
            retry_game(retry)  
    

def game_logs():
    clear_screen()
    print("Game is start loading...")
    typewriter("........................", 0.8)
    time.sleep(2)
    clear_screen()


def start_game():
    typewriter("Welcome to the adventure game.")
    time.sleep(2)
    clear_screen()

    typewriter("Title: The Lost Crystal of Nytheria")
    print("\n")
    time.sleep(2)
    typewriter("Premise : ")
    print("\n")
    time.sleep(2)
    typewriter("You are a young adventurer in a mystical land where darkness is spreading. Legends say that the Crystal of Nytheria can restore balance, but it has been stolen and hidden deep within dangerous lands.")
    time.sleep(2)
    clear_screen()


def story_1(user_name):
    typewriter(f"{user_name} wakes up in a small village: ")
    time.sleep(1)

    typewriter("Sudden sound of knowking heard and you opend door ")
    time.sleep(2)
    clear_screen()

    typewriter(questions.get('question-1'))
    time.sleep(1)

    choice = input("Open Door or Keep Sleeping: ").strip().lower()
    time.sleep(1)

    typewriter(paths.get(choice, "invalid choice"))
    time.sleep(2)
    user_choices.append(choice)
    clear_screen()

    typewriter(questions.get('question-2'))
    time.sleep(1)

    choice = input("Brothel or Temple: ").strip().lower()
    time.sleep(1)

    typewriter(paths.get(choice, "invalid choice"))
    time.sleep(1)
    user_choices.append(choice)

    print(f"Your health : {health}, inventories : {inventories}")
    time.sleep(2)
    clear_screen()


def story_2():
    typewriter("elder told the path has many obstacles in order to save yourself take some weapons with you")
    time.sleep(1)

    typewriter(questions.get('question-3'))
    time.sleep(1)

    choice = input(" sword or axe or bow-arrow: ").strip().lower()
    time.sleep(2)

    user_choices.append(choice)
    if choice == "sword" or choice == "axe" or choice == "bow-arrow":
        inventories.add(choice)
    else:
        typewriter("elder insist to you take axe")
        time.sleep(2)
        inventories.add("axe")

    clear_screen()


def story_3():
    typewriter("you packed and headed towards concurring the crystal")
    time.sleep(1)

    typewriter("Choose the path? ")
    time.sleep(1)

    choice = input("Alpine Fields or Glaciers: ")
    time.sleep(1)
    user_choices.append(choice)

    typewriter(paths.get(choice, "invalid choice"))
    time.sleep(1)

    if choice == "alpine fields":
        clear_screen()
        alpine_story()
    else:
        clear_screen()
        glaciers_story()

    time.sleep(2)
    clear_screen()



def story_4():
    typewriter("after days of travel you reached to wild forest")
    time.sleep(1)

    typewriter(paths.get('wild forest'))
    user_choices.append('wild forest')
    time.sleep(1)
       
    typewriter("protect yourself take your weapon in hand")
    time.sleep(1)

    choice = input("press d to hold your axe or s to hold sword : ")
    time.sleep(1)

    if choice not in ["d", "s"]:
        if choice == 's':
            health += 50 
        else:
            health += 10

        typewriter("You loss your weapon behind so ran")
        time.sleep(1)
        typewriter("but chased and killed by lion..")
        time.sleep(1)
        retry = input("press r to play again.. " )
        if retry == "r":
            retry_game(retry)

    else:
        user_choices.append(choice)
        encounter = lion_encounter()

        if  "charges harder" in encounter:
            typewriter(f"{encounter}")
            time.sleep(1)
            ("hold your will to fight")
            time.sleep(1)
            count = input("press f seven times to kill... ").lower()
            time.sleep(1)
            damage(65)
            fight_story(count)

        elif "attacks fiercely" in encounter:
            damage(40)
            typewriter(f"{encounter}")
            time.sleep(1)
            typewriter("hold your will to fight")
            time.sleep(1)

            count = input("press f seven times to kill... ").lower()
            time.sleep(1)
            clear_screen()
            fight_story(count)

        else:
            time.sleep(2)
            typewriter(f"\n {encounter} but sees your weapon and ran")
            time.sleep(2)
            final_story()

    # else:
    #     time.sleep(.5)
    #     print("after you were attacked by lion and died..")
    #     retry = input("press r to play again.. " )
    #     if retry == "r":
    #         retry_game(retry)


while True:
    game_logs()
    clear_screen()
    user_name = input("Enter your name: ")
    time.sleep(2)
    clear_screen()
    start_game()
    story_1(user_name)
    story_2()
    story_3()
    story_4()
    again = input("Play again? (y/n) : " ).lower()
    if again != "y":
        print("Thanks for playing!")
        break
