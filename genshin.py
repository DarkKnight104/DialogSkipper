from pynput import keyboard
from pynput.keyboard import Key, Listener, Controller
import pyautogui
import threading
import time
import random
import pygetwindow as gw
import json
from pathlib import Path


kb = Controller()
dialog_flag = False
setting = Path(__file__).parent / "genshin.json"
Welcome="Genshin Dialogue Skipper is ready to Start\n" \
        "Press F8 to start and stop the program"

def start():
    if setting.is_file():
        print(Welcome)
        main()
    else:
        config = {"lenguage": 0, "screensize":0}
        config["screensize"] = input("Chose Screen Size\n 1:1920x1080\n")
        config["lenguage"] = input("Chose Lenguage\n1:English\n2:Italian\n")
        with open(setting, "w") as f:
            json.dump(config,f)
        print(Welcome)
        main()


def main():
    thread2 = threading.Thread(target=dialog_skipper, args=())
    thread2.start()

    with Listener(on_press=on_press) as listener:
        listener.join()

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
    global lenguage
    if lenguage == 2:
        if pyautogui.pixelMatchesColor(364,47,(59, 67, 84), tolerance=5):
            #print("In Dialog Ita")
            return True
        #print("Not Dialog Ita")
        return False
    elif lenguage == 1:
        if pyautogui.pixelMatchesColor(280,48,(59, 67, 84), tolerance=5):
            #print("In Dialog Eng")
            return True
        #print("Not Dialog Eng")
        return False

def game_focused():
    if gw.getActiveWindowTitle() == "Genshin Impact":
        return True
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
        t = (random.randint(1,50))/100
        if dialog_flag and game_focused():
            if in_dialog():
                text_skip()
                dialog_option()            
        time.sleep(t)
        
start()              


