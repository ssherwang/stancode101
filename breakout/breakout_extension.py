"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program aims to create a very classical game, breakout, by Python.
At the beginning, player will have three lives.
When all of bricks disappear, player win the game.

In this extension version, the velocity of ball will increase with score.
When brick remains account for only 20% of total amount,
the score for each collision will change from 1 points to 10 points.

"""

from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add animation loop here!
    while True:
        # pause
        pause(FRAME_RATE)

        # check
        graphics.collision_check()

        # win condition
        if graphics.brick_remain() <= 0:
            graphics.win()
            break

        # when ball leaves the bottom of window, lives will - 1
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            lives -= 1
            graphics.reset_lives_count(1)
            if lives > 0:
                graphics.reset_ball()
            else:
                # game over
                graphics.over()
                break

        # ball move
        graphics.ball.move(graphics.ball_vx(), graphics.ball_vy())

        # check ball position and let it bounce back
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.set_ball_vx(-graphics.ball_vx())
        if graphics.ball.y <= 0:
            graphics.set_ball_vy(-graphics.ball_vy())


if __name__ == '__main__':
    main()
