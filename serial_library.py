import numpy as np
from serial.tools.list_ports import comports
import serial

WIDTH = 32*2
HEIGHT = 8
NUM_LEDS = WIDTH * HEIGHT

# connect to the open serial port
ports = list(map(lambda x: x[0], comports()))
port_index = 0

if len(ports) == 0:
	print("couldn't find any open ports")
	exit()

elif len(ports) > 1:
	print("enter a number to choose a serial port")
	print("======================================")
	print("\n".join([f" [{i}] {x}" for i,x in enumerate(ports)]))
	x = input()
	assert x.isdigit(), "must specify a number"
	x = int(x)
	assert 0 <= x < len(ports), "number specified not in range"
	port_index = x

ser = serial.Serial(ports[port_index], 115200, timeout=0.2)



def write_channel(channel, values):
	if not 0 <= channel <= 2:
		print("channel must be between 0 and 2")
		exit()
	output = bytearray([channel]+list(values))
	ser.write(output)


# input shape is (height, width, 3)
def write(rgb_image):
	pixel_count = rgb_image.shape[0] * rgb_image.shape[1]
	rgb = rgb_image.flatten()

	if pixel_count > NUM_LEDS:
		print("ERROR: trying to write to too many LEDs")
		rgb = rgb[:NUM_LEDS]
	if pixel_count < NUM_LEDS:
		print("WARNING: trying to write to too few LEDs")
		rgb = np.array([(255, 255, 255)]*NUM_LEDS)
		rgb[0::2,:] = [255, 0, 0]
	if np.any(rgb < 0):
		print("WARNING: negative values in array")
	if np.any(rgb > 255):
		print("WARNING: values in array above 255")
	rgb = np.clip(np.round(rgb), 0, 255).astype(np.int8)

	data = b'['

	# write pixels until every pixel has been sent
	written = 0
	while written * 3 < len(rgb):
		# check whether to write a group of 64 pixels or 1 pixel
		if len(rgb) - written * 3 >= 64 * 3:
			print("writing 64 pixels, delete line 64 of serial_library") # TODO delete after testing
			data += b'.'
			data += bytearray(rgb[written * 3 : (written + 64) * 3].tolist())
			
			written += 64
		else:
			data += b'>'
			data += bytearray(rgb[written * 3: written * 3 + 3].tolist())

			written += 1
	
	data += b']'

	ser.write(data)
