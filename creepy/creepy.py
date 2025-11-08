from sense_hat import SenseHat, ACTION_PRESSED
from datetime import datetime
import time
import logging
import subprocess
import sys

def make_creeper():
    g = (0, 255, 0)
    b = (0, 0, 0)

    return [
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, b, b, g, g, b, b, g,
        g, b, b, g, g, b, b, g,
        g, g, g, b, b, g, g, g,
        g, g, b, b, b, b, g, g,
        g, g, b, b, b, b, g, g,
        g, g, b, g, g, b, g, g
    ]

def make_skeleton():
    g = (112, 112, 112)
    b = (0, 0, 0)

    return [
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, b, b, g, g, b, b, g,
        g, g, g, g, g, g, g, g,
        g, b, b, b, b, b, b, g,
        g, g, g, g, g, g, g, g
    ]

def make_enderman():
    p = (255, 0, 255)
    i = (128, 32, 220)
    b = (0, 0, 0)

    return [
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        p, i, p, b, b, p, i, p,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b
    ]

def make_pig():
    p = (255, 128, 128)
    o = (255, 200, 200)
    q = (100, 50, 50)
    i = (192, 0, 192)
    b = (0, 0, 0)
    w = (255, 255, 255)

    return [
        p, p, p, p, p, p, p, p,
        p, p, p, p, p, p, p, p,
        p, p, p, p, p, p, p, p,
        b, w, p, p, p, p, w, b,
        p, p, o, o, o, o, p, p,
        p, p, q, p, p, q, p, p,
        p, p, o, o, o, o, p, p,
        p, p, p, p, p, p, p, p
    ]

faces = [
    make_creeper(),
    make_enderman(),
    make_pig(),
    make_skeleton()
]

def set_face(index):
    sense.set_pixels(faces[index])

def init_sense():
    sense = SenseHat()
    sense.clear()
    sense.set_rotation(180)
    return sense

def get_handlers():
    args = sys.argv
    handlers = []
    handlers.append(logging.FileHandler('creepy.log'))
    if not '-q' in args:
        handlers.append(logging.StreamHandler())
    return handlers

def init_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s] %(asctime)s - %(message)s',
        handlers=get_handlers())

def update_paused(active):
    for event in sense.stick.get_events():
        if event.action == ACTION_PRESSED:
            active = not active
            if not active:
                sense.clear()
    return active

active = True
sense = init_sense()
init_logging()
try:
    index = 0;
    while True:
        if active:
            set_face(index)
            index = (index + 1) % len(faces)
        time.sleep(3)
        active = update_paused(active)
except KeyboardInterrupt:
    logging.debug('Interrupted.  Cleaning up')
    sense.clear()
