"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    : param img: old image
    : return : new image
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):

            pixel = new_img.get_pixel(x, y)

            total_red = 0
            total_blur = 0
            total_green = 0
            total_num = 0

            # Judgment is the first row, which determines the upper limit area
            if x == 0:
                r_l = x
            else:
                r_l = x - 1
            # Judgment is the first column, determines the left limit area
            if y == 0:
                c_u = y
            else:
                c_u = y - 1
            # Judgment is the last row, determine the lower limit area
            if x == (img.width - 1):
                r_r = x
            else:
                r_r = x + 1
            # Judgment is the last column, determines the right limit area
            if y == (img.height - 1):
                c_d = y
            else:
                c_d = y + 1

            # RGB values, add up individually
            for r in range(r_l, r_r + 1):
                for c in range(c_u, c_d + 1):
                    total_red += img.get_pixel(r, c).red
                    total_blur += img.get_pixel(r, c).blue
                    total_green += img.get_pixel(r, c).green
                    total_num += 1

            # RGB average value, put it back separately.
            pixel.red = total_red / total_num
            pixel.green = total_green / total_num
            pixel.blue = total_blur / total_num

    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
