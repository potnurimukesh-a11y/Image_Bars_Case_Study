"""
Image Visualization Project.
"""
from simpleimage import SimpleImage

GREEN = 127
BLUE = 127

CANVAS_WIDTH = 1100
CANVAS_HEIGHT = 200

def main():
    canvas = SimpleImage.blank(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.show()
    # write your code here or you can create your own function and call them
    # remember as i told you, you can pass a list, dict, string, single variable etc as arguments to functions.
    # you can use the above feature to create your program.

    values = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]

    num_values = len(values)
    bar_width = CANVAS_WIDTH // num_values

    for i in range(num_values):
        red = int(values[i] * 255)

        start_x = i * bar_width
        end_x = start_x + bar_width

        for x in range(start_x, end_x):
            for y in range(CANVAS_HEIGHT):
                canvas.set_rgb(x, y, red, GREEN, BLUE)

    canvas.show()

if __name__ == '__main__':
    main()