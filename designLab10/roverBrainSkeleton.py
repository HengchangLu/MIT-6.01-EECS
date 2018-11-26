import math
import lib601.util as util
import lib601.sm as sm
import lib601.gfx as gfx
from soar.io import io

import os
labPath = os.getcwd()
from sys import path
if not labPath in path:
    path.append(labPath)
    print 'setting labPath to', labPath

from boundaryFollower import boundaryFollowerClass


class Stop(sm.SM):
    def getNextValues(self, state, inp):
        return state, io.Action(fvel=0, rvel=0)


class MySMClass(sm.SM):

    def getNextValues(self, state, inp):
        [neck, left, right] = inp.analogInputs[0:3]
        sonars = inp.sonars
        [neck, left, right] = inp.analogInputs[0:3]
        gain = 1
        if -0.2 < neck - 5 < 0.2:
            # return (state, io.Action(fvel=1, rvel=0))
            mySM = boundaryFollowerClass()
        else:
            return (state, io.Action(fvel=0, rvel=gain * (neck - 5)))
        # return state, io.Action(fvel=0.1, rvel=gain * (inp.analogInputs[1]-inp.analogInputs[2]))


mySM = MySMClass()
mySM.name = 'brainSM'
    

######################################################################
###
###          Brain methods
###
######################################################################

def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False)

def brainStart():
    robot.behavior = mySM
    robot.behavior.start(robot.gfx.tasks())
    robot.data = []

def step():
    inp = io.SensorInput().analogInputs
    inp = io.SensorInput()
    robot.behavior.step(inp).execute()

def brainStop():
    pass

def shutdown():
    pass
