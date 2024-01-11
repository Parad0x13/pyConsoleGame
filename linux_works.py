#! /usr/bin/python3

# Shouldn't need to do this really, the entire screen should be overwritten instead
#def clear_screen(): print("\x1b[2J\x1b[H")

import time
import sys
import os
import shutil

def set_cursor_position(x: int, y: int) -> None:
    print(end="\033[{};{}f".format(y, x))

class Screen:
    def __init__(self) -> None:
        self.data = None

#set_cursor_position(0, 0)
#print("X")
#time.sleep(1)

columns, rows = shutil.get_terminal_size()
size = columns * rows
for l in "ABCD":
    set_cursor_position(0, 0)
    sys.stdout.write(l*size)
    sys.stdout.flush()
    time.sleep(0.5)
