'''Wait the trigger using parallel port input or keyboard press.

Use the response box from Cornelius to emulate signal.
'''

from psychopy import visual, parallel, core, event

# Does the computer have a parallel port (True or False)
parallel_port = False

if parallel_port:  # this solution is for windows machines
    from psychopy.parallel._inpout32 import PParallelInpOut32
    port = PParallelInpOut32()
    # Parallel port related parameters
    pin = 13
    expected_trigger = 0  # can be 0 or 1

# Prepare the window and the stimuli
win = visual.Window(size=(800,600), allowGUI=True, color='grey')
text = visual.TextStim(win=win, text='waiting for scanner...')

# Begin the loop
start_trigger = True
global_clock = core.Clock()
while start_trigger:
    text.draw()
    win.flip()

    if parallel_port and port.readPin(pin) == expected_trigger:
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
