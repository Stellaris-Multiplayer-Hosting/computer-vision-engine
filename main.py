from tkinter import *
import cv2 as cv
from cv2 import ml_NormalBayesClassifier
import pyautogui as pt
from time import sleep
import keyboard
import random
import subprocess

#Opens Stellaris.... Siper spend two hours trying to figure this out with cv2 but you can just go to the dir and open it this way... much easier...

subprocess.Popen("C:\Program Files (x86)\Steam\steamapps\common\Stellaris\stellaris.exe")

## waits for the loadingscreen.

ready = input("Ready Siper?: ")
print("Here we go...")

def wait_for_loadingscreen():
    print("this function is running you just did something right.")
    position = pt.locateCenterOnScreen("assets\stellaris_main_menu.png", confidence=.80)

wait_for_loadingscreen()

    
def setting_up_lobby():   
    #goes to mp.
    print("M was pressed")
    pt.press("m")
    sleep(5)
    #Goes to host.
    print("N was pressed")
    pt.press("n")
    sleep(5)
    #Opens the lobby.
    print("Enter was pressed")
    pt.press("enter")
    sleep(5)

sleep(5)

setting_up_lobby()

