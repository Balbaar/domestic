from distutils import msvccompiler
import pytesseract as pt
from PIL import ImageGrab
import pyautogui
import keyboard
import time
import cv2
import numpy as np
import regex

pt.tesseract_cmd = "C:\Program Files\Tesseract-OCR\tesseract.exe"


#Info
math_region = (528,412,584,435)
white_from_box = (625,572,653,587)

ans_input = (663,467)
enter_button = (669,535)
sign_button =(1264,557)

work1 = (789,252) #Domestor
work2 = (157,719) #Workers

#Math Problem To Solve
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
    print(ms)

    while "+" not in str(ms) or regex.search("[a-zA-Z]", ms):
        print("Unable to read or string contained alphabet")
        reload_page()
        time.sleep(1)

        #Grab the new math problem
        ms = math_to_string()
    
    return ms

def process_and_sign():
    #Process string
    ms_numbers = (grab_and_solve().split("+"))

    #Calulate answer and if string contains something weird redo previus steps
    #try:
    ans = int(ms_numbers[0]) + int(ms_numbers[1])

    #except:
    grab_and_solve()

    #Answer is more than lileky wrong in this case
    if ans > 40:
        grab_and_solve()
    print(ans)

    #Type answer into input box
    pyautogui.leftClick(ans_input)
    for x in str(ans):
        time.sleep(0.3)
        pyautogui.press(f"{x}")
    time.sleep(0.5)

    #Sign in using wallet
    pyautogui.leftClick(enter_button)
    time.sleep(8)
    pyautogui.leftClick(sign_button)

process_and_sign()

def start_work():
    pyautogui.leftClick(work1)
    time.sleep(5)
    pyautogui.leftClick(work2)

time.sleep(5)

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
    
    time.sleep(10)
    start_work()
    time.sleep(610)
