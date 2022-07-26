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
    sleep(3)
    pyt.leftClick(1450, 850)


def wait_for_loadingscreen():
    print("this function is running you just did something right.")
    position = pt.locateCenterOnScreen("assets\stellaris_main_menu.png", confidence=.80)


def main():
    # use the steamworks library to open the game
    steam = sw.STEAMWORKS()
    steam.initialize()
    subprocess.Popen(f'{steam.Apps.GetAppInstallDir(281990)}/stellaris.exe')

    ## waits for the loadingscreen.

    ready = input("Ready Siper?: ")
    print("Here we go...")
    sleep(3)
    wait_for_loadingscreen()
    setting_up_lobby()


if __name__ == '__main__':
    main()
