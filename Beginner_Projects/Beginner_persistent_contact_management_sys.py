import json

def add_person():
    name = input("name: ").strip()
    age = input("age: ")
    email = input("email: ")
    return  {"name": name, "age": age, "email": email}
    

def delete_person(people):
    if not people:
        print("No contacts avaliable to delete.")
        return

    display_person(people)
    while True:
        user_id = input("for deleting user provide user-id : ")
        try:
            user_id = int(user_id)
            if user_id <= 0 or user_id > len(people):
                print("invalid user id not found")
            else:
                break
        except: 
            print("Invalid number")

    people.pop(user_id -1)


def search_person(people):
    if not people:
        print("No contacts avaliable to search.")
        return

    username = input("search user here using name: ").lower()
    result = []

    for person in people:
        name = person['name']
        if username in name.lower():
            result.append(person)

    display_person(result)


def display_person(people):
   for i, person in enumerate(people):
   #    print(i+1,'-', person)
        print(i+1,'-', person['name'], "|", person['age'], "|", person['email'])

def read_json():
    global people
    try:
        with open("contact_details.json",'r') as f:
            people = json.load(f)
    except FileNotFoundError:
        people = []


def save_json():
    with open("contact_details.json", 'w') as f:
        json.dump(people, f, indent=2)
    
       
    
people = []



print("Hi, welcome to the Contact Management System.")

while True:
    read_json()
    print()
    print("contact list size: ", len(people))
    print()
    event = input("You can 'add' or 'delete' or 'search' or 'q' for quit : ").strip().lower()

    if event == 'add':
        person = add_person()
        people.append(person)
        print(f"A user with name {person.get('name')} added !")
            
    elif event == "delete":
        delete_person(people)
        print("person has been delisted!")

    elif event == "search":
        search_person(people)

    elif event == "q":
        save_json()
        break
    else:
        print("invaild function!")


