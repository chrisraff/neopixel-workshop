import time
import sys
import numpy as np
from serial_library import write
from color_library import color_names, hsv2rgb


NUM_LEDS = 226
rgb = np.array([(255, 255, 255)]*NUM_LEDS)


# read in the color arguments
args = sys.argv[1:]
if len(args) == 1:
    color_name = args[0]

    if color_name == 'rainbow':
        rgb = np.array( [hsv2rgb(i/NUM_LEDS, 1, 1) for i in range(NUM_LEDS)] )
        # rgb = np.array( [hsv2rgb(((i*2)%NUM_LEDS)/NUM_LEDS, 1, 1) for i in range(NUM_LEDS)] )
        write(rgb)

    elif color_name in color_names:
        rgb[:] = color_names[color_name]
        write(rgb)

elif len(args) > 0 and len(args) % 3 == 0:
    a = np.array(list(map(int, args))).reshape(-1,3)
    indexes = np.arange(NUM_LEDS)*a.shape[0]//NUM_LEDS
    indexes = indexes.astype(int)
    rgb = a[indexes,:]
    write(rgb)

else:
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

