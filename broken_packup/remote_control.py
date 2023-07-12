import time
from trilobot import *
import logging
from sshkeyboard import listen_keyboard
from distance_stop import wall

"""
Simple program to control a Trilobot using an SSH connection.

Control the Trilobot by using W,A,S,D to move and turn, and press space to stop

Press ESC to end the program
"""

# Defines a Trilobot Object to control the motor attachments
tbot = Trilobot()

# Define logging format and level
# To show logs, change `level=logging.INFO` -> `level=logging.DEBUG`
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
          
GLOBAL_SPEED = 0.8 # Speed to drive at, between 0.0 and 1.0
GLOBAL_TURN = 0.5 # Time to turn for, in seconds
   
def control(key):    
    logging.debug("%s pressed", key)
    tbot.clear_underlighting()
    if key == "w":  # Move forwards when w pressed
        tbot.set_underlights(LIGHTS_FRONT, r_color=[0,255,0])
        tbot.forward(GLOBAL_SPEED)
    elif key == "s":    # Move backwards when s pressed
        tbot.set_underlights(LIGHTS_REAR, r_color=[0,255,0])
        tbot.backward(GLOBAL_SPEED)
    elif key == "a":    # Turn left when a pressed
        tbot.set_underlights(LIGHTS_LEFT, r_color=[0,255,0])
        tbot.turn_left(GLOBAL_SPEED)
        time.sleep(GLOBAL_TURN)
        tbot.stop()
        tbot.clear_underlighting()
        tbot.fill_underlighting(r_color=[0,0,255])
    elif key == "d":    # Turn right when d pressed
        tbot.set_underlights(LIGHTS_RIGHT, r_color=[0,255,0])
        tbot.turn_right(GLOBAL_SPEED)
        time.sleep(GLOBAL_TURN)
        tbot.stop()
        tbot.clear_underlighting()
        tbot.fill_underlighting(r_color=[0,0,255])
    else:   # Stop when any other key pressed 
        tbot.stop()
        tbot.fill_underlighting(r_color=[255,0,0])
            
if __name__ == "__main__":
    print("Control this robot using w,a,s,d for movement and space to stop. Press ESC to stop this program.")
    listen_keyboard(on_press=control, sequential=True)  # Listens for key pressed in SSH sessions