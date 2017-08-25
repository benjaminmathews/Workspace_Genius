"""
Python Script for Workspace Genius
Version         : 1.0.1
Date Created    : 24-08-2017
Last Modified   : 26-08-2017
Auhor           : Benjamin Mathews Abraham
Online Repo     : https://bitbucket.org/codeinator/workspace_genius
"""
from Tkinter import *
import json
import os
import time

# Open the config JSON file
with open('workspace_config.json') as data_file:    
    data = json.load(data_file)

root = Tk()
root.title("Workspace Genius")

w = 500 # width for the Tk root
h = 650 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))


def btn_cb(p):
    """
    Button Callback function
    Parameter : p (project name)
    """
    p_name = data[p]["PROJECT_NAME"]
    p_path = data[p]["PROJECT_PATH"]
    p_url = data[p]["LIVE_URL"]
    p_vsc = data[p]["VSCODE_PATH"]
    p_cmd = data[p]["CMD_PATH"]
    p_scp = data[p]["WINSCP_URL"]
    p_putty = data[p]["PUTTY_SESSION"]

    # Open cmd at CMD_PATH, and run Django development server
    if(localFlag.get()):
        os.system("start cmd /k \"C: && cd " + str(p_cmd) + " && python manage.py runserver\"")
    
    # Open Microsoft Visual Studio Code at VSCODE_PATH
    os.system("code " + str(p_vsc))
    
    # If "live" is checked,
    if(liveFlag.get()):
        
        # Start File Explorer at PROJECT_PATH
        os.system("start " + str(p_path))

        # Start Microsoft Edge browser at LIVE_URL
        os.system("start microsoft-edge:" + str(p_url))

        # Start WinSCP session at WINSCP_URL
        os.system("start \"C:\Program Files (x86)\WinSCP\winscp.exe\" " + str(p_scp) + " /newinstance")

        # Start PuTTY session at PUTTY_SESSION
        os.system("start D:\PuTTY\putty -load " + str(p_putty))
    if(localFlag.get()):
        
        time.sleep(5)
        # Start Microsoft Edge browser at localhost and port 8000 (Django development server default)
        os.system("start microsoft-edge:http://localhost:8000")


buttons = {}

for project in data:
    p_name = data[project]["PROJECT_NAME"]
    
    # Create buttons and assign callback
    buttons[p_name] = Button(root, text=p_name, height=10, width=50)
    buttons[p_name].configure(command=lambda widget=p_name: btn_cb(widget))
    buttons[p_name].pack()

# Create Checkboxes
liveFlag = IntVar()
liveCheck = Checkbutton(root, text="Live", variable=liveFlag)
localFlag = IntVar()
localCheck = Checkbutton(root, text="Local", variable=localFlag)
liveCheck.pack()
localCheck.pack()
localCheck.select()

# Start GUI
root.mainloop()
