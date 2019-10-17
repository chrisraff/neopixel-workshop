# cycle through hues, show a rainbow
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
hue = 0.0

# set a target framerate (max possible is around 60)
fps = 30
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

    # assign the whole matrix to be one color
    leds[:, :] = hsv2rgb(hue, 1, 1)

    # change hue over time
    hue += 0.01

    # END DRAWING LOGIC

    # stay at target framerate
    sleep_duration = last_draw_time + spf - time()
    if sleep_duration > 0:
        sleep(sleep_duration)
    last_draw_time = time()

    # update the matrix
    write(leds)
