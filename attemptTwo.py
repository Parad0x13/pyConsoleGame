#! /usr/bin/python3

import shutil
import ctypes
import time
import os

def flood_screen(buffer):
    STD_OUTPUT_HANDLE = -11
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    columns, rows = shutil.get_terminal_size()

    # Clear the screen
    #ctypes.windll.kernel32.FillConsoleOutputCharacterW(handle, " ", columns * rows, 0)
    #text = text.encode("utf-8")
    #ctypes.windll.kernel32.FillConsoleOutputCharacterW(handle, text, len(text), 0)

    text = ""
    for row in buffer:
        text += "".join(row)

    set_cursor_position(0, 0)
    ctypes.windll.kernel32.WriteConsoleW(ctypes.windll.kernel32.GetStdHandle(-11), text, len(text), None, None)
    set_cursor_position(0, 0)

    # Reset text attributes
    #ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x07)

def set_cursor_position(x, y):
    STD_OUTPUT_HANDLE = -11
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    pos = (y << 16) | x
    ctypes.windll.kernel32.SetConsoleCursorPosition(handle, pos)

def write_text(x, y, text):
    set_cursor_position(x, y)
    ctypes.windll.kernel32.WriteConsoleW(ctypes.windll.kernel32.GetStdHandle(-11), text, len(text), None, None)

class _CursorInfo(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int), ("visible", ctypes.c_byte)]

def set_cursor_visibility(visible: bool) -> None:
    __console_handle = ctypes.windll.kernel32.GetStdHandle(-11)    # STD_OUTPUT_HANDLE
    ci = _CursorInfo()
    ctypes.windll.kernel32.GetConsoleCursorInfo(__console_handle, ctypes.byref(ci))
    ci.visible = visible
    ctypes.windll.kernel32.SetConsoleCursorInfo(__console_handle, ctypes.byref(ci))

# Example usage
#set_cursor_position(10, 4)
#clear_screen()
#write_text(10, 5, "Hello, World!")
#time.sleep(3)

set_cursor_visibility(False)
columns, rows = shutil.get_terminal_size()
render_buffer = [['.'] * columns for _ in range(rows)]
flood_screen(render_buffer)

x = 10
y = 2
while True:
    render_buffer = [['.'] * columns for _ in range(rows)]
    render_buffer[y][x] = "♥"
    flood_screen(render_buffer)

    x += 1

    time.sleep(1.0 / 30.0)
