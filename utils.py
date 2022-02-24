import time
import keyboard
import pyautogui


def wait_function(wait_time, pressed_key):
    for i in range(int(wait_time / 0.05)):
        if keyboard.is_pressed(pressed_key):
            return True
        time.sleep(0.05)

    return False

def clear_input(times):
    for i in range(times):
        pyautogui.write('\b')


