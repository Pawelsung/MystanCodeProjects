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

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Set lives to 3


def main():
    graphics = BreakoutGraphics()  # Initialize the graphics
    lives = NUM_LIVES  # Set lives as constant
    while True:  # Start the loop
        if graphics.is_clicked:  # Check if the mouse is clicked
            dx = graphics.get_dx()  # Get horizontal value of the ball to dx
            dy = graphics.get_dy()  # Get vertical value of the ball to dx
            graphics.ball.move(dx, dy)  # Ball moves according to the velocity

            # Check if the ball stays inside the window
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                # IF it hit the left or right corner
                dx *= -1  # The ball bounces reverse
                graphics.set_dx(dx)  # Update the horizontal value to the ball
            if graphics.ball.y <= 0:  # IF it hits the top
                dy *= -1  # The ball bounces reverse
                graphics.set_dy(dy)  # Update the vertical value to the ball
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:  # IF it hits the bottom
                lives -= 1  # Decrease the number of value by -1
                if lives > 0:  # If there are still lives
                    graphics.set_ball_position()  # Reset the ball position
                    graphics.is_clicked = False  # Wait for the mouse clicked to star again
                else:  # If there are no lives
                    graphics.set_ball_position()  # Reset the ball position
                    break  # End the game
                graphics.check_collision()  # Check if the ball collides with bricks and the paddle
            if graphics.bricks_num == 0:  # If there are no bricks
                break  # End the game
            graphics.check_collision()  # Check if the ball collides with bricks and the paddl
        pause(FRAME_RATE)  # Pause the game according to the frame rate


if __name__ == '__main__':
    main()
