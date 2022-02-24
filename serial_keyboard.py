import serial
import sys
import pyautogui
from pyautogui import press
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.001 # increase speed of keyboard
port = input("Enter port number: ") # Windows only.

ser = serial.Serial(port,9600,parity=serial.PARITY_EVEN) # for TRS-80 Model 100, set Stat 88E1E in TELCOM

while True:
    raw = ser.read()
    char = raw.decode('ascii')
    if int.from_bytes(raw, byteorder=sys.byteorder) == 13: # this is a Carriage Return - Windows doesn't like it
        char = 'enter'
    elif char == chr(27): # The user pressed Escape and wants to end the serial session
        break
    press(char)