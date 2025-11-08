import os
import select
import sys
import termios
import tty

import pygame


class TerminalManager:
    # This class does all the messy work around setting up key handling, initializating the display settings, etc
    def __init__(self):
        os.environ["SDL_VIDEODRIVER"] = "dummy"
        pygame.init()
        pygame.display.set_mode((1, 1))

        self._fd = sys.stdin.fileno()
        self._old_settings = termios.tcgetattr(self._fd)
        tty.setcbreak(self._fd)

    def is_escape_pressed(self):
        dr, dw, de = select.select([sys.stdin], [], [], 0)
        if dr:
            ch = sys.stdin.read(1)
            return ch == '\x1b'  # Escape key
        return False

    def close(self):
        termios.tcsetattr(self._fd, termios.TCSADRAIN, self._old_settings)
