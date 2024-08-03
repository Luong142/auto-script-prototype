# todo day la comment, comment la su dung de ghi chu
import pyautogui
import random


def testingAutoPyGui():
    firstnames = [
        "Ha", "Nguyen", "TRAN", "Le", "Pham", "Vu", "Ho", "Do",
        "Thi", "Anh", "Khai", "Quang", "Duy", "Tung", "Minh", "Hieu",
        "Tuan", "Tam", "Lu", "Viet", "Long", "Bao", "Nam", "Huy",
        "Thanh", "Tu", "Manh", "Hung", "Cuong", "Dang", "Khoa", "Son"
    ]

    randomFirstNames = random.choice(firstnames)

    pyautogui.moveTo(600, 820, 0.4)  # todo: the duration is to increase the time
    print(f"\nThe first name decided for the registration is {randomFirstNames}")

    pyautogui.click()
    pyautogui.typewrite(randomFirstNames, 0.3)  # todo: the interval how fast to type in the word.





