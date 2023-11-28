"""
File: bouncing_ball.py
Name: Paul
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
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
window = GWindow(800, 500, title='bouncing_ball.py')  # Create a new window and a new ball object
ball = GOval(SIZE, SIZE)
ball_drop = 0
is_clicked = False
edg = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True  # Fill the ball with black color and add it to the starting position
    ball.fill_color = 'black'
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(bounce)  # Call the bounce function when the mouse is clicked


def bounce(event):
    """
    This function is called when the mouse is clicked.
    :param : The mouse event that triggered this function.
    :return: None
    """
    # Declare global variables to use and modify them within the function
    global edg, is_clicked, ball_drop, VX, DELAY, GRAVITY, SIZE, REDUCE, START_X, START_Y
    vy = 0.5  # Initial vertical velocity is 0.5
    if not is_clicked and edg < 3:
        # Check if the mouse is clicked and if it bounces out less than 3 times
        is_clicked = True  # Set True while the mouse is clicked
        while True:
            if not ball.x+ball.height >= window.width:
                # Ball keeps moving tile reaches the edge of the window
                ball.move(VX, vy)
                if not ball.y+ball.height >= window.height:
                    # If ball hasn't reached the bottom, increase vertical velocity by the gravity value.
                    vy += GRAVITY
                else:
                    # If the ball has reached the bottom, reverse back with Reduce height.
                    vy = -vy * REDUCE
                pause(DELAY)
            else:
                # If the ball has reached the edge of the window, move it back to the starting position.
                window.add(ball, x=START_X, y=START_Y)
                is_clicked = False  # Set False for waiting for next click.
                edg += 1  # Count touching edge.
                break


if __name__ == "__main__":
    main()
