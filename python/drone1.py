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
drone = ps_drone.Drone()                   # initializes the drone
drone.startup()                            # connects the script to the drone
drone.reset()                              # reset the lights on the drone

while drone.getBattery()[0] == -1:         # reset complete check
    time.sleep(0.1)

print "Battery: " + str(drone.getBattery()[0]) + "%  " + str(drone.getBattery()[1])   # outputs current battery level
drone.useDemoMode(True)                                                                # 15 data sets per second
drone.getNDpackage(["demo", "vision detect"])                                          # packets to decode
time.sleep(0.5)                                                                         # extra time to complete setup
# /*/ Clean Start up Sequence /*/ #


app = Flask(__name__)


@app.route('/drone/right')
def droneright():
    drone.moveRight(0.5)
    time.sleep(0.1)


@app.route('/drone/left')
def droneleft():
    drone.moveLeft(0.5)
    time.sleep(0.1)


@app.route('/drone/forward')
def droneforward():
    drone.moveForward(0.5)
    time.sleep(0.1)


@app.route('/drone/backward')
def dronebackward():
    drone.moveBackward(0.5)
    time.sleep(0.1)


@app.route('/drone/up')
def droneup():
    drone.moveUp(0.5)
    time.sleep(0.1)


@app.route('/drone/down')
def dronedown():
    drone.moveDown(0.5)
    time.sleep(0.1)


@app.route('/drone/turnright')
def robotright():
    drone.turnRight(0.5)
    time.sleep(0.1)


@app.route('/drone/turnleft')
def robotleft():
    drone.turnLeft(0.5)
    time.sleep(0.1)


if __name__ == "__main__":
    
    app.run()
