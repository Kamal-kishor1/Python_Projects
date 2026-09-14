import random

print("Game of quessing the random number..")
end_number = input("Enter a end number: ")


if end_number.isdigit():
    end_number = int(end_number)

    if end_number <= 0:
        print("Next time provide the number greater than 0.")
        quit()

else:
    print("Next time provide the number instead of character.")
    quit()

ran_number = random.randint(0, end_number)
# print(ran_number)

counter = 0

while True:
    counter += 1

    guessed_number = input("Guess which number could be generated: ")

    if guessed_number.isdigit():
        guessed_number = int(guessed_number)

    else:
        print("Next time provide the number instead of character.")
        continue

    if guessed_number == ran_number:
        print(f"correct guess! random number : {ran_number}")
        print(f"Total guesses: {counter}")
        break

    else:
        print(f"incorrect guess! random number : {ran_number}")
