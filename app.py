import cv2
import pyautogui
import pytesseract
import numpy as np
import random
import time
from PIL import ImageGrab
import pygetwindow as gw

# path to tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def find_image_on_screen(image, region):
    screenshot = pyautogui.screenshot(region=region)
    img_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.7
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        return pt[0] + w / 2, pt[1] + h / 2
    return None


def get_health_value(region):
    screenshot = pyautogui.screenshot(region=region)
    text = pytesseract.image_to_string(screenshot)
    health = ''.join(filter(str.isdigit, text))
    return int(health) if health else None


def press_random_key():
    random_key = random.choice(['a', 's', 'd'])
    pyautogui.keyDown(random_key)
    time.sleep(1)
    pyautogui.keyUp(random_key)


def main():
    window_title = 'Wizard101'
    window = gw.getWindowsWithTitle(window_title)[0]
    window.activate()

    # coordinates for the region where the health value is displayed, I got mine using SHARE X tool.
    health_region = (224, 818, 366, 918)

    while True:
        # Player movement
        pyautogui.keyDown('w')
        time.sleep(2)
        pyautogui.keyUp('w')
        press_random_key()

        if find_image_on_screen('verify.png', region=(window.left, window.top, window.width, window.height)):
            health = get_health_value(health_region)
            print(f"Current health: {health}")
            for _ in range(2):  # Repeat twice
                if health and health < 7500:
                    # Find and click PIXIE card
                    pixie_location = find_image_on_screen('pixie.png', region=(
                        window.left, window.top, window.width, window.height))
                    if pixie_location:
                        pyautogui.click(pixie_location)
                        print("Cast pixie spell")
                else:
                    # Find and click EPIC card
                    epic_location = find_image_on_screen('epic.png', region=(
                        window.left, window.top, window.width, window.height))
                    if epic_location:
                        pyautogui.click(epic_location)
                        print("Cast epic spell")

                    # Find and click SANDSTORM card/ replace just sandstorm.png with tempest/meteor or whatever your aoe spell is. Just replace the image not the code.
                    sandstorm_location = find_image_on_screen('sandstorm.png', region=(
                        window.left, window.top, window.width, window.height))
                    if sandstorm_location:
                        pyautogui.click(sandstorm_location)
                        print("Cast sandstorm spell")


if __name__ == "__main__":
    main()
