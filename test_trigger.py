'''Wait the trigger using parallel port input or keyboard press.
Use the response box from Cornelius to emulate signal'''

from psychopy import visual, parallel, core, event
from psychopy.parallel._inpout32 import PParallelInpOut32

port = PParallelInpOut32()
pin, expected_trigger = 13, 0

# Prepare the window and the stimuli
win = visual.Window(size=(800,600), allowGUI=True, color='grey')
text = visual.TextStim(win=win, text='waiting for scanner...')

# Begin the loop
start_trigger = True
global_clock = core.Clock()
while start_trigger:
    text.draw()
    win.flip()
    if port.readPin(pin) == expected_trigger:
        start_trigger = False

    for keys in event.getKeys():
        if keys in ['5']:
            start_trigger = False
        elif keys[0] in ['escape', 'q']:
            win.close()
            core.quit()

global_clock.reset()  # required for precise timing

# For testing purposes
text.text = 'I got the trigger'
text.draw()
win.flip()
