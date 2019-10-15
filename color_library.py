import colorsys

color_names = {
    'red': (255,0,0),
    'orange': (64,16,0),
    'sunset': (104,16,0),
    'macaroni': (96,32,0),
    'yellow': (255,128,0),
    'green': (0,255,0),
    'blue': (0,0,255),
    'turqoise': (0,255,128),
    'seafoam': (0,255,64),
    'cyan': (0,255,255),
    'purple': (128,0,150),
    'magenta': (255,0,255),
    'pink': (255,0,64),
    'rose': (255,0,25),
    'white': (255,255,255),
    'black': (0,0,0),
}

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
