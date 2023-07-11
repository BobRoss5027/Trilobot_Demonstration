import time
from trilobot import *
import logging
from sshkeyboard import listen_keyboard
from distance_stop import wall

tbot = Trilobot()
global show
show = True

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG,datefmt="%H:%M:%S")

def flashing():
    global show
    INTERVAL = 0.1  # control the speed of the LED animation

    RED = (255, 0, 0)

    # Map so 0-5 goes from left to right.
    MAPPING = [LIGHT_REAR_LEFT,
            LIGHT_MIDDLE_LEFT,
            LIGHT_FRONT_LEFT,
            LIGHT_FRONT_RIGHT,
            LIGHT_MIDDLE_RIGHT,
            LIGHT_REAR_RIGHT]

    while show:
        for n in range(0, NUM_UNDERLIGHTS - 1):
            phy_led = MAPPING[n]
            tbot.clear_underlighting(show=False)
            tbot.set_underlight(phy_led, RED)
            time.sleep(INTERVAL)

        for n in range(NUM_UNDERLIGHTS - 1, 0, -1):
            phy_led = MAPPING[n]
            tbot.clear_underlighting(show=False)
            tbot.set_underlight(phy_led, RED)
            time.sleep(INTERVAL)
            
GLOBAL_SPEED = 0.8
   
def control(key):  
    global show   

    logging.debug("%s pressed", key)
    tbot.clear_underlighting()
    if key == "w":
        tbot.set_underlights(LIGHTS_FRONT, r_color=[0,255,0])
        tbot.forward(GLOBAL_SPEED)
    elif key == "s":
        tbot.set_underlights(LIGHTS_REAR, r_color=[0,255,0])
        tbot.backward(GLOBAL_SPEED)
    elif key == "a":
        tbot.set_underlights(LIGHTS_LEFT, r_color=[0,255,0])
        tbot.turn_left(GLOBAL_SPEED)
        time.sleep(0.5)
        tbot.stop()
        tbot.clear_underlighting()
        tbot.set_underlights(LIGHTS_FRONT, r_color=[0,255,0])
    elif key == "d":
        tbot.set_underlights(LIGHTS_RIGHT, r_color=[0,255,0])
        tbot.turn_right(GLOBAL_SPEED)
        time.sleep(0.5)
        tbot.stop()
        tbot.clear_underlighting()
        tbot.set_underlights(LIGHTS_FRONT, r_color=[0,255,0])
    else:
        tbot.stop()
        show=True
        tbot.fill_underlighting(r_color=[255,0,0])
            
if __name__ == "__main__":
    print("Control this robot using w,a,s,d for movement and space to stop")
    listen_keyboard(on_press=control, sequential=True)