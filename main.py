from tkinter import *
import cv2 as cv
from cv2 import ml_NormalBayesClassifier
import pyautogui as pt
from time import sleep
import keyboard
import random
import subprocess
import steamworks as sw
import pydirectinput as pyt


def setting_up_lobby():  
    #testingstuff
    #goes to mp.
    print("M was pressed")
    pyt.press("m")
    sleep(1)
    #Goes to host.
    print("N was pressed")
    pyt.press("n")
    sleep(1)
    #Opens the lobby.
    print("Enter was pressed")
    pyt.press("enter")

def main():
    # use the steamworks library to open the game
    steam = sw.STEAMWORKS()
    steam.initialize()
    subprocess.Popen(f'{steam.Apps.GetAppInstallDir(281990)}/stellaris.exe')


##Looks for the image main_menu and loops until it is found.
    while 1:
        if pt.locateOnScreen("assets\stellaris_main_menu.png", confidence=.80) != None:
            print("Let's get this show on the road.")
            break
        else:
            print("I cannot locate stellaris main screen make sure to click on the application as well please wait 20 seconds.")
            sleep(20)

    print("Here we go...")
    sleep(3)
    setting_up_lobby()


if __name__ == '__main__':
    main()
