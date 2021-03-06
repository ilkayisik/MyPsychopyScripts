#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This script draws a slider bar on the screen, updates it's position with the
mouse wheel and saves the position, reaction time info
Created on Tue Sep 12 10:30:41 2017
@author: ilkay.isik

"""

from psychopy import visual, core, event, monitors
import numpy as np
import time

#%% monitor
moni = monitors.Monitor('testMonitor', width=53, distance=60,
                        #gamma=0.6
                        )  # in cm
# create a window to draw
win = visual.Window(size=(1920, 1080),#size=(800, 600),
                    color = 'gray', allowGUI=True,
                    monitor=moni,
                    units='deg')


#%% initialize the things to draw in the window

""" Text stimuli """
slider_text_l = visual.TextStim(win=win, height=2, text='L', pos=(-22.5, 0))
slider_text_r = visual.TextStim(win=win, height=2, text='H', pos=(22,0))

""" Response Stimuli"""
TIK_STEP = [1, 0]  # x and y
min, max = [-20, 20]

slider_bar = visual.GratingStim(win=win, tex=None,
                                pos=(0, 0), size=(40+1, 1.5),
                                color='darkgray', interpolate=False)

slider_tik = visual.GratingStim(win=win, tex=None,
                                pos=(0, 0), size=(1, 1.5),
                                color='DarkRed', interpolate=False)
#%%set the mouse
mouse = event.Mouse(win=win)

#%% Rendering
# give the system time to settle
core.wait(0.5)

# create a clock
clock = core.Clock()
clock.reset()

mouse_history = []
while True: #continue until keypress
    state_start = clock.getTime()
    #handle key presses each frame
    for key in event.getKeys():
        if key in ['escape','q']:
            core.quit()


    #Handle the wheel(s): Y is the normal mouse wheel
    wheel_dX, wheel_dY = mouse.getWheelRel()
    if wheel_dY == -1:
        resp_time = clock.getTime() - state_start
        slider_tik.pos = tuple(np.add(slider_tik.pos, TIK_STEP))
        if slider_tik.pos[0] >= max:
            slider_tik.pos =  (max, slider_tik.pos[1])
        mouse_history.append([slider_tik.pos[0], resp_time])

    # Decrease and new_tik_pos will be updated
    elif  wheel_dY == 1:
        resp_time = clock.getTime() -  state_start
        slider_tik.pos = tuple(np.subtract(slider_tik.pos, TIK_STEP))
        if slider_tik.pos[0] <= min:
            slider_tik.pos = (min, slider_tik.pos[1])
        # to save history of the dial
        mouse_history.append([slider_tik.pos[0], resp_time])

    event.clearEvents()#get rid of other, unprocessed events

    # do the drawing
    slider_bar.draw()
    slider_tik.draw()
    slider_text_l.draw()
    slider_text_r.draw()
    win.flip()   #redraw the buffer
