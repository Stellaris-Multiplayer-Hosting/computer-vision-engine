from tkinter import *
import cv2 as cv
from cv2 import ml_NormalBayesClassifier
from cv2 import threshold
import pyautogui as pt
from time import sleep
import keyboard
import random
import subprocess
import steamworks as sw
import pydirectinput as pyt
import pytesseract as pts

playersf_img = cv.imread("assets\westingstuff.png", cv.IMREAD_UNCHANGED)
players_img = cv.imread("assets\players.png", cv.IMREAD_UNCHANGED)

wafflefries = cv.matchTemplate(playersf_img, players_img, cv.TM_CCOEFF_NORMED)

cv.imshow('Result', wafflefries)



sleep(5000)


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

#def bot_messages():
 #   pyt.click(700, 815)
  #  pyt.typewrite("Hello and welcome to the game.")

def detect_players():
    #detects how many players are in the game 
    pts.image_to_boxes
    print("")

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
            print("I cannot locate stellaris main screen make sure to click on the application as well please wait 10 seconds.")
            sleep(10)

    sleep(3)
    setting_up_lobby()
    sleep(2)
#    bot_messages()


if __name__ == '__main__':
    main()
