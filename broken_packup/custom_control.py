import time
from trilobot import *
import logging
from sshkeyboard import listen_keyboard
from distance_stop import wall
from enum import Enum

tbot = Trilobot()

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG,datefmt="%H:%M:%S")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
            
GLOBAL_SPEED = 0.8
TURN_DURATION = 0.25

class RobotState(Enum):
    STOP = 0
    FORWARD = 1
    LEFT = 2
    RIGHT = 3
    BACKWARD = 4
    DANCE = 5

ROBOTSTATE = RobotState.STOP

class RobotController:
    def __init__(self):
        self.ROBOTSTATE = RobotState.STOP
    def control(self,key): 
        logging.debug("%s pressed", key)
        tbot.clear_underlighting()
        if key == "w":
            if self.ROBOTSTATE == RobotState.BACKWARD:
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
            tbot.turn_left(GLOBAL_SPEED)
        elif key == "d":
            #Program the robot to turn right when the d key is pressed
            #If the robot is currently turning left then stop the robot
            tbot.set_underlights(LIGHTS_RIGHT, r_color=GREEN)
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