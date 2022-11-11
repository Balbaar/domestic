import PySimpleGUI as pg
import json
import pyautogui as pag
import time
import threading
from main import *

# PySimpleGUI
pg.theme("DarkTeal4")

layout = [
    [pg.Text("Punkter På Skärmen")],
    [pg.Button("Matte Vänster Uppe")],
    [pg.Button("Vitt Från Matte")],
    [pg.Button("Svars Ruta")],
    [pg.Button("Svara Knapp")],
    [pg.Button("Metamask Sign Knapp")],
    [pg.Button("Start Domestor")],
    [pg.Button("Start Workers")],
    
    [pg.Text("Starta & Stoppa Domestic Bot")],
    [pg.Button("Start")],
    [pg.Button("Stop")]
]

window = pg.Window("Domestic Automatic Worker", layout, size=(300, 400))


#Open JSON config file
with open("config.json", "r") as f:
    config_file = json.loads(f.read())

def start():
    while True:
        if stop_thread == True:
            print("Stopped Bot")
            break
        print("Started Bot")
        start_bot()
        print("Bot Finished")
        print("Waiting 10min")
        time.sleep(610)


while True:
    event, values = window.read()
    if event == pg.WINDOW_CLOSED:
        break
    if event == "Matte Vänster Uppe":
        time.sleep(5)
        current_pos = pag.position()
        config_file["math_region"] = [current_pos[0], current_pos[1], current_pos[0] + 60, current_pos[1] + 25]
        new_config_file = json.dumps(config_file, indent=3)
        with open("config.json", "w") as f:
            f.write(new_config_file)
    
    if event == "Vitt Från Matte":
        time.sleep(5)
        current_pos = pag.position()
        config_file["white_from_box"] = [current_pos[0], current_pos[1], current_pos[0] + 30, current_pos[1] + 30]
        new_config_file = json.dumps(config_file, indent=3)
        with open("config.json", "w") as f:
            f.write(new_config_file)
    
    if event == "Svars Ruta":
        time.sleep(5)
        current_pos = pag.position()
        config_file["ans_input"] = [current_pos[0], current_pos[1]]
        new_config_file = json.dumps(config_file, indent=3)
        with open("config.json", "w") as f:
            f.write(new_config_file)
    
    if event == "Svara Knapp":
        time.sleep(5)
        current_pos = pag.position()
        config_file["enter_button"] = [current_pos[0], current_pos[1]]
        new_config_file = json.dumps(config_file, indent=3)
        with open("config.json", "w") as f:
            f.write(new_config_file)
    
    if event == "Metamask Sign Knapp":
        time.sleep(5)
        current_pos = pag.position()
        config_file["sign_button"] = [current_pos[0], current_pos[1]]
        new_config_file = json.dumps(config_file, indent=3)
        with open("config.json", "w") as f:
            f.write(new_config_file)

    if event == "Start Domestor":
        time.sleep(5)
        current_pos = pag.position()
        config_file["work1"] = [current_pos[0], current_pos[1]]
        new_config_file = json.dumps(config_file, indent=3)
        with open("config.json", "w") as f:
            f.write(new_config_file)

    if event == "Start Workers":
        time.sleep(5)
        current_pos = pag.position()
        config_file["work2"] = [current_pos[0], current_pos[1]]
        new_config_file = json.dumps(config_file, indent=3)
        with open("config.json", "w") as f:
            f.write(new_config_file)

    if event == "Start":
        stop_thread = False
        start_bot_thread = threading.Thread(target=start)
        start_bot_thread.start()
        if stop_thread == True:
            start_bot_thread.join()

        
    
    if event == "Stop":
        stop_thread = True
        
        




window.close()
exit()
