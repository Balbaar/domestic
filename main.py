from distutils import msvccompiler
import pytesseract as pt
from PIL import ImageGrab
import pyautogui
import keyboard
import time
import cv2
import numpy as np
import regex
import json

pt.tesseract_cmd = "C:\Program Files\Tesseract-OCR\tesseract.exe"

#JSON file
with open("config.json", "r") as f:
    cfg = json.loads(f.read())

#Info
math_region = (cfg["math_region"][0],cfg["math_region"][1],cfg["math_region"][2],cfg["math_region"][3])
white_from_box = (cfg["white_from_box"][0],cfg["white_from_box"][1],cfg["white_from_box"][2],cfg["white_from_box"][3])

ans_input = (cfg["ans_input"][0],cfg["ans_input"][1])
enter_button = (cfg["enter_button"][0],cfg["enter_button"][1])
sign_button =(cfg["sign_button"][0],cfg["sign_button"][1])

work1 = (cfg["work1"][0],cfg["work1"][1]) #Domestor
work2 = (cfg["work2"][0],cfg["work2"][1]) #Workers




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


def start_work():
    pyautogui.leftClick(work1)
    time.sleep(5)
    pyautogui.leftClick(work2)


def start_bot():
    time.sleep(5)

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

    if avg_color[0] > 200:
        process_and_sign()
    
    time.sleep(10)
    start_work()
