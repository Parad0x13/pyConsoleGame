#! /usr/bin/python3

# GOT THIS FROM HERE: https://github.com/Matthias1590/ConsoleDraw/tree/main

#print("\033[5;10H\033[31mHello, World!\033[0m")
def draw(x, y, c):
    print("\033[{};{}H\033[31m{}\033[0m".format(x, y, c))

import shutil

def get_terminal_size():
    try:
        # Use shutil to get terminal size on Windows
        columns, rows = shutil.get_terminal_size()

    except Exception as e:
        print("Error: {}".format(e))
        columns, rows = 0, 0

    return rows, columns

#############################
#############################
#############################
#############################

import os
import time
import ctypes

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        print("\x1b[2J\x1b[H")

class _CursorInfo(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int), ("visible", ctypes.c_byte)]

def set_cursor_visibility(visible: bool) -> None:
    if os.name == "nt":
        __console_handle = ctypes.windll.kernel32.GetStdHandle(-11)    # STD_OUTPUT_HANDLE
        ci = _CursorInfo()
        ctypes.windll.kernel32.GetConsoleCursorInfo(__console_handle, ctypes.byref(ci))
        ci.visible = visible
        ctypes.windll.kernel32.SetConsoleCursorInfo(__console_handle, ctypes.byref(ci))
    else:
        print("\x1b[?25h" if visible else "\x1b[?25l")

def set_cursor_position(x: int, y: int) -> None:
    if os.name == "nt":
        value = x + (y << 16)
        __console_handle = ctypes.windll.kernel32.GetStdHandle(-11)    # STD_OUTPUT_HANDLE
        ctypes.windll.kernel32.SetConsoleCursorPosition(__console_handle, value)
    else:
        print(end="\033[{};{}f".format(y, x))

x = 0
y = 0
xDir = 0
yDir = 1
#width, height = get_terminal_size()
size = os.get_terminal_size()
set_cursor_visibility(False)
while True:
    clear_screen()
    set_cursor_position(y, x)
    print("{}, {}".format(size.columns, size.lines))

    x += xDir
    y += yDir

    #if y > height - 1:
    #    y = height - 1
    #    yDir = -1

    time.sleep(1.0 / 30.0)
