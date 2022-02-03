import curses

ACTION_SEND_FILE = 'send_file'
ACTION_RECEIVE_FILE = 'receive_file'
ACTION_EXIT = 'exit'

ACTIONS = [ACTION_SEND_FILE, ACTION_RECEIVE_FILE, ACTION_EXIT]


class MainMenu:
    """
    The number of the hovered menu option.
    The cursor is painted on the corresponding row.
    """
    _cursor_pos = 1

    _select_handler = {
        ACTION_SEND_FILE: lambda: None,
        ACTION_RECEIVE_FILE: lambda: None,
        ACTION_EXIT: lambda: None
    }

    def __init__(self, stdscr, color):
        self.stdscr = stdscr
        self.color = color
        self._print_menu()

    def set_handler(self, action, cb):
        """
        Registers a handler to an action. Only 1 handler can be set per action!
        :param action: 'send_file', 'receive_file' or 'exit'
        :param cb: handler called on item selection
        :raises exception if an incorrect action set
        """
        if action not in ACTIONS:
            raise f'There is no action {action}'
        self._select_handler[action] = cb

    def start(self):
        """Starts the menu - i.e. prints the menu and listen for events to handle."""
        self._print_menu()

        while True:
            key = self.stdscr.getch()

            # Move cursor down
            if key == curses.KEY_DOWN and self._can_cursor_move_bottom:
                self._cursor_pos += 1
            # Move cursor up
            elif key == curses.KEY_UP and self._can_cursor_move_top:
                self._cursor_pos -= 1
            # Number 3 press - exit
            elif key == 51:
                self._handle_select(ACTION_EXIT)
            # Enter press - handle current hovered action
            elif key == 10:
                self._handle_hovered_action()

            self._print_menu()
            self.stdscr.addstr(str(key), self.color.GREEN_BLACK)

    @property
    def _can_cursor_move_bottom(self):
        """False if the cursor can't be moved bottom (as it's already on the last item)"""
        return self._cursor_pos < 3

    @property
    def _can_cursor_move_top(self):
        """False if the cursor can't be moved top (as it's already on the first item)"""
        return self._cursor_pos > 1

    def _handle_select(self, action):
        """Triggers a handler by a given action"""
        if action not in ACTIONS:
            raise f'There is no action {action}'
        self._select_handler[action]()

    def _handle_hovered_action(self):
        """Triggers a handler by the currently hovered menu option"""
        action = ACTIONS[self._cursor_pos - 1]
        self._handle_select(action)

    def _print_menu(self):
        """Prints the menu"""
        self.stdscr.clear()

        self.stdscr.addstr(0, 0, '========= File Sender =========', self.color.GREEN_BLACK)
        self.stdscr.addstr(1, 5, '1. Send a File', self.color.GREEN_BLACK)
        self.stdscr.addstr(2, 5, '2. Receive a File', self.color.GREEN_BLACK)
        self.stdscr.addstr(3, 5, '3. Exit', self.color.GREEN_BLACK)

        self.stdscr.addstr(self._cursor_pos, 0, '-->', self.color.GREEN_BLACK)

        self.stdscr.refresh()
