"""
File: draw_line
Name: draw_line
-------------------------
Step 1: set mouseclick on main
Step 2: set start point, if it doesn't have start point on window, then draw a pen stroke.
Step 3: set end point
Step 4: remove the pen stroke on start point first
Step 5: add the line
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 5
window = GWindow()
start_point = None
end_point = None
x = 0
y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    global start_point, end_point
    onmouseclicked(click)


def click(event):
    global start_point, end_point, x, y

    pen_stroke = GOval(SIZE, SIZE)
    pen_stroke.filled = True
    pen_stroke.fill_color = 'white'
    # draw a white ball

    if start_point is None:
        start_point = (event.x, event.y)
        x = event.x
        y = event.y
        # put x and y to global variables, so the end point can detect start point place
        window.add(pen_stroke, x=x - SIZE / 2, y=y - SIZE / 2)

    elif end_point is None:
        pen_stroke = window.get_object_at(x, y)
        window.remove(pen_stroke)
        # remove the pen stroke on start point first
        # if we put the code under Gline, python will remove the line and pen stroke

        line = GLine(x, y, event.x, event.y)
        window.add(line)
        # draw a line
        start_point = None
        end_point = None
        # reset start point and end point


if __name__ == "__main__":
    main()
