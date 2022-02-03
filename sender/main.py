import curses
from curses import wrapper

from src.color import Color
from src.menus.main_menu import MainMenu, ACTION_EXIT


def main(stdscr):
    curses.noecho()
    curses.curs_set(0)

    color = Color()
    menu = MainMenu(stdscr, color)

    menu.set_handler(ACTION_EXIT, lambda: exit())

    menu.start()


wrapper(main)
