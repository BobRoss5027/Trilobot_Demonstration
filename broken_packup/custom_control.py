import time
from trilobot import *
import logging
from sshkeyboard import listen_keyboard
from distance_stop import wall
from enum import Enum

# Defines a Trilobot Object to control the motor attachments
tbot = Trilobot()

# Define logging format and level
# To show logs, change `level=logging.INFO` -> `level=logging.DEBUG`
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
            
GLOBAL_SPEED = 0.8 # Speed to drive at, between 0.0 and 1.0
GLOBAL_TURN = 0.25 # Time to turn for, in seconds

class RobotState(Enum): # Possible states for the Trilobot to be in
    STOP = 0
    FORWARD = 1
    LEFT = 2
    RIGHT = 3
    BACKWARD = 4
    DANCE = 5

ROBOTSTATE = RobotState.STOP

class RobotController:
    def __init__(self):
        self.ROBOTSTATE = RobotState.STOP   # Import Trilobot States
    def control(self,key): 
        logging.debug("%s pressed", key)
        tbot.clear_underlighting()
        if key == "w":
            if self.ROBOTSTATE == RobotState.BACKWARD:  # If Trilobot is already moveing backwards, stop
                tbot.stop()
                self.ROBOTSTATE = RobotState.STOP
            else:
                tbot.forward(GLOBAL_SPEED)
                self.ROBOTSTATE = RobotState.FORWARD
            tbot.set_underlights(LIGHTS_FRONT, r_color=GREEN)     
        elif key == "s":
            #Program the robot so it moves backward when s is pressed
            #If the robot is currently moving forward then stop the robot
            tbot.backward(GLOBAL_SPEED)
            self.ROBOTSTATE = RobotState.BACKWARD
            tbot.set_underlights(LIGHTS_REAR, r_color=GREEN)
        elif key == "a":
            #Program the robot to turn left when the a key is pressed
            #If the robot is currently turning right then stop the robot
            tbot.set_underlights(LIGHTS_LEFT, r_color=GREEN)
            tbot.turn_left(GLOBAL_SPEED)
        elif key == "d":
            #Program the robot to turn right when the d key is pressed
            #If the robot is currently turning left then stop the robot
            tbot.set_underlights(LIGHTS_RIGHT, r_color=GREEN)
            tbot.turn_right(GLOBAL_SPEED)
        elif key == "q":
            #If the q key is pressed make the robot dance!!
            tbot.set_underlights(LIGHTS_FRONT, r_color=RED)
        else:
            tbot.stop()
            tbot.fill_underlighting(r_color=RED)
            
if __name__ == "__main__":
    controller = RobotController()
    print("Control this robot using w,a,s,d for movement and space to stop")
    listen_keyboard(on_press=controller.control, sequential=True)