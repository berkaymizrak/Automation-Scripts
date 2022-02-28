import pyautogui
import time
from utils import wait_function


while True:
    xx, yy = pyautogui.position()
    print(xx, yy)
    if wait_function(1, "p"):
        print('Paused! Waiting for 10 second.')
        time.sleep(10)
