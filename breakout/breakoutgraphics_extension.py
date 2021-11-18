"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This program aims to create a very classical game, breakout, by Python.
At the beginning, player will have three lives.
When all of bricks disappear, player win the game.

In this extension version, the velocity of ball will increase with score.
When brick remains account for only 20% of total amount,
the score for each collision will change from 1 points to 10 points.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.__paddle = GRect(paddle_width, paddle_height)
        self.__paddle.filled = True
        self.window.add(self.__paddle, x=(self.window.width - self.__paddle.width) / 2,
                        y=self.window.height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)

        # Default initial velocity for the ball
        self._dy = 0
        self._dx = 0

        # Initialize our mouse listeners, running is a switch to start game
        self.__running = False
        onmouseclicked(self.game_start)
        onmousemoved(self.move_click)

        # Score count, initial score is 0,use GLabel to make score label.
        self.__score = 0
        self.__score_label = GLabel('Score: ' + str(self.__score))
        self.__score_label.font = '-20-bold'
        self.__score_label.color = 'blue'
        self.window.add(self.__score_label, x=0, y=brick_offset - self.__score_label.height)

        # Lives count, initial lives are 3, use GLabel to make lives label.
        self.__life = 3
        self.__lives_label = GLabel('Lives: ' + str(self.__life))
        self.__lives_label.font = '-20-bold'
        self.__lives_label.color = 'blue'
        self.window.add(self.__lives_label, x=window_width-self.__lives_label.width,
                        y=brick_offset - self.__lives_label.height)

        # Draw bricks, bricks at each raw are different color.
        self.__total_brick = 0
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.__brick = GRect(brick_width, brick_height)
                self.__brick.filled = True
                if j <= 1:
                    self.__brick.fill_color = 'red'
                elif 2 <= j <= 3:
                    self.__brick.fill_color = 'orange'
                elif 4 <= j <= 5:
                    self.__brick.fill_color = 'yellow'
                elif 6 <= j <= 7:
                    self.__brick.fill_color = 'green'
                else:
                    self.__brick.fill_color = 'blue'
                self.brick_x = i * (brick_width + brick_spacing)
                self.brick_y = brick_offset + j * (brick_height + brick_spacing)
                self.window.add(self.__brick, x=self.brick_x, y=self.brick_y)
                self.__total_brick += 1
                self._original_brick = self.__total_brick

    # collision check function
    def collision_check(self):
        obj_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj_2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        obj_3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        obj_4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)

        # collision condition on different four points of ball
        if obj_1 is not None and obj_1 is not self.__paddle and obj_1 is not self.__score_label \
                and obj_1 is not self.__lives_label:
            self.window.remove(obj_1)
            self.__total_brick -= 1
            # ball velocity increase 1% with each collision of ball
            self._dy = -self._dy*1.01
            # score will change from 1 to 10 when bricks on screen remains only 20% of the initial amount of bricks.
            if (self.__total_brick / self._original_brick) <= 0.2:
                self.__score += 10
            else:
                self.__score += 1
            # change score on score label
            self.__score_label.text = 'Score: ' + str(self.__score)

        elif obj_2 is not None and obj_2 is not self.__paddle and obj_2 is not self.__score_label\
                and obj_2 is not self.__lives_label:
            self.window.remove(obj_2)
            self.__total_brick -= 1
            # ball velocity increase 1% with each collision of ball
            self._dy = -self._dy*1.01
            # score will change from 1 to 10 when bricks on screen remains only 20% of the initial amount of bricks.
            if (self.__total_brick / self._original_brick) <= 0.2:
                self.__score += 10
            else:
                self.__score += 1
            # change score on score label
            self.__score_label.text = 'Score: ' + str(self.__score)

        elif obj_3 is not None and obj_3 is not self.__paddle and obj_3 is not self.__score_label\
                and obj_3 is not self.__lives_label:
            self.window.remove(obj_3)
            self.__total_brick -= 1
            # ball velocity increase 1% with each collision of ball
            self._dy = -self._dy*1.01
            # score will change from 1 to 10 when bricks on screen remains only 20% of the initial amount of bricks.
            if (self.__total_brick / self._original_brick) <= 0.2:
                self.__score += 10
            else:
                self.__score += 1
            # change score on score label
            self.__score_label.text = 'Score: ' + str(self.__score)

        elif obj_4 is not None and obj_4 is not self.__paddle and obj_4 is not self.__score_label\
                and obj_4 is not self.__lives_label:
            self.window.remove(obj_4)
            self.__total_brick -= 1
            # ball velocity increase 1% with each collision of ball
            self._dy = -self._dy*1.01
            # score will change from 1 to 10 when bricks on screen remains only 20% of the initial amount of bricks.
            if (self.__total_brick / self._original_brick) <= 0.2:
                self.__score += 10
            else:
                self.__score += 1
            # change score on score label
            self.__score_label.text = 'Score: ' + str(self.__score)
        # when ball hits the paddle
        elif obj_3 is not None and obj_3 is self.__paddle:
            if self._dy > 0:
                self._dy = -self._dy
        elif obj_4 is not None and obj_4 is self.__paddle:
            if self._dy > 0:
                self._dy = -self._dy

    # reset ball position
    def reset_ball(self):
        self.window.remove(self.ball)
        self.__running = False
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)
        self._dx = 0
        self._dy = 0

    # on-mouse click start function
    def game_start(self, event):
        if self.__running is True:
            pass
        else:
            self.__running = True
            self.ball.move(self._dx, self._dy)
            self._dy = INITIAL_Y_SPEED
            self._dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self._dx = -self._dx

    # paddle controller
    def move_click(self, mouse):
        # mouse out of left range
        if mouse.x <= 0:
            self.__paddle.x = 0
        # mouse out of right range
        elif mouse.x >= self.window.width - self.__paddle.width:
            self.__paddle.x = self.window.width - self.__paddle.width
        # mouse within the window
        elif 0 <= mouse.x <= self.window.width - self.__paddle.width:
            self.__paddle.x = mouse.x

    # ball velocity setter
    def set_ball_vx(self, new_vx):
        self._dx = new_vx

    # ball velocity setter
    def set_ball_vy(self, new_vy):
        self._dy = new_vy

    # ball velocity getter
    def ball_vx(self):
        return self._dx

    # ball velocity getter
    def ball_vy(self):
        return self._dy

    # total brick count getter
    def brick_remain(self):
        return self.__total_brick

    # lives count setter
    def reset_lives_count(self, new_lives):
        self.__life -= new_lives
        self.__lives_label.text = 'Lives: ' + str(self.__life)

    # win sign
    def win(self):
        win_label = GLabel('You Win !')
        win_back_ground = GRect(self.window.width, self.window.height)
        win_back_ground.filled = True
        win_label.font = '-50-bold'
        win_label.color = 'white'
        self.window.add(win_back_ground)
        self.window.add(win_label, x=(self.window.width - win_label.width)/2,
                        y=(self.window.height - win_label.height)/2)

    # game over sign
    def over(self):
        over_label = GLabel('You Loss !')
        over_back_ground = GRect(self.window.width, self.window.height)
        over_back_ground.filled = True
        over_label.font = '-50-bold'
        over_label.color = 'white'
        self.window.add(over_back_ground)
        self.window.add(over_label, x=(self.window.width - over_label.width)/2,
                        y=(self.window.height - over_label.height)/2)

