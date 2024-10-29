"""
File: bouncing_ball
Name: bouncing_ball
-------------------------
Step 1 : set the mouse click, click and trigger will be open
Step 2 : when it is triggered, the ball will start moving
Step 3 : x will move in equal speed, but y will move in ratio
Step 4 : move 3 times, and it cannot move. set the number to count.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
trigger = True

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global VX, GRAVITY
    global trigger
    num = 0
    vy = 0

    ball = set_a_ball()
    # add a ball, but it cannot move

    onmouseclicked(start)
    # move the ball,when it is clicked. (click and then the trigger will be False)

    while True:
        if not trigger:
            # trigger is False, it moves.
            ball.move(VX, vy)
            # vy should move in ratio, but vx move in same speed.
            vy += GRAVITY

            if ball.y + ball.height >= window.height:
                vy = -vy*REDUCE
                # reduce its power

            if ball.x > window.width:
                num += 1
                ball = set_a_ball()
                # reset a ball

                if num == 3:
                    break
                else:
                    trigger = True
                    vy = 0
                    # reset vy, or it will count from the last move
        pause(DELAY)


def start(event):
    global trigger
    trigger = False


def set_a_ball():
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball.filled = True
    window.add(ball)
    return ball


if __name__ == "__main__":
    main()
