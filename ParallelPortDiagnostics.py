# -*- coding: utf-8 -*-
'''Test the trigger via the parallel port and keyboard press'''

from psychopy import visual, parallel, core, event
from psychopy.parallel._inpout32 import PParallelInpOut32

win = visual.Window(size=(800,600), allowGUI=True, color='grey')
instruction = visual.TextStim(win=win, pos=(0, -0.8), height=0.05,
text='- Use keyboard buttons 2-9 to change output pins.\n- Press q to quit.')
instruction.setAutoDraw(True)
text_1 = visual.TextStim(win=win, height=0.1, font='Monospace')
text_2 = visual.TextStim(win=win, pos=(0, -0.2), height=0.1)
port = PParallelInpOut32()

def ReadPins():
    """Read selected pins from parallel port."""
    out = '|'
    selected_pins = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    for pin in selected_pins:
        out += str(port.readPin(pin))  + '|' #read the pin value - 0 or 1
    return out


# begin the loop
loop_switch = True
while loop_switch:
    text_1.text = ReadPins()
    text_1.draw()
    text_2.text = '8-bit data: ' + str(port.readData())  #read the combined data from the input pins
    text_2.draw()
    win.flip()
    for keys in event.getKeys():
        if keys[0] in ['escape', 'q']:  # quit
            loop_switch = False
        elif keys[0] in ['2']:
            port.setPin(2, (port.readPin(2) + 1) % 2)# add one each time the button is pressed
        elif keys[0] in ['3']:
            port.setPin(3, (port.readPin(3) + 1) % 2)
        elif keys[0] in ['4']:
            port.setPin(4, (port.readPin(4) + 1) % 2)
        elif keys[0] in ['5']:
            port.setPin(5, (port.readPin(5) + 1) % 2)
        elif keys[0] in ['6']:
            port.setPin(6, (port.readPin(6) + 1) % 2)
        elif keys[0] in ['7']:
            port.setPin(7, (port.readPin(7) + 1) % 2)
        elif keys[0] in ['8']:
            port.setPin(8, (port.readPin(8) + 1) % 2)
        elif keys[0] in ['9']:
            port.setPin(9, (port.readPin(9) + 1) % 2)
