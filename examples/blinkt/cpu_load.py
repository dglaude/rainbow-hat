#!/usr/bin/env python

import math
import time
from sys import exit

try:
    import psutil
except ImportError:
    exit("This script requires the psutil module\nInstall with: sudo pip install psutil")

import rainbowhat

set_clear_on_exit=rainbowhat.rainbow.set_clear_on_exit
set_pixel=rainbowhat.rainbow.set_pixel
show=rainbowhat.rainbow.show
set_brightness=rainbowhat.rainbow.set_brightness

set_clear_on_exit()

def show_graph(v, r, g, b):
    v *= 7
    for x in range(7):
        if v  < 0:
            r, g, b = 0, 0, 0
        else:
            r, g, b = [int(min(v,1.0) * c) for c in [r,g,b]]

        set_pixel(x, r, g, b)

        v -= 1

    show()

set_brightness(0.1)

while True:
    v = psutil.cpu_percent() / 100.0
    show_graph(v, 255, 255, 255)
    time.sleep(0.01)
