from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as mb
import os
import random

root = Tk()
root.title("Welcome To PandoOS")
root.geometry("1020x500")
root.iconbitmap("img/logo.ico")
root.bind("<Escape>", lambda e: root.destroy())

# Ressources

class res(object):
    def __init__(res, arg):
        super(res, self).__init__()
        self.arg = arg
    boot = False
    version = "1.2"

# Boot (start)

def boot():
    if res.boot == False:
        res.boot = True
        session = open("sessions/sessions.PandoOS-session", "w+")
        session.write("session=user")
        session.close()
        mb.showinfo("PandoOS","Boot successful, press ENTER for continue.")
        root.destroy()
        os.system('cls')
        print("PandoOS> Boot...")
        print(f"PandoOS> Latest version: {res.version}")
        os.system('py PandoOS.py')
    else:
        os.system('exit')

# Run

res.boot = False

# UI

boot = Button(root, text="Boot PandoOS", command=boot)
boot.pack(anchor="center")
# boot.grid()

root.mainloop()
