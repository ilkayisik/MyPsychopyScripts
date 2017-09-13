from __future__ import division
from psychopy import visual, core, event
import os

win = visual.Window((1920, 1080))
mov = visual.MovieStim3(win, '/Users/ilkay.isik/Desktop/Matched_Stim/d_12.mp4', 
    size=(1280, 720),
    flipVert=False, 
    flipHoriz=False, 
    loop=False)


print('orig movie size=%s' % mov.size)
print('duration=%.2fs' % mov.duration)

globalClock = core.Clock()


while mov.status != visual.FINISHED:
    mov.draw()
    win.flip()
    if event.getKeys():
        break

win.close()
core.quit()
