import curses

class Color:
    def __init__(self):
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        self.GREEN_BLACK = curses.color_pair(1)

