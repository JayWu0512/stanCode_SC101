"""
File: sierpinski.py
Name: Jay
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
# from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO: repeat this code and draw multiple triangle
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: times to draw a triangle
	:param length: the length of one side of a triangle
	:param upper_left_x: left-up side of a triangle (where to start to draw a triangle)
	:param upper_left_y: left-up side of a triangle (where to start to draw a triangle)
	:return: triangles on the canvas
	"""
	# the most bottom side(x and y) of a triangle
	below_x = upper_left_x + length*0.5
	below_y = upper_left_y + length*0.866
	# the right-up side(x and y) of a triangle
	upper_right_x = upper_left_x + length
	upper_right_y = upper_left_y

	# stop when it comes to 0
	if order == 0:
		pass
	else:
		# draw every side of a triangle
		left_line = GLine(upper_left_x, upper_left_y, below_x, below_y)
		right_line = GLine(below_x, below_y, upper_right_x, upper_right_y)
		up_line = GLine(upper_right_x, upper_right_y, upper_left_x, upper_left_y)

		# add it on the window
		window.add(left_line)
		window.add(right_line)
		window.add(up_line)

		# new left-up x and y
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)
		# new right-up x and y
		sierpinski_triangle(order-1, length/2, upper_left_x+length/2, upper_left_y)
		# new bottom x and y
		sierpinski_triangle(order-1, length/2, upper_left_x+length/2*0.5, upper_left_y+length/2*0.866)


if __name__ == '__main__':
	main()
