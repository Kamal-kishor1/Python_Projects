import json
import time
import random


def main_menu():
    print("Welcome to the quiz!")
    while True:
        user_input = input(
            "Press 'a' - Add question 'p' - Play quiz 'q' - Exit : "
        ).lower()
        if user_input == "p":
            print("\nQuiz Started\n")
            start_game()
        elif user_input == "a":
            print("\nCreate Questions for Quiz Bank.\n")
            create_question()
        elif user_input == "q":
            print("\nExit Successfully")
            break
        else:
            print("Invalid operation! Please select a valid option.")


def create_question():
    options = []
    question = input("Add the question: ")
    while True:
        add_option = input("Continue add option (c) or quit (q): ").lower()
        if add_option == "c":
            option = input("Add the option: ")
            options.append(option)
        elif add_option == "q":
            print("Successfully saved options")
            break
        else:
            print("Invalid choice! Try again.")

    answer = input("Correct answer: ")
    new_question = {"question": question, "options": options, "answer": answer}
    save_question([new_question])
    print("Question added successfully!\n")


def save_question(new_question):
    try:
        with open("Quiz_bank.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"questions": []}

    data["questions"].extend(new_question)

    with open("Quiz_bank.json", "w") as f:
        json.dump(data, f, indent=4)


def load_question():
    with open("Quiz_bank.json", "r") as f:
        return json.load(f)["questions"]


def get_random_question(questions, num_questions):
    if num_questions > len(questions):
        num_questions = len(questions)
    return random.sample(questions, num_questions)


def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(str(i + 1) + ".", option)

    try:
        number = int(input("Enter the answer number: "))
    except ValueError:
        print("Invalid input, defaulting to wrong answer.")
        return False

    if number < 1 or number > len(question["options"]):
        print("Invalid choice, defaulting to wrong answer.")
        return False

    return question["options"][number - 1] == question["answer"]


def start_game():
    while True:
        try:
            total_questions = int(input("Enter the number of questions: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    correct = 0
    questions = load_question()
    random_question = get_random_question(questions, total_questions)

    start_time = time.time()
    for question in random_question:
        if ask_question(question):
            correct += 1
        print("---------------------------------------\n")

    end_time = time.time() - start_time

    print("Summary")
    print("Total Questions:", total_questions)
    print("Correct Answers:", correct)
    print("Score:", str(round((correct / total_questions) * 100, 2)) + "%")
    print(f"Total time taken: {round(end_time, 2)} seconds")

    # Replay option
    replay = input("Do you want to play again? (y/n): ").lower()
    if replay == "y":
        start_game()


main_menu()

# Improvements needs to perform
# learboard and save the user data
