from trilobot import *
import logging
from time import sleep

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG,datefmt="%H:%M:%S")

def wall(tbot, GLOBAL_SPEED):
    while not tbot.read_button(BUTTON_A):
        distance=tbot.read_distance(timeout=100, samples=9)
        logging.debug("%s cm from wall", distance)
        if distance < 20:
            logging.debug("Too Close")
            tbot.backward(GLOBAL_SPEED)
            tbot.set_underlights(LIGHTS_REAR,r_color=[0,255,0])
            sleep(0.2)
            tbot.stop()
            tbot.fill_underlighting(r_color=[255,0,0])