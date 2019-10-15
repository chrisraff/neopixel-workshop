import time
from sys import argv as args
import numpy as np
from serial_library import write, WIDTH, HEIGHT, NUM_LEDS
from color_library import color_names, hsv2rgb


# TODO increase dimensions
rgb = np.array([(255, 255, 255)]*NUM_LEDS)
# rgb = np.zeros((WIDTH, HEIGHT, 3))
# rgb = np.ones((WIDTH, HEIGHT, 3))*255


# non-animated demos (using arguments from the command line)
args = args[1:]
if len(args) == 1:
    color_name = args[0]

    # if you run `python lights.py rainbow` it will show a rainbow
    if color_name == 'rainbow':
        rgb = np.array( [hsv2rgb(i/NUM_LEDS, 1, 1) for i in range(NUM_LEDS)] )
        # rgb = np.array( [hsv2rgb(((i*2)%NUM_LEDS)/NUM_LEDS, 1, 1) for i in range(NUM_LEDS)] )
        write(rgb)

    # if you run `python lights.py green` it will set all the pixels to green
    elif color_name in color_names:
        rgb[:] = color_names[color_name]
        write(rgb)

# arguments are a list of numbers, in the form "r g b r g b ..." where each triple of numbers is the color of the pixel
elif len(args) > 0 and len(args) % 3 == 0:
    a = np.array(list(map(int, args))).reshape(-1,3)
    indexes = np.arange(NUM_LEDS)*a.shape[0]//NUM_LEDS
    indexes = indexes.astype(int)
    rgb = a[indexes,:]
    write(rgb)

else:
    # animated demos
    def millis():
        return int(round(time.time() * 1000))

    last_tick = 0
    frame = 0
    fps = 10
    ms_per_frame = 1000/fps
    while True:
        current_tick = millis()
        if current_tick - last_tick >= ms_per_frame:
            last_tick = current_tick
            frame += 1

            # # rainbow
            sec_per_cycle = fps*10  # number of seconds for each rainbow cycle
            rgb = np.array( [hsv2rgb((frame % sec_per_cycle)/(sec_per_cycle-1), 1, 1)]*NUM_LEDS, dtype=int )
            write(rgb)

            # # single dot
            # rgb = np.zeros((NUM_LEDS, 3), dtype=int)
            # rgb[frame % NUM_LEDS, :] = [255, 0, 0]
            # write(rgb)

