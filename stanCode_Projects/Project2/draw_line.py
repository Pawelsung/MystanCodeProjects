"""
File: draw_line.py
Name: Paul
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 5
window = GWindow()
is_clicked = False
start_x = 0
start_y = 0
circle = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(event):
    """
    This function is called when the mouse is clicked. It draws a line from
    the point where the mouse button was clicked to the point where it was released.
    Then, remove the starting circle.
    :param event: The mouse event that triggered this function.
    :return: None
    """
    global start_x, start_y, is_clicked, circle  # Declare global variables
    if not is_clicked:  # Check if the mouse is not clicked
        start_x = event.x  # Store the starting x and y
        start_y = event.y
        circle = GOval(SIZE, SIZE,)  # Create a circle
        circle.filled = False
        window.add(circle, start_x, start_y)
        is_clicked = True
    else:
        # If the mouse is released, create a line from the start point to the current click.
        line = GLine(start_x, start_y, event.x, event.y)
        window.add(line)
        window.remove(circle)
        is_clicked = False


if __name__ == "__main__":
    main()
