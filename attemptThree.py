import ctypes

def write_text_at_position(x, y, text):
    try:
        handle = ctypes.windll.kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
        if handle == -1:
            raise ValueError("Failed to get console handle")

        pos = (y << 16) | x
        ctypes.windll.kernel32.SetConsoleCursorPosition(handle, pos)

        result = ctypes.windll.kernel32.WriteConsoleOutputCharacterW(handle, text, len(text), None, None)
        if result == 0:
            raise ValueError("Failed to write to console")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
write_text_at_position(5, 5, "Hello, World!")
