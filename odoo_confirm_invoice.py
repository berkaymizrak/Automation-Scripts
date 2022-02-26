import pyautogui
from utils import wait_function


count = 0
while True:
    count += 1
    print('Clicking times: %s' % count)
    try:
        pyautogui.click(322, 300)
        if wait_function(1, "q"):
            break
        pyautogui.click(1411, 247)
        if wait_function(1, "q"):
            break

        if count >= 70:
            pyautogui.click(303, 211)  # invoices button
            if wait_function(1, "q"):
                break
            pyautogui.click(457, 354)  # first invoice item
            if wait_function(1, "q"):
                break
            count = 0
    except Exception as e:
        print()
        print('ERROR:')
        print(e)
        break
