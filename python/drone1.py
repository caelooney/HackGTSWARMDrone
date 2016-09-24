"""
This file will run the
back-end server for drone_1

@author - Jeremiah Lantzer
for: HackGT
"""

from flask import Flask
import time
import ps_drone

# /*/ Clean Start up Sequence /*/ #
drone1 = ps_drone.Drone()               # initializes the drone
drone1.startup()                        # connects the script to the drone
drone1.reset()                          # reset the lights on the drone

while drone1.getBattery()[0] == -1:     # reset complete check
    time.sleep(0.1)

print "Battery: "+str(drone1.getBattery()[0])+"%  "+str(drone1.getBattery()[1])     # outputs current battery level
drone1.useDemoMode(True)                                                            # 15 data sets per second
drone1.getNDpackage(["demo", "vision detect"])                                      # packets to decode
time.sleep(0.5)                                                                     # extra time to complete setup
# /*/ Clean Start up Sequence /*/ #

app = Flask(__name__)


@app.route('/<drone_ID>/right')
def droneright(drone_ID):
    if drone_ID == 1:
        drone1.moveRight(0.5)
        time.sleep(0.1)


@app.route('/<drone_ID>/left')
def droneleft(drone_ID):
    if drone_ID == 1:
        drone1.moveLeft(0.5)
        time.sleep(0.1)


@app.route('/<drone_ID>/forward')
def droneforward(drone_ID):
    if drone_ID == 1:
        drone1.moveForward(0.5)
        time.sleep(0.1)


@app.route('/<drone_ID>/backward')
def dronebackward(drone_ID):
    if drone_ID == 1:
        drone1.moveBackward(0.5)
        time.sleep(0.1)


@app.route('/<drone_ID>/up')
def droneup(drone_ID):
    if drone_ID == 1:
        drone1.moveUp(0.5)
        time.sleep(0.1)


@app.route('/<drone_ID>/down')
def dronedown(drone_ID):
    if drone_ID == 1:
        drone1.moveDown(0.5)
        time.sleep(0.1)


@app.route('/<drone_ID>/turnright')
def robotright(drone_ID):
    if drone_ID == 1:
        drone1.turnRight(0.5)
        time.sleep(0.1)


@app.route('/<drone_ID>/turnleft')
def robotleft(drone_ID):
    if drone_ID == 1:
        drone1.turnLeft(0.5)
        time.sleep(0.1)

if __name__ == "__main__":
    app.run()
