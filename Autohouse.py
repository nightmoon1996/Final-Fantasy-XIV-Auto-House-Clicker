# Made with love [KanameS]

from pyautogui import *
import time

# just leave it 0.25 for now
config_delaytime = 0.25

def longclick(button="left"):
    mouseDown(button=button)
    time.sleep(0.1)
    mouseUp(button=button)


while(True):
    x, y = position()
    # Target middle of screen
    moveTo(987, 547)
    click();
    longclick(button="right")
    time.sleep(config_delaytime)
    # Buy button
    moveTo(870, 637)
    longclick(button="left")
    time.sleep(config_delaytime)
    # Free Comapny Button
    moveTo(825, 601)
    longclick(button="left")
    time.sleep(config_delaytime)
    # Yes/Confirm Button
    moveTo(899, 589)
    longclick(button="left")
    time.sleep(config_delaytime)



