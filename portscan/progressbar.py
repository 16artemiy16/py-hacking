import sys
import threading

class Progressbar:
    JUMP_LEFT_SEQ = '\u001b[100D'
    max = 100
    current = 0
    bar_len = 25

    def _print_progress(self):
        progress_percent = self.current / self.max * 100
        progress_len = int(self.bar_len * progress_percent / 100)
        progressbar_chars = '=' * progress_len + '-' * (self.bar_len - progress_len)

        print(self.JUMP_LEFT_SEQ, end='')
        print(f'[{progressbar_chars}] {self.current}/{self.max} scanned', end='')

        sys.stdout.flush()

        if progress_percent == 100:
            print('\n')

    def __init__(self, max):
        self.max = max
        self._print_progress()

    def next(self):
        self.current += 1
        self._print_progress()
