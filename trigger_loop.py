# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 19:40:06 2017

@author: ilkay.isik
"""
'''Wait the trigger using parallel port input.
Use the response box from Cornelius to emulate signal.
'''
from psychopy import visual, parallel, core, event

# Does the computer have a parallel port (True or False)
parallel_port = True

if parallel_port:  # this solution is for windows machines
    from psychopy.parallel._inpout32 import PParallelInpOut32
    port = PParallelInpOut32()
    # Parallel port related parameters
    pin = 13 #scanner=10
    expected_trigger = 0  # can be 0 or 1

clock = core.Clock()
print clock.getTime()

receive_trigger =0
counter=0
while clock.getTime() < 1:
    if parallel_port and port.readPin(pin) == expected_trigger:
        receive_trigger+=1
    for keys in event.getKeys():
        if keys in ['5']:
            pass
    counter+=1
    
print counter
print receive_trigger






