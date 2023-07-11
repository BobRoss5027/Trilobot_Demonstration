import time
from trilobot import *
import logging
from sshkeyboard import listen_keyboard
from distance_stop import wall

tbot = Trilobot()

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
            
GLOBAL_SPEED = 0.8
GLOBAL_TURN = 0.5
   
def control(key):    

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
        time.sleep(GLOBAL_TURN)
        tbot.stop()
        tbot.clear_underlighting()
        tbot.set_underlights(LIGHTS_FRONT, r_color=[0,255,0])
    elif key == "d":
        tbot.set_underlights(LIGHTS_RIGHT, r_color=[0,255,0])
        tbot.turn_right(GLOBAL_SPEED)
        time.sleep(GLOBAL_TURN)
        tbot.stop()
        tbot.clear_underlighting()
        tbot.set_underlights(LIGHTS_FRONT, r_color=[0,255,0])
    else:
        tbot.stop()
        show=True
        tbot.fill_underlighting(r_color=[255,0,0])
            
if __name__ == "__main__":
    print("Control this robot using w,a,s,d for movement and space to stop. Press ESC to stop this program.")
    listen_keyboard(on_press=control, sequential=True)