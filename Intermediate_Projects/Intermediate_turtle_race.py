from re import I
import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "blue", "orange", "yellow", "brown", "cyan", "pink", "black"]


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)

        else:
            print("Input is not numeric... Try again")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10. Try Again")


# try to do bias where co-ordinates are (0,0) for more realistic
def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(
                1, 20
            )  # we can also see the bias 1 position more chance to win rather than others
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]  # or you can use enumerate


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        # set position
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")


racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color: ", winner)
time.sleep(5)


# racer = turtle.Turtle()
# racer.speed(3)
# racer.penup()          # no line appear as goes up and pendown()
# racer.shape('turtle')  # circle, arrow, turtle and other
# racer.color('green')   # color of turtle
# racer.forward(100)
# racer.left(90)
# racer.forward(100)
# racer.right(90)
# racer.backward(100)
# time.sleep(20)
