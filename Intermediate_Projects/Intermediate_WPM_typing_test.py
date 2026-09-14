import curses  # styling of terminal
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin! ")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        print(correct_char)
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)


def load_text():
    with open("wpm.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)  # do not delay if user doesn't hit key

    # stdscr.clear()
    # stdscr.addstr(target_text)
    # stdscr.refresh()

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        # convert list to string
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()  # it gives error without try and except
        except:
            continue

        if ord(key) == 27:  # ascii represent of keyboard keys
            break  # hit the escape key to exit

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):  # standard screen
    curses.init_pair(
        1, curses.COLOR_GREEN, curses.COLOR_BLACK
    )  # (ID, FOREGROUND, BACKGROUND)
    curses.init_pair(
        2, curses.COLOR_RED, curses.COLOR_BLACK
    )  # (ID, FOREGROUND, BACKGROUND)
    curses.init_pair(
        3, curses.COLOR_RED, curses.COLOR_BLACK
    )  # (ID, FOREGROUND, BACKGROUND)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You copleted the text! Press any key to continue...")
        key = stdscr.getkey()

        if ord(key) == 27:
            break

    # example

    # stdscr.clear()
    # # stdscr.addstr(1, 5, "hello world!", curses.color_pair(1))  # POSITION, TEXT, COLOR
    # stdscr.addstr(1, 5, "hello world!", curses.color_pair(1))  # POSITION, TEXT, COLOR
    # stdscr.refresh()
    # key = stdscr.getkey()  # wait for user to press something then react
    # print(key)


wrapper(main)
