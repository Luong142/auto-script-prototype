import pyautogui
import random

def register():
    # todo: a list to key in first name and last name in facebook.
    global firstnamesPos
    firstnames = [
        "Ha", "Nguyen", "TRAN", "Le", "Pham", "Vu", "Ho", "Do",
        "Thi", "Anh", "Khai", "Quang", "Duy", "Tung", "Minh", "Hieu",
        "Tuan", "Tam", "Lu", "Viet", "Long", "Bao", "Nam", "Huy",
        "Thanh", "Tu", "Manh", "Hung", "Cuong", "Dang", "Khoa", "Son"
    ]

    surnames = [
        "Nguyen", "Tran", "Le", "Pham", "Vo", "Huynh", "Dang", "Duong",
        "Dao", "Nguyet", "Ngo", "La", "Chau", "Ha", "Vu", "Thi", "Anh",
        "Khai", "Quang", "Duy", "Tung", "Minh", "Hieu", "Tuann", "Tam",
        "Lu", "Viet", "Long", "Bao", "Nam", "Huy", "Thanh", "Tu", "Manh",
        "Hung", "Cuong", "Dang", "Khoa", "Son"
    ]

    # open the web browser
    # webbrowser.open_new_tab('https://www.facebook.com/register')

    # todo: move to register button and click on it on Facebook.    firstnamesPos = None
    '''
        try:
        x, y = pyautogui.locateCenterOnScreen(
            'firstName.png')

        if x and y:
            print(f"\nFound {x}, {y}")
        else:
            print("\n Not found.")

    except Exception as e:
        print(f"Failed to locate first name input field: {e}")
    '''

    # todo: the difference between moveTo() and move() are one is forcing to move the cursor regardless of location

