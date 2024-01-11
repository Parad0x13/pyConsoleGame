import ctypes
import time
import shutil

def set_cursor_visibility(visible: bool) -> None:
    __console_handle = ctypes.windll.kernel32.GetStdHandle(-11)    # STD_OUTPUT_HANDLE
    ci = _CursorInfo()
    ctypes.windll.kernel32.GetConsoleCursorInfo(__console_handle, ctypes.byref(ci))
    ci.visible = visible
    ctypes.windll.kernel32.SetConsoleCursorInfo(__console_handle, ctypes.byref(ci))

def set_cursor_position(x, y):
    STD_OUTPUT_HANDLE = -11
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    pos = (y << 16) | x
    ctypes.windll.kernel32.SetConsoleCursorPosition(handle, pos)

class _Coord(ctypes.Structure):
    _fields_ = [("x", ctypes.c_short), ("y", ctypes.c_short)]

class _CharsWritten(ctypes.Structure):
    _fields_ = [("val", ctypes.c_longdouble)]

def stuff(char):
    STD_OUTPUT_HANDLE = -11
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    columns, rows = shutil.get_terminal_size()

    c = _Coord()
    c.x = 0
    c.y = 0
    r = _CharsWritten()
    size = columns * rows
    ctypes.windll.kernel32.FillConsoleOutputCharacterA(handle, ord(char), size, c, ctypes.byref(r))

#set_cursor_position(0, 0)

for l in "ABCD":
    stuff(l)
    time.sleep(0.1)
