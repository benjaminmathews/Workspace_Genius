"""
Python Script for Workspace Genius
Version        : 1.0.0
Date Created   : 24-08-2017
Auhor          : Benjamin Mathews Abraham
Online Repo    : https://bitbucket.org/codeinator/workspace_genius
"""
from Tkinter import *
import json
import os
import time

with open('workspace_config.json') as data_file:    
    data = json.load(data_file)

button = {}

root = Tk()
root.title("Workspace Launcher")

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
    p_name = data[p]["PROJECT_NAME"]
    p_path = data[p]["PROJECT_PATH"]
    p_url = data[p]["LIVE_URL"]
    p_vsc = data[p]["VSCODE_PATH"]
    p_cmd = data[p]["CMD_PATH"]
    p_scp = data[p]["WINSCP_URL"]
    p_putty = data[p]["PUTTY_SESSION"]
    print p_name
    os.system("code " + str(p_vsc))
    os.system("start cmd /k \"C: && cd " + str(p_cmd) + " && python manage.py runserver\"")
    # os.system("powershell -Command \"Start-Process cmd -Verb RunAs\"")
    print liveFlag.get()
    print localFlag.get()
    if(liveFlag.get()):
        os.system("start microsoft-edge:" + str(p_url))
        os.system("start \"C:\Program Files (x86)\WinSCP\winscp.exe\" " + str(p_scp) + " /newinstance")
        os.system("start D:\PuTTY\putty -load " + str(p_putty))
    if(localFlag.get()):
        time.sleep(5)
        os.system("start microsoft-edge:http://localhost:8000")

for project in data:
    p_name = data[project]["PROJECT_NAME"]
    
    button[p_name] = Button(root, text=p_name, height=10, width=50)
    button[p_name].configure(command=lambda widget=p_name: btn_cb(widget))
    button[p_name].pack()

liveFlag = IntVar()
liveCheck = Checkbutton(root, text="Live", variable=liveFlag)
localFlag = IntVar()
localCheck = Checkbutton(root, text="Local", variable=localFlag)
liveCheck.pack()
localCheck.pack()
localCheck.select()
root.mainloop()
