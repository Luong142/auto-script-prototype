import pyautogui
import webbrowser


def register():
    current_pos = 0

    # open the web browser
    webbrowser.open_new_tab('https://www.facebook.com/register')

    # todo: move to register button and click on it on Facebook.
    pyautogui.moveTo(600, 820, 0.4)  # todo: the duration is to increase the time

    pyautogui.click()

    # todo: the difference between moveTo() and move() are one is forcing to move the cursor regardless of location

    name = "# Testing"

    pyautogui.typewrite(name, 0.5)  # todo: the interval how fast to type in the word.
