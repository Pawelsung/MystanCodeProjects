"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This is a classic Breakout game that the player needs to control
the paddle with the mouse, making the ball bounce and hit the bricks.
This Game stared when mouse click, the ball moves in a random direction on the screen.
When the ball hits a brick, the brick disappears and the ball bounces back.
If the ball hits the bottom of the window, the player loses one life till there are none.
Then then game ends.
If all the bricks are removed, the player wins and the game ends too.

Enjoy!
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 14        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle

        self.paddle = GRect(width=paddle_width, height=paddle_height)  # Create a paddle
        self.paddle.x = (self.window.width - paddle_width) / 2  # Set the centered horizontal position
        self.paddle.y = self.window.height - paddle_offset  # Offset the position from the bottom
        self.paddle.filled = True  # Fill the default color
        self.window.add(self.paddle)  # Add paddle to the window

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2,)
        self.ball.filled = True  # Fill the default color
        self.set_ball_position()  # Set the initial centered position of the ball
        self.window.add(self.ball)  # Add ball to the window

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.is_clicked = False  # Initialize the mouse click status to False (not clicked)

        # Initialize our mouse listeners
        onmouseclicked(self.ball_run)  # Add a mouse click listener that starts the ball run
        onmousemoved(self.move_paddle)  # Add a mouse move listener that moves the paddle

        # Draw bricks
        self.bricks_num = BRICK_COLS * BRICK_ROWS  # Set total number of bricks
        self.draw_bricks(brick_width, brick_height, brick_rows, brick_cols, brick_offset, brick_spacing)

    def set_ball_position(self):
        self.ball.x = (self.window.width-self.ball.width)/2  # Center the ball horizontally
        self.ball.y = (self.window.height-self.ball.height)/2  # Center the ball vertically

    def draw_bricks(self, width, height, rows, cols, offset, spacing):
        for i in range(rows):  # For each row of bricks
            for j in range(cols):  # For each column of bricks
                brick = GRect(width, height)  # Create a brick as given values
                brick.x = (width+spacing) * j  # Space bricks vertically with given values
                brick.y = (height+spacing) * i + offset
                # Space bricks horizontally with given values according to the offset
                brick.filled = True
                if i < rows // 5:
                    brick.fill_color = "red"
                elif i < 2 * rows // 5:
                    brick.fill_color = "orange"
                elif i < 3 * rows // 5:
                    brick.fill_color = "yellow"
                elif i < 4 * rows // 5:
                    brick.fill_color = "green"
                else:
                    brick.fill_color = "blue"
                self.window.add(brick)

    def move_paddle(self, mouse):  # Ensure the paddle stays within the window
        if mouse.x < self.paddle.width / 2:  # If the mouse moves outside of left edge
            self.paddle.x = 0  # Constrain the paddle to move only to the edge of left side of window
        elif mouse.x > self.window.width - self.paddle.width / 2:  # If the mouse moves outside of right edge
            self.paddle.x = self.window.width - self.paddle.width
            # Constrain the paddle to move only to the right edge of window
        else:  # If the mouse stays in the horizontal range
            self.paddle.x = mouse.x - self.paddle.width / 2  # Center the paddle to the mouse

    def ball_run(self, event):
        if not self.is_clicked:  # If the mouse has not been clicked yet
            self.is_clicked = True  # Update the mouse click status to True (clicked)
            self.__dx = random.randint(1, MAX_X_SPEED)  # Set a random horizontal velocity for the ball
            self.__dy = INITIAL_Y_SPEED  # Set the initial vertical velocity for the ball

    def get_dx(self):
        return self.__dx  # Return the current horizontal velocity of the ball

    def get_dy(self):
        return self.__dy  # Return the current vertical velocity of the ball

    def set_dx(self, dx):
        self.__dx = dx  # Update the horizontal velocity of the ball

    def set_dy(self, dy):
        self.__dy = dy  # Update the vertical velocity of the ball

    def check_collision(self):
        r = self.ball.width / 2  # Set the radius of the ball.

        # Check upper left corner
        obj = self.window.get_object_at(self.ball.x, self.ball.y)
        # Get the object at the upper left corner of the ball
        if obj is not None:  # If there is an object
            self.collied(obj)  # Call function collied
            return

        # Check upper right corner
        obj = self.window.get_object_at(self.ball.x + r * 2, self.ball.y)
        # Get the object at the upper right corner of the ball
        if obj is not None:
            self.collied(obj)
            return

        # Check down left corner
        obj = self.window.get_object_at(self.ball.x, self.ball.y + r * 2)
        # Get the object at the down left corner of the ball
        if obj is not None:
            self.collied(obj)
            return

        # Check down right corner
        obj = self.window.get_object_at(self.ball.x + r * 2, self.ball.y + r * 2)
        # Get the object at the down right corner of the ball
        if obj is not None:
            self.collied(obj)
            return

    def collied(self, obj):
        if obj == self.paddle:  # Move reverse while touching paddle
            self.__dy *= -1  # Reverse the vertical direction
            self.ball.y = self.paddle.y - self.ball.height  # Move the ball above the paddle
        else:  # move reverse and remove brick.
            self.__dy *= -1  # Reverse the vertical direction
            self.bricks_num -= 1  # Decrease the number of bricks by 1
            self.window.remove(obj)  # Remove the brick from the window
