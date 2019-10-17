# a pixel bounces around
from neopixel.serial_library import write, WIDTH, HEIGHT
from neopixel.color_library import color_names, hsv2rgb
from time import time, sleep
import numpy as np

##############################################
# SET UP
##############################################

# initialize led array
leds = np.zeros((WIDTH, HEIGHT, 3))

# variables for drawing logic
ball_pos = np.array([2, 2])
ball_dpos = np.array([1, -1])
ball_hue = 0.0

# set a target framerate (max possible is around 60)
fps = 15
# variables for framerate logic
spf = 1 / fps
last_draw_time = time()


##############################################
# DRAW LOOP
##############################################

while True:

    #----------------------------------------
    # DRAWING LOGIC
    #----------------------------------------
    
    # turn off the pixel where the ball used to be (prevent leaving a trail)
    leds[ball_pos[0], ball_pos[1]] = (0,0,0)

    # update the position of the ball
    ball_pos += ball_dpos

    # check for bounce on x axis
    # if ball passed the near wall or the far wall
    if not (0 < ball_pos[0] < WIDTH-1):
        # reverse direction on this axis
        ball_dpos[0] *= -1

    # check for bounce on y axis
    # if ball passed the near wall or the far wall
    if not (0 < ball_pos[1] < HEIGHT-1):
        # reverse direction on this axis
        ball_dpos[1] *= -1

    leds[ball_pos[0], ball_pos[1]] = hsv2rgb(ball_hue, 1, 1)

    # make the ball change color
    ball_hue += 0.01

    # END DRAWING LOGIC

    # stay at target framerate
    sleep_duration = last_draw_time + spf - time()
    if sleep_duration > 0:
        sleep(sleep_duration)
    last_draw_time = time()

    # update the matrix
    write(leds)
