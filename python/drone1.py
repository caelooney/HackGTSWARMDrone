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

drone.trim()                               # reset to the horizontal plane

while drone.getBattery()[0] == -1:         # reset complete check
    time.sleep(0.1)

print "Battery: " + str(drone.getBattery()[0]) + "%  " + str(drone.getBattery()[1])   # outputs current battery level
drone.useDemoMode(True)                                                                # 15 data sets per second
drone.getNDpackage(["demo", "vision detect"])                                          # packets to decode
time.sleep(0.5)                                                                         # extra time to complete setup
# /*/ Clean Start up Sequence /*/ #


app = Flask(__name__)


@app.route('/drone/takeoff')
def dronetakeoff():
    print "Takeoff start"
    drone.takeoff()
    time.sleep(3)
    drone.stop()
    time.sleep(0.5)
    print "Takeoff end"
    return "takeoff"


@app.route('/drone/right')
def droneright():
    print "right start"
    drone.moveRight()
    time.sleep(1.5)
    drone.stop()
    time.sleep(0.5)
    print "right end"
    return "right"


@app.route('/drone/left')
def droneleft():
    print "left start"
    drone.moveLeft()
    time.sleep(1.5)
    drone.stop()
    time.sleep(0.5)
    print "left end"
    return "left"


@app.route('/drone/forward')
def droneforward():
    print "forward start"
    drone.moveForward()
    time.sleep(1.5)
    drone.stop()
    time.sleep(0.5)
    print "forward end"
    return "forward"


@app.route('/drone/backward')
def dronebackward():
    print "backward start"
    drone.moveBackward()
    time.sleep(1.5)
    drone.stop()
    time.sleep(0.5)
    print "backward end"
    return "end"


@app.route('/drone/up')
def droneup():
    print "start up"
    drone.moveUp()
    time.sleep(1.5)
    drone.stop()
    time.sleep(0.5)
    print "end up"
    return "up"


@app.route('/drone/down')
def dronedown():
    print "start down"
    drone.moveDown()
    time.sleep(1.5)
    drone.stop()
    time.sleep(0.5)
    print "end down"
    return "down"


@app.route('/drone/turnright')
def robotright():
    print "start turn right"
    drone.turnRight()
    time.sleep(1.5)
    drone.stop()
    time.sleep(0.5)
    print "end turn right"
    return "turn right"


@app.route('/drone/turnleft')
def robotleft():
    print "start turn left"
    drone.turnLeft()
    time.sleep(1.5)
    drone.stop()
    time.sleep(0.5)
    print "end turn left"
    return "turn left"


@app.route('/drone/land')
def droneland():
    print "start land"
    drone.moveDown()
    time.sleep(1.5)
    drone.land()
    time.sleep(0.5)
    print "end land"
    return "land"


if __name__ == "__main__":
    app.run()
