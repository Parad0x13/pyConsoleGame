#! /usr/bin/python3

import os
import time
import ctypes
import shutil

class _CursorInfo(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int), ("visible", ctypes.c_byte)]

class _Coord(ctypes.Structure):
    _fields_ = [("x", ctypes.c_short), ("y", ctypes.c_short)]

class _CharsWritten(ctypes.Structure):
    _fields_ = [("val", ctypes.c_longdouble)]

class Console:
    def __init__(self, cursor_visible: bool = False) -> None:
        self.set_cursor_visibility(cursor_visible)

    def __del__(self) -> None:
        self.set_cursor_visibility(True)

    def set_cursor_visibility(self, visible):
        if os.name == "nt":
            __console_handle = ctypes.windll.kernel32.GetStdHandle(-11)    # STD_OUTPUT_HANDLE
            ci = _CursorInfo()
            ctypes.windll.kernel32.GetConsoleCursorInfo(__console_handle, ctypes.byref(ci))
            ci.visible = visible
            ctypes.windll.kernel32.SetConsoleCursorInfo(__console_handle, ctypes.byref(ci))
        else:
            print("\x1b[?25h" if visible else "\x1b[?25l")

    def set_cursor_position(self, x: int, y: int) -> None:
        if os.name == "nt":
            value = x + (y << 16)
            __console_handle = ctypes.windll.kernel32.GetStdHandle(-11)    # STD_OUTPUT_HANDLE
            ctypes.windll.kernel32.SetConsoleCursorPosition(__console_handle, value)
        else:
            print(end="\033[{};{}f".format(y, x))

    def clear_screen(self) -> None:
        if os.name == "nt":
            STD_OUTPUT_HANDLE = -11
            handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
            columns, rows = shutil.get_terminal_size()

            self.set_cursor_position(0, 0)    # [TODO] Not sure how to do this better, should I flush the screen instead?

            c = _Coord()
            c.x = 0
            c.y = 0
            r = _CharsWritten()

            ctypes.windll.kernel32.FillConsoleOutputCharacterA(handle, ord(" "), columns * rows, c, ctypes.byref(r))
        else:
            print("\x1b[2J\x1b[H")

console = Console()
console.clear_screen()
time.sleep(1.0)
