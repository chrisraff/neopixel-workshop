from serial_library import write, WIDTH, HEIGHT
from color_library import color_names, hsv2rgb
from time import time, sleep
import numpy as np

##############################################
# SET UP
##############################################

# initialize led array
leds = np.zeros((WIDTH, HEIGHT, 3))

# variables for drawing logic go here

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

    # TODO Delete the next line and make something cool
    leds[:, :] = ((255 if time() % 2 < 1 else 0), 0, 0)

    # END DRAWING LOGIC

    # stay at target framerate
    sleep_duration = last_draw_time + spf - time()
    if sleep_duration > 0:
        sleep(sleep_duration)
    last_draw_time = time()

    # update the matrix
    write(leds)
