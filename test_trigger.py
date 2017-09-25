'''Test the trigger via the parallel port'''

from psychopy import visual, parallel, core, logging, event
win = visual.Window(size=(800,600),
                    allowGUI=True, 
                    color='grey')

parallel.setPortAddress(address=0xCFE9)

text = visual.TextStim(win=win, #height=2, wrapWidth=50,
                       text='waiting for scanner...',
                       )

globalClock = core.Clock()
# begin the loop
start_trigger = True
while start_trigger:
    text.draw()
    win.flip()

    if parallel.readPin(13) == 1:
            start_trigger = False
    for keys in event.getKeys():
 
        if keys in ['5']:
            start_trigger = False

        elif keys[0] in ['escape', 'q']:
            win.close()
            core.quit()

globalClock.reset()
logging.exp('parallel trigger: start of scan')
win.flip()  # blank the screen on first sync pulse received