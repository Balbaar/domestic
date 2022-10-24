import pytesseract as pt
from PIL import ImageGrab
import pyautogui
import keyboard
import time
import cv2
import numpy as np

pt.tesseract_cmd = "C:\Program Files\Tesseract-OCR\tesseract.exe"

#Math Problem To Solve
math_region = (1070,777,1165,805)
white_from_box = (1263,483,1270,490)

def reload_page():
    pyautogui.keyDown("ctrl")
    pyautogui.press("r")
    pyautogui.keyUp("ctrl")

def grab_and_solve():
    def math_to_string():
        #Grab region
        math_problem = ImageGrab.grab(math_region)
        math_problem.save("math_problem.png")

        #OCR Image to string
        math_string = pt.image_to_string("math_problem.png")
        return math_string

    ms = math_to_string()

    while "+" not in str(ms):
        print("Unable to read")
        reload_page()
        time.sleep(1)

        #Grab the new math problem
        ms = math_to_string()
    
    return ms

def process_and_sign():
    #Process string
    ms_numbers = (grab_and_solve().split("+"))
    ans = int(ms_numbers[0]) + int(ms_numbers[1])

    #Answer is more than lileky wrong in this case
    if ans > 40:
        grab_and_solve()
    print(ans)

    #Type answer into input box
    pyautogui.leftClick(1250,850)
    for x in str(ans):
        time.sleep(0.3)
        pyautogui.press(f"{x}")
    time.sleep(0.5)

    #Sign in using wallet
    pyautogui.leftClick(1250,940)
    time.sleep(6)
    pyautogui.leftClick(2450,550)

process_and_sign()

def start_work():
    pyautogui.leftClick(1750,426)
    time.sleep(0.5)
    pyautogui.leftClick(1335,921)


while True:
    reload_page()
    time.sleep(2)
    #Check to see if robot check comes up

    #Grab image
    capture = ImageGrab.grab(white_from_box)
    capture.save("cap_check.png")
    cap_check = cv2.imread("cap_check.png")

    #Check for color white
    temp = np.average(cap_check, axis=0)
    avg_color = np.average(temp, axis=0)
    print(avg_color)

    if avg_color[0] == 255:
        process_and_sign()
    
    time.sleep(610)
    start_work()
