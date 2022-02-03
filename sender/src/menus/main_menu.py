import curses

ACTION_SEND_FILE = 'send_file'
ACTION_RECEIVE_FILE = 'receive_file'
ACTION_EXIT = 'exit'

ACTIONS = [ACTION_SEND_FILE, ACTION_RECEIVE_FILE, ACTION_EXIT]


class MainMenu:
    stdscr = None
    cursor_pos = 1

    _select_handler = {
        ACTION_SEND_FILE: lambda: None,
        ACTION_RECEIVE_FILE: lambda: None,
        ACTION_EXIT: lambda: None
    }

    def __init__(self, stdscr, color):
        self.stdscr = stdscr
        self.color = color
        self.print_menu()

    @property
    def can_cursor_move_bottom(self):
        return self.cursor_pos < 3

    @property
    def can_cursor_move_top(self):
        return self.cursor_pos > 1

    def set_handler(self, action, cb):
        if action not in ACTIONS:
            raise f'There is no action {action}'
        self._select_handler[action] = cb

    def _handle_select(self, action):
        if action not in ACTIONS:
            raise f'There is no action {action}'
        self._select_handler[action]()

    def _handle_cursor_action(self):
        action = ACTIONS[self.cursor_pos]
        self._handle_select(action)

    def set_handler_send_file(self, cb):
        self._select_handler['send_file'] = cb

    def start(self):
        self.print_menu()

        while True:
            key = self.stdscr.getkey()

            if key == 'KEY_DOWN' and self.can_cursor_move_bottom:
                self.cursor_pos += 1
            elif key == 'KEY_UP' and self.can_cursor_move_top:
                self.cursor_pos -= 1
            elif key == '3':
                self._handle_select(ACTION_EXIT)

            self.print_menu()
            self.stdscr.refresh()

    def print_menu(self):
        self.stdscr.clear()

        self.stdscr.addstr(0, 0, '========= File Sender =========', self.color.GREEN_BLACK)
        self.stdscr.addstr(1, 5, '1. Send a File', self.color.GREEN_BLACK)
        self.stdscr.addstr(2, 5, '2. Receive a File', self.color.GREEN_BLACK)
        self.stdscr.addstr(3, 5, '3. Exit', self.color.GREEN_BLACK)

        self.stdscr.addstr(self.cursor_pos, 0, '-->', self.color.GREEN_BLACK)

        self.stdscr.refresh()
