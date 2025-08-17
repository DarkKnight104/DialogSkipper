from pynput import keyboard
from pynput.keyboard import Key, Listener, Controller
import pyautogui
import threading
import time
import random
import pygetwindow as gw
import json
from pathlib import Path
import math


kb = Controller()
dialog_flag = False
setting = Path(__file__).parent / "genshin.json"
Welcome="Genshin Dialogue Skipper is ready to Start\n" \
        "Press F8 to start and stop the program"
config = ''
x = 0
y = 0
def start():
    global config
    global x,y
    if setting.is_file():
        with open(setting, 'r') as f:
            config = json.load(f)
        x = config["X"]
        y = config["Y"]
        print(Welcome)
        main()
    else:
        x,y = find_hide_button()
        config = {"X": x, "Y": y}
        with open(setting, "w") as f:
            json.dump(config,f)
        print(Welcome)
        main()
def main():
    thread2 = threading.Thread(target=dialog_skipper, args=())
    thread2.start()

    with Listener(on_press=on_press) as listener:
        listener.join()
def find_hide_button():
    lenguage = int(input("Chose Lenguage\n1:English and French\n2:Simplified and Traditional Chinese\n3:Korean\n4:Japanese\n5:Spanish,Portugese and Italian\n6:Indonesian\n7:Russian\n8:German\n9:Thai\n10:Turkish\n11:Vietnamese\n"))
    if lenguage == 1: #English / French
        rel_pos_x = 280
    elif lenguage == 2: #Simplified Chinese / Traditional Chinese
        rel_pos_x = 270
    elif lenguage == 3:
        rel_pos_x = 268 # Korean
    elif lenguage == 4:
        rel_pos_x = 342 # Japanese
    elif lenguage == 5:
        rel_pos_x = 364 # Spanish / Portuguese / Italian
    elif lenguage == 6:
        rel_pos_x = 335 # Indonesian
    elif lenguage == 7:
        rel_pos_x = 283 # Russian
    elif lenguage == 8:
        rel_pos_x = 377 # German
    elif lenguage == 9:
        rel_pos_x = 225 # Thai
    elif lenguage == 10:
        rel_pos_x = 337 # Turkish
    elif lenguage == 11:
        rel_pos_x = 325 # Vietnamese
   
    screen_width,screen_height = pyautogui.size()
    x = math.floor((rel_pos_x * int(screen_width)) / 1920)
    y = math.floor((48 * int(screen_height)) / 1080)
    return x,y

def on_press(key):
    global dialog_flag
    try:
        if key == keyboard.Key.f8:
            dialog_flag = not dialog_flag
            if dialog_flag:
                print("ON")
            else:
                print("OFF")
    except AttributeError:
        pass
def in_dialog():
    global x,y,config
    if pyautogui.pixelMatchesColor(x,y,(59, 67, 84), tolerance=5):
            return True
    return False

def game_focused():
    window = gw.getActiveWindow()
    if window.title == "Genshin Impact" or "原神" or "원신" or "原神":
        return True
    print(window.title)
    return False

def text_skip():
    kb.press(Key.space)
    time.sleep(0.01)
    kb.release(Key.space)

def dialog_option():
    kb.press('f')
    time.sleep(0.01)
    kb.release('f')

def dialog_skipper():
    global dialog_flag
    while True:
        t = (random.randint(1,10))/100
        if dialog_flag and game_focused():
            if in_dialog():
                text_skip()
                dialog_option()            
        time.sleep(t)
        
start()              


