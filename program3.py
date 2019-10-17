# change brightness over time
from neopixel.serial_library import write, WIDTH, HEIGHT
from neopixel.color_library import color_names, hsv2rgb
from time import time, sleep
import numpy as np

##############################################
# SET UP
##############################################

# initialize led array
leds = np.zeros((WIDTH, HEIGHT, 3))

# we need to keep track of which frame we're on
brightness = 0

# set a target framerate (max possible is around 60)
fps = 10
# variables for framerate logic
spf = 1 / fps
last_draw_time = time()


##############################################
# DRAW LOOP
##############################################

while True:

    #----------------------------------------
    # DRAWING LOGIC GOES HERE
    #----------------------------------------

    # [:, :] assigns the same color to every LED in the array
    leds[:, :] = (brightness, 0, 0)

    # keep track of which frame it is
    brightness += 6

    # prevent brightness from going above the maximum value, 255
    brightness = brightness % 256

    # END DRAWING LOGIC

    # stay at target framerate
    sleep_duration = last_draw_time + spf - time()
    if sleep_duration > 0:
        sleep(sleep_duration)
    last_draw_time = time()

    # update the matrix
    write(leds)
