import json
import os
import sys
import time


def typewriter(text, speed=0.09):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def email_validation(email):
    if email not in ["@", "@gmail", "@gmail.com", ".", "*@gmail.com"]:
        return print("invalid email")


def add_detail():
    typewriter("Add user details")

    name = input("Username : ")
    time.sleep(1)
    age = input("Age : ")
    time.sleep(1)
    email = input("Email : ")

    if email_validation(email) is False:
        pass

    return {"name": name, "age": age, "email": email}


def delete_detail(people):
    if not people:
        typewriter("No contacts avaliable to delete.")
        return

    display_detail(people)
    while True:
        user_id = input("For deleting user provide the user_id: ")

        try:
            user_id = int(user_id)
            if user_id <= 0 or user_id > len(people):
                print("Invalid user id not found.")
            else:
                break
        except:
            print("invalid number")

        people.pop(user_id - 1)


def search_detail():
    if not people:
        typewriter("No contacts avaliable to search.")
        return

    search_name = input("search user here using name or email: ").lower()
    result = []

    for person in people:
        name = person["name"]
        email = person["email"]
        if search_name in name.lower() or email.lower():
            result.append(person)

    display_detail(people)


def display_detail(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])


def read_json():
    global people
    try:
        with open("contact_details.json", "r") as f:
            people = json.load(f)
    except FileNotFoundError:
        people = []


def save_json():
    with open("contact_details.json", "w") as f:
        json.dump(people, f, indent=3)


people = []

clear_screen()
typewriter("Hi, welcome to Contact Management System.")
typewriter(".........................................", 0.1)
time.sleep(2)

while True:
    clear_screen()
    read_json()
    print()
    print("Contact list size: ", len(people))
    time.sleep(1)
    print()
    print("User Manual: ")
    time.sleep(1)
    typewriter("1. Add | 2. Delete | 3. Search | 4. Display | 5. 'q' for quit |")
    print()
    time.sleep(1)

    event = input("Enter a number to perform: ")

    clear_screen()

    if event == "1":
        add_detail()
        time.sleep(1)
        typewriter("User detail added!")

    elif event == "2":
        delete_detail(people)
        time.sleep(1)
        typewriter("User detail deleted!")

    elif event == "3":
        search_detail(people)
        time.sleep(1)
        typewriter("This is what you args for!")

    elif event == "4":
        display_detail(people)
        time.sleep(1)
        typewriter("Over all details!")

    elif event == "q":
        save_json()
        time.sleep(1)
        typewriter("Your data has been automatically saved!")
        break

    else:
        time.sleep(1)
        typewriter("Invalid keywords!")
