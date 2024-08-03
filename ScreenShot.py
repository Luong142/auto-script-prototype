import pyautogui
import webbrowser
import time


def screenShot():
    webbrowser.open_new('https://www.facebook.com/register')

    # delay for this to take screenshot
    time.sleep(1.8)
    firstNameShot = pyautogui.screenshot("firstName.png", region=(930, 560, 360, 80))

    # todo: start from here if we want to continue.
    surNameShot = pyautogui.screenshot("surname.png", region=(1500, 560, 360, 80))

