# Made with love [KanameS]

from pyautogui import *
import time

#
config_delaytime = 0.25

def longclick(button="left"):
    mouseDown(button=button)
    time.sleep(0.1)
    mouseUp(button=button)


while(True):
    x, y = position()
    moveTo(987, 547)
    click();
    longclick(button="right")
    time.sleep(config_delaytime)
    moveTo(870, 637)
    longclick(button="left")
    time.sleep(config_delaytime)
    moveTo(825, 601)
    longclick(button="left")
    time.sleep(config_delaytime)
    moveTo(899, 589)
    longclick(button="left")
    time.sleep(config_delaytime)



