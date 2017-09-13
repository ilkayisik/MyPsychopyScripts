#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
This script is created to test the current designs dial output.
It uses pywinusb library to connect to the dial, read the data
and prints the dial input in a separate window
@author: omer faruk gulban / ilkay isik
'''
from psychopy import visual, core, event, monitors
import numpy as np
import pywinusb.hid as hid

#%% Current designs dial
# product info
VENDOR_ID = 6171
PRODUCT_ID = 8

#Find the device
myDevice = hid.HidDeviceFilter(vendor_id=VENDOR_ID,
                              product_id=PRODUCT_ID).get_devices()

dial_input = [0, 0, 0, 0, 0, 0]
# Functions for  dial input
def rotation_listener(data):
    """Print dial input only for rotation."""
    global dial_input
    dial_input = data[1]

def curdes_rotation_listener(data):
    """Print dial input in a way that the output does not wrap after reaching
    extremes ends"""
    global dial_input, prev_cycle
    if data[2] <= 112:
        dial_input = data[1] + 256*data[2]
    else:
        dial_input = data[1] - (data[2]%256)

# alternative function for data handler specific to curdes dial.
prev_data = [0, 0, 0, 0, 0, 0]
def curdes_dial_direction(data):
    """Derive Current Designs dial direction from raw input."""
    global prev_data, dial_input
    #print"Direction: ", (prev_data[1] - data[1])%256
    dial_input = (prev_data[1] - data[1])%256
    prev_data = data

if myDevice:
    curdes_dial = myDevice[0]
    print "Current designs dial is connected"
    curdes_dial.open()

    # Set a function to determine the data type
    #curdes_dial.set_raw_data_handler(rotation_listener)
    #curdes_dial.set_raw_data_handler(curdes_rotation_listener)
    curdes_dial.set_raw_data_handler(curdes_dial_direction)


if not myDevice:
    print ("Can't find current designs dial!")


# %%
""" Monitor """
# set monitor information used in the experimental setup
moni = monitors.Monitor('testMonitor', width=8.2, distance=60)  # in cm

# create a window to draw
mywin = visual.Window(size=(800, 600), screen=0, winType='pyglet',
                      allowGUI=True, color = 'gray', fullscr=False, monitor=moni)

# %%
""" Stimulus """
text = visual.TextStim(win=mywin, text='test', color='black', height=0.3)


# %%
""" Time """
# give the system time to settle
core.wait(0.5)

# %%
""" Render Loop """
switch = True
while switch:
    # change text according to the dial input
    text.text = str(dial_input)
    text.draw()
    mywin.flip()

    # handle key presses each frame
    for keys in event.getKeys(timeStamped=True):
        if keys[0] in ['t']:
            switch = False
        elif keys[0] in ['escape', 'q']:
            mywin.close()
            core.quit()

mywin.close()
core.quit()
