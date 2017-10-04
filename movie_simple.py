from __future__ import division
from psychopy import visual, core, event
import os

win = visual.Window((1920, 1080))
mov = visual.MovieStim3(win, '/Volumes/Projekte/2016-0065-vesfmri1/Stimuli/Orig_movies/BluerayMovies/SAMSARA/Samsara_1280x720.m4v', #'/Volumes/Projekte/2016-0065-vesfmri1/Movie_Pilot/Beh_Pilot_04/stimuli/d_01.mp4', 
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
