from io import BytesIO

import pyautogui


def take_screenshot():
    image = pyautogui.screenshot()
    with BytesIO() as image_binary:
        image.save(image_binary, 'PNG')
        image_binary.seek(0)
        return image_binary.getvalue()
