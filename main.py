from tkinter import *
import cv2
import pyautogui as pt
from time import sleep
import keyboard
import random
import subprocess

#Opens Stellaris.... Siper spend two hours trying to figure this out with cv2 but you can just go to the dir and open it this way... much easier...

subprocess.Popen("C:\Program Files (x86)\Steam\steamapps\common\Stellaris\stellaris.exe")

## waits for the loadingscreen.
def wait_for_loadingscreen():
    print("this function is running you just did something right.")
    position = pt.locateCenterOnScreen("assets\stellaris_main_menu.png", confidence=.80)
   

    
def setting_up_lobby(key_press, duration, action='starting_mp_game'): 
    pt.keyDown(key_press)   
    #goes to mp.
    print("M was pressed")
    pt.keyDown("m")
    pt.keyUp("m")
    sleep(5)
    #Goes to host.
    print("N was pressed")
    pt.keyDown("n")
    pt.keyUp("n")
    sleep(5)
    #Opens the lobby.
    print("Enter was pressed")
    pt.keyDown("enter")
    pt.keyUp("enter")
    sleep(5)

wait_for_loadingscreen()

sleep(5)

setting_up_lobby()
