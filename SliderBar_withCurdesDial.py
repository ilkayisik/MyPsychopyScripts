#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Still under development
this script reads the current designs data info and moves the slider
cursor based on the turn of the direction
issues:
1) where to start the dial,
2) what should be the step size
@author: ilkay.isik
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
moni = monitors.Monitor('testMonitor', width=53, distance=60)

# set screen (make 'fullscr = True' for fullscreen)
mywin = visual.Window(size=(1920, 1080),#size=(800,600),
                    screen=0, winType='pyglet',
                    allowGUI=False,  # show mouse
                    fullscr=True,
                    monitor=moni,
                    color='grey',
                    colorSpace='rgb',
                    units='deg',
                    useFBO=True,
                    )

# %%
""" Stimulus """
text = visual.TextStim(win=mywin, text='test', color='black', height=0.3)

slider_text_l = visual.TextStim(win=mywin, height=2, text='L', pos=(-22.5, 0))
slider_text_r = visual.TextStim(win=mywin, height=2, text='H', pos=(22,0))

""" Response Stimuli"""
TIK_STEP = [0.5, 0]  # x and y
min, max = [-20, 20]

slider_bar = visual.GratingStim(win=mywin, tex=None,
                                pos=(0, 0), size=(40+1, 1.5),
                                color='darkgray', interpolate=False)

slider_tik = visual.GratingStim(win=mywin, tex=None,
                                pos=(0, 0), size=(1, 1.5),
                                color='DarkRed', interpolate=False)

# %%
""" Time """
# give the system time to settle
core.wait(0.5)

# create a clock
clock = core.Clock()
clock.reset()

dial_history = []
while True: #continue until keypress
    state_start = clock.getTime()
    #handle key presses each frame
    for key in event.getKeys():
        if key in ['escape','q']:
            core.quit()

    #Increase or decrease the slider position baes on the direction

    if dial_input == 255: #increase
        resp_time = clock.getTime() - state_start
        slider_tik.pos = tuple(np.add(slider_tik.pos, TIK_STEP))
        if slider_tik.pos[0] >= max:
            slider_tik.pos =  (max, slider_tik.pos[1])
        dial_history.append([slider_tik.pos[0], resp_time])

    # Decrease and new_tik_pos will be updated
elif  dial_input == 1: #decrease
        resp_time = clock.getTime() -  state_start
        slider_tik.pos = tuple(np.subtract(slider_tik.pos, TIK_STEP))
        if slider_tik.pos[0] <= min:
            slider_tik.pos = (min, slider_tik.pos[1])
        # to save history of the dial
        dial_history.append([slider_tik.pos[0], resp_time])

    event.clearEvents()#get rid of other, unprocessed events

    # do the drawing
    slider_bar.draw()
    slider_tik.draw()
    slider_text_l.draw()
    slider_text_r.draw()
    mywin.flip()   #redraw the buffer
