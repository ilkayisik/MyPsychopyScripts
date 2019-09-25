#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''Simple movie script presenting one video,
video is interrrupted and replaced with an image after a button press
@author Cornelius Abel, Ilkay Isik
uses PsychoPy2 v1.85.2
'''
from __future__ import division
from psychopy import visual, core, event
import time, os

videopath = 'C:/Users/ilkay.isik/Video01.mp4'
if not os.path.exists(videopath):
    raise RuntimeError("Video File could not be found:" + videopath)
# Create the window to present the movie
PixW = 1280
PixH = 720
win = visual.Window(size=(PixW, PixH),
                    fullscr=True,
                    allowGUI=False,
                    color='black')

# Create your movie stim.
mov=visual.MovieStim3(win, videopath,
                  #size=(1440, 810), #HD
                  pos=[0, 0], flipVert=False,
                  flipHoriz=False,
                  loop=True,
                  noAudio=True)

pic=visual.ImageStim(win, image='Stimulus-V01.png')


running=True
while running:
    showcup=False
    # Check for action keys.....
    for key in event.getKeys():
        if key in ['escape', 'q']:
            win.close()
            core.quit()
        if key in ['space']:
            showcup=True

    if showcup:
        pic.draw()
        win.flip()
        core.wait(1)
    else:
        mov.draw()
        win.flip()


win.close()
core.quit()
