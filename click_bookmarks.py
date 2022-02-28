import pyautogui
from utils import wait_function


while True:
    try:
        pyautogui.click(563, 115)
        if wait_function(1, "q"):
            break
        pyautogui.click(660, 115)
        if wait_function(1, "q"):
            break

    except Exception as e:
        print()
        print('ERROR:')
        print(e)
        break
