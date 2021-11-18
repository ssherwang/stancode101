"""
File: bouncing_ball
Name: Sher Wang
-------------------------
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

# Global variables
run = 0
bouncing = False

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
window.add(ball)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(trigger)                                 # trigger mouse event, bouncing ball


def trigger(mouse):
    global run, ball, bouncing                              # import global variables
    if bouncing is True:                                    # set condition to avoid multiple clicks
        pass
    else:
        bouncing = True                                     # block for triggering the next event by mouse click
        run += 1                                            # run counter (limitation : 3)
        if run <= 3:
            window.remove(ball)
            window.add(ball, x=START_X, y=START_Y)
            vx = VX                                         # initial velocity of Vx
            vy = 0                                          # initial velocity of Vy
            while True:
                if (ball.x+SIZE) >= window.width:           # when the ball bounces outside the window
                    window.add(ball, x=START_X, y=START_Y)  # go back to initial position
                    break
                else:
                    ball.move(vx, vy)
                    if (ball.y+SIZE) >= window.height:      # when the ball bounces to the ground
                        ball.y = (window.height - SIZE)     # assume the ball is hitting on the ground
                        vy = -vy*REDUCE                     # ball bounces from the ground
                    else:
                        vy = vy + GRAVITY                   # velocity changing with gravity
                    pause(DELAY)
        bouncing = False



if __name__ == "__main__":
    main()
