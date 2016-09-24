"""
This file will run the
back-end server for drone_2

@author - Jeremiah Lantzer
for: HackGT
"""

from flask import Flask
import time
import ps_drone

# /*/ Clean Start up Sequence /*/ #
drone2 = ps_drone.Drone()               # initializes the drone
drone2.startup()                        # connects the script to the drone
drone2.reset()                          # reset the lights on the drone

while drone2.getBattery()[0] == -1:     # reset complete check
    time.sleep(0.1)

print "Battery: "+str(drone2.getBattery()[0])+"%  "+str(drone2.getBattery()[1])     # outputs current battery level
drone2.useDemoMode(True)                                                            # 15 data sets per second
drone2.getNDpackage(["demo", "vision detect"])                                      # packets to decode
time.sleep(0.5)                                                                     # extra time to complete setup
# /*/ Clean Start up Sequence /*/ #

app = Flask(__name__)


@app.route('/<drone_ID>/right')
def droneright(drone_ID):
    if drone_ID == 1:
        drone2.moveRight(0.5)


@app.route('/<drone_ID>/left')
def droneleft(drone_ID):
    if drone_ID == 1:
        drone2.moveLeft(0.5)


@app.route('/<drone_ID>/forward')
def droneforward(drone_ID):
    if drone_ID == 1:
        drone2.moveForward(0.5)


@app.route('/<drone_ID>/backward')
def dronebackward(drone_ID):
    if drone_ID == 1:
        drone2.moveBackward(0.5)


@app.route('/<drone_ID>/up')
def droneup(drone_ID):
    if drone_ID == 1:
        drone2.moveUp(0.5)


@app.route('/<drone_ID>/down')
def dronedown(drone_ID):
    if drone_ID == 1:
        drone2.moveDown(0.5)


@app.route('/<drone_ID>/turnright')
def robotright(drone_ID):
    if drone_ID == 1:
        drone2.turnRight(0.5)


@app.route('/<drone_ID>/turnleft')
def robotleft(drone_ID):
    if drone_ID == 1:
        drone2.turnLeft(0.5)

if __name__ == "__main__":
    app.run()
