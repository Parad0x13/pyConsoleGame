#! /usr/bin/python3

import curses
import time

def main(stdscr):
    x = 20
    y = 10
    xVel = 0
    yVel = 0

    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    stdscr.nodelay(1)    # getch non-blocking

    height, width = stdscr.getmaxyx()
    render_buffer = [[' '] * width for _ in range(height)]

    frameCount = 0
    startTime = time.time()

    while True:
        stdscr.refresh()

        #render_buffer[y][x] = "☻"
        render_buffer[int(y)][int(x)] = "☻"

        # Game screen
        stdscr.move(0, 0)    # I HAVE to do this because curses acts a fool when you try to do anything with its coordinate system...
        for i in range(height):
            for j in range(width):
                # I HAVE to do it this way because curses is effed up and won't let you draw on the bottom right of the screen
                # This is because addch/addstr automatically tries to 'wrap' at the edge of the screen
                # If GOD FORBID you are on the last possible VALID place to draw it will crash... This 'fixes' it
                try: stdscr.addch(render_buffer[i][j])
                except: pass

        # FPS
        frameCount += 1
        elapsedTime = time.time() - startTime
        fps = frameCount / elapsedTime
        stdscr.addstr(0, 0, "FPS: {:.2f}, ({}, {}) of ({}, {})".format(fps, x, y, width, height))
        frameCount = 0
        startTime = time.time()

        key = stdscr.getch()

        if key == 27:    # (ESC)
            break
        if key == ord("w"):
            #y = max(y - 1, 0)
            yVel -= 1.0
        if key == ord("s"):
            #y = min(y + 1, height - 1)
            yVel += 1.0
        if key == ord("a"):
            xVel -= 1.0
            #x = max(x - 1, 0)
        if key == ord("d"):
            xVel += 1.0
            #x = min(x + 1, width - 1)

        #x += xVel
        #if x < 0.0 or x == 0.0: xVel *= 0.90

        x += xVel
        xVel *= 0.975
        if x < 0:
            x = 0
            xVel *= -0.75
        if x > width - 1:
            x = width - 1
            xVel *= -0.75

        y += yVel
        yVel *= 0.975
        if y < 0:
            y = 0
            yVel *= -0.75
        if y > height - 1:
            y = height -1
            yVel *= -0.75

        #if abs(x - int(x)) < 0.05: x = int(x)    # Why doesn't this work for both directions?

        render_buffer = [[' '] * width for _ in range(height)]

        time.sleep(1.0 / 60.0)

    curses.endwin()

if __name__ == "__main__":
    curses.wrapper(main)
