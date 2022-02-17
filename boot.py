from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as mb
import os
import random

root = Tk()
root.title("Welcome To PandoOS")
root.geometry("300x100")
root.iconbitmap("img/logo.ico")
root.bind("<Escape>", lambda e: root.destroy())
root.resizable(False, False)
root.withdraw()

# Boot (start)

def boot():
    os.system('cls')
    mb.showinfo("PandoOS","Démarrage effectué, appuyez sur ENTRER pour continuer.")
    # root.destroy()
    os.system('cls')
    print("PandoOS> Lancement...")
    pandoos = "PandoOS.py"
    os.system(pandoos)

boot()

# UI

# Label(root, text="\n").pack()
# boot = Button(root, text="Boot PandoOS", command=boot, width=30)
# boot.pack(anchor='center')
# boot.grid()

# root.mainloop()
