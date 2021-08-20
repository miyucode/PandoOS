from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from time import *
from time import strftime
from subprocess import Popen, PIPE
import numpy as np
import cv2
import tkinter.messagebox as mb
import os
import platform

# Folder verification

try:
    os.mkdir("root/Desktop")
except FileExistsError:
    # if "Desktop/" already exist
    pass

# UI Config

PandoOS = Tk()
PandoOS.title("PandoOS")
PandoOS.geometry("1000x500")
PandoOS.iconbitmap("img/logo.ico")
PandoOS.minsize(1000, 500)
PandoOS.maxsize(1000, 500)
PandoOS.bind('<Escape>', lambda e: shutdown())
PandoOS.config(bg="white")

# --> App(s) and Tool(s)

def notepad():
    def savefile():
        i = l.get()
        if i == "":
            npgui.destroy()
            mb.showerror("PandoPad","Merci d'entrer un nom correct pour votre fichier !")
            notepad()
        else:
            t = text.get("1.0", "end-1c")
            npgui.destroy()
            confirmation3 = Toplevel()
            confirmation3.title("PandoPad - Attention !")
            confirmation3.geometry("300x100")
            confirmation3.resizable(False, False)
            confirmation3.iconbitmap("img/warning.ico")

            def yes():
                confirmation3.destroy()
                def requesttextfile():
                    foldername = folderName.get()
                    m.destroy()
                    if foldername == "":
                        mb.showerror("PandoPad","Entrez un nom correct d'un dossier existant ou non !")
                        yes()
                    else:
                        try:
                            os.mkdir("root/Desktop/" + foldername)
                            file = open("root/Desktop/" + foldername + "/" + i, "w+")
                            file.write(t)
                            file.close()
                            mb.showinfo("PandoPad","Vous avez créer un fichier texte avec succès !")
                        except FileExistsError:
                            # directory already exists
                            file = open("root/Desktop/" + foldername + "/" + i, "w+")
                            file.write(t)
                            file.close()
                            mb.showinfo("PandoPad","Vous avez créer un fichier texte avec succès !")

                m = Toplevel()
                m.title("PandoPad - Information")
                m.geometry("300x100")
                m.resizable(False, False)
                m.iconbitmap("img/warning.ico")

                Label(m, text="Entrez le nom du dossier:").pack()

                folderName = Entry(m)
                folderName.pack()

                Button(m, text="Continuer", command=requesttextfile).pack()

            def no():
                confirmation3.destroy()
                file = open('root/Desktop/' + i, 'w+')
                file.write(t)
                file.close()
                mb.showinfo("PandoPad","Vous avez créer un fichier texte avec succès !")
                

            Label(confirmation3, text="Souhaitez-vous le sauvegarder \ndans un dossier en particulier ?").pack()
            Button(confirmation3, text="Oui.", command=yes).pack()
            Button(confirmation3, text="Non.", command=no).pack()


    npgui = Toplevel()
    npgui.title('PandoPad')
    npgui.geometry('850x500')
    npgui.resizable(False, False)
    npgui.iconbitmap('img/notepad-icon.ico')
    text = Text(npgui)
    text.pack()
    Label(npgui, text="Donnez un nom au fichier:").pack()
    l = Entry(npgui)
    l.pack()
    button = Button(npgui, text="Créer le fichier texte", command=savefile)
    button.pack()

def clock():
    clockapp = Toplevel()
    clockapp.title("PandoOS - Horloge")
    clockapp.maxsize(450, 120)
    clockapp.minsize(450, 120)
    clockapp.geometry("300x200")
    clockapp.iconbitmap("img/information.ico")

    def time():
        string=strftime('%H:%M:%S')
        label.config(text=string)
        label.after(1000,time)

    label = Label(clockapp, font=('arial', 80))
    label.pack(anchor='center')
    time()

def fileexplorer():
    def openfile():
        fe.destroy()
        FileRequest1.pack_forget()
        FileRequest2.pack_forget()
        Name.pack_forget()
        # print("Alerte> Si un message bizarre apparaît ici, cela est normal et si il ne s'affiche pas, ignorer cet alerte.")
        file = filedialog.askopenfilename(title="Sélectionner un fichier", initialdir="C:/Users/")
        if file == "":
            mb.showerror("PandoOS","Vous avez sélectionner aucun fichier à lancer !")
            fileexplorer()
        else:
            mb.showinfo('PandoOS','Vous avez ouvert avec succès "' + file + '" !')
            os.system(f"start {file}")
            fileexplorer()

    # (Func) Create Folder

    def folder():
        Name.pack()
        FileRequest2.pack()
        FileRequest1.pack_forget()
        # print("Alerte> Si un message bizarre apparaît ici, cela est normal et si il ne s'affiche pas, ignorer cet alerte.")

    def createFolder():
        name = Name.get()
        fe.destroy()
        if name == "default" or name == "":
            mb.showerror("PandoOS","Veuillez donner un nom correct à votre dossier !")
        else:
            def yes():
                def requestfolder():
                    folder = nameoffolder.get()
                    d.destroy()
                    if folder == "":
                        mb.showerror("PandoOS","Rentrer le nom du dossier correctement !")
                        yes()
                    else:
                        try:
                            os.mkdir(f"root/Desktop/{folder}")
                            os.mkdir(f"root/Desktop/{folder}/{name}")
                            mb.showinfo("PandoOS","Dossier crée avec succès !")
                        except FileExistsError:
                            # os.mkdir(f"root/Desktop/{name}/{folder}")
                            os.mkdir(f"root/Desktop/{folder}/{name}")
                            mb.showinfo("PandoOS","Dossier crée avec succès !")

                confirmation4.destroy()
                d = Toplevel()
                d.title("PandoOS - Information")
                d.geometry("300x100")
                d.resizable(False, False)
                d.iconbitmap("img/warning.ico")
                Label(d, text="Entrez le nom du dossier:").pack()
                nameoffolder = Entry(d)
                nameoffolder.pack()
                Button(d, text="Continuer", command=requestfolder).pack()

            def no():
                confirmation4.destroy()
                os.mkdir(f"root/Desktop/{name}")
                fe.destroy()
                mb.showinfo("PandoOS","Dossier crée avec succès !")

            # userprofile = os.system('%userprofile%')
            # print('PandoOS> %userprofile% not found.')
            confirmation4 = Toplevel()
            confirmation4.title("PandoOS - Attention !")
            confirmation4.geometry("300x100")
            confirmation4.resizable(False, False)
            confirmation4.iconbitmap("img/warning.ico")
            Label(confirmation4, text="Souhaitez-vous le créer dans un dossier en particulier ?").pack()
            Button(confirmation4, text="Oui.", command=yes).pack()
            Button(confirmation4, text="Non.", command=no).pack()

            # os.system('cls')
            # name = Name.get()
            # os.mkdir(f"root/Desktop/{name}")
            # fe.destroy()
            # mb.showinfo("PandoOS","Dossier crée avec succès !")

    def RequestFolder():
        createFolder()

    # (Func) Create File

    def file():
        Name.pack()
        FileRequest1.pack()
        FileRequest2.pack_forget()
        # print("Alerte> Si un message bizarre apparaît ici, cela est normal et si il ne s'affiche pas, ignorer cet alerte.")

    def createFile():
        name = Name.get()
        if name == "":
            mb.showerror("PandoOS","Veuillez donner un nom à votre fichier !")
        else:

            # --> Button "Oui"

            def yes():
                def requestfilewithfolder():
                    nameFolder = namefolder.get()
                    confirmation2.destroy()
                    if nameFolder == "":
                        mb.showerror("PandoOS","Entrez un nom correct d'un dossier existant ou non !")
                        yes()
                    else:
                        try:
                            os.mkdir("root/Desktop/" + nameFolder)
                            file = open("root/Desktop/" + nameFolder + "/" + name, 'w+')
                            file.write(".")
                            file.close()
                            mb.showinfo("PandoOS","Fichier crée avec succès !")
                        except FileExistsError:
                            # directory already exists
                            file = open("root/Desktop/" + nameFolder + "/" + name, 'w+')
                            file.write(".")
                            file.close()
                            mb.showinfo("PandoOS","Fichier crée avec succès !")
                confirmation.destroy()
                fe.destroy()
                confirmation2 = Toplevel()
                confirmation2.maxsize(300, 100)
                confirmation2.minsize(300, 100)
                confirmation2.title("PandoOS - Information")
                confirmation2.iconbitmap("img/warning.ico")
                Label(confirmation2, text="Entrez le nom du dossier:").pack()
                namefolder = Entry(confirmation2, text="")
                namefolder.pack()
                Button(confirmation2, text="Continuer", command=requestfilewithfolder).pack()

            # <-- end
            # --------------------- #
            # --> Button "Non"

            def no():
                file = open("root/Desktop/" + name, 'w+')
                file.write("*")
                file.close()
                confirmation.destroy()
                mb.showinfo("PandoOS","Fichier crée avec succès !")

            # <-- end

            fe.destroy()
            confirmation = Toplevel()
            confirmation.maxsize(300, 100)
            confirmation.minsize(300, 100)
            confirmation.title("PandoOS - Attention !")
            confirmation.iconbitmap("img/warning.ico")
            Label(confirmation, text="Souhaitez-vous le sauvegarder \ndans un dossier en particulier ?").pack()
            Button(confirmation, text="Oui.", command=yes).pack()
            Button(confirmation, text="Non.", command=no).pack()
        
        # name = Name.get()
        # file = open(name, 'w+')
        # file.write("*")
        # file.close()
        # fe.destroy()
        # mb.showinfo("PandoOS","File created with successful !")

    def RequestFile():
        createFile()

    # <-- end


    fe = Toplevel()
    fe.title("PandoOS - Explorateur de fichiers")
    fe.geometry("800x500")
    fe.minsize(800, 500)
    fe.maxsize(800, 500)
    fe.iconbitmap("img/fileexplorer-icon.ico")

    # File Explorer (UI)

    menuFe = Menu(fe)

    Name = Entry(fe, text="")
    FileRequest1 = Button(fe, text="Créer le fichier", command=RequestFile)
    FileRequest2 = Button(fe, text="Créer le dossier", command=RequestFolder)

    # Menu(s)

    File = Menu(menuFe, tearoff=0)
    File.add_command(label="Créer un nouveau fichier", command=file)
    File.add_command(label="Créer un nouveau dossier", command=folder)
    File.add_separator()
    File.add_command(label="Ouvrir un fichier", command=openfile)
    # File.add_command(label="Ouvrir une PandoApp", command=openpandoapp)

    # <-- end Menu(s)

    # Config UI

    fe.config(menu=menuFe, bg="white")
    Name.pack_forget()
    FileRequest1.pack_forget()
    FileRequest2.pack_forget()

    # Config menu

    menuFe.add_cascade(label="Fichier", menu=File)

    # <-- end

# <-- end

# Restart

def restart():
    os.system('cls')
    PandoOS.destroy()
    os.system('boot.py')

# Shutdown

def shutdown():
    sleep(0.5)
    mb.showinfo("PandoOS","Shutdown successful, press ENTER for continue.")
    os.system('cls')
    print("PandoOS> Shutdown...")
    sleep(0.5)
    mb.showinfo('PandoOS','See you a next time !')
    PandoOS.destroy()
    sleep(1)

# Settings

# --> 

def cbg():
    PandoOS.config(bg="gray")

def cbd():
    PandoOS.config(bg="white")

# <-- end

def settings():
    settingsGui = Toplevel()
    settingsGui.title("PandoOS - Paramètres")
    settingsGui.geometry("950x500")
    settingsGui.iconbitmap("img/settings.ico")
    settingsGui.resizable(False, False)
    # settingsGui.destroy()
    # mb.showinfo("PandoOS","Application indisponible pour le moment.")

    # --> Personalization Event

    def cbtowhite():
        PandoOS.config(bg="white")

    def cbtogray():
        PandoOS.config(bg="gray")

    def closepersonalizationoptionswindow():
        settings()

    def closesysteminformationswindow():
        settings()

    def closescreenoptionswindow():
        settings()

    def screenoptionsevent():
        def recordcameraofuser():
            def continuer1():
                nameoffile = nameOfFile.get()
                if nameoffile == "":
                    confirmation_.destroy()
                    mb.showerror("Enregistreur de caméra - Erreur !","Merci de donner un nom à votre fichier vidéo !")
                    recordcameraofuser()
                else:
                    mb.showinfo(f"Enregistreur de caméra - Information",f"Vous avez nommé votre vidéo en \"{nameoffile}.mp4\" !")
                    confirmation_.destroy()
                    print("PandoOS> record camera --> true")
                    mb.showwarning("Enregistreur de caméra - Attention !","Pressez la touche \"Q\" pour stopper l'enregistrement quand vous l'avez terminer.")
                    cap = cv2.VideoCapture(0)
                    cap.set(3,640)
                    cap.set(4,480)

                    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
                    out = cv2.VideoWriter(f'video/{nameoffile}.mp4', fourcc, 20.0, (640,480))

                    while(True):
                        ret, frame = cap.read()
                        out.write(frame)
                        cv2.imshow('Votre camera - RECORD (yes)', frame)
                        c = cv2.waitKey(1)
                        if c & 0xFF == ord('q'):
                            print("PandoOS> record camera --> false")
                            screenoptionsevent()
                            break

                    cap.release()
                    out.release()
                    cv2.destroyAllWindows()

            screenoptionswindow.destroy()
            confirmation_ = Toplevel()
            confirmation_.config(bg="white")
            confirmation_.geometry("300x100")
            confirmation_.title("Enregistreur de caméra - Information")
            confirmation_.resizable(False, False)
            confirmation_.iconbitmap("img/information.ico")
            i2 = Label(confirmation_, text="Entrez le nom de votre fichier \n(Pour donner le nom à la fin de l'enregistrement):")
            i2.pack()
            nameOfFile = Entry(confirmation_)
            nameOfFile.pack()
            Button(confirmation_, text="Continuer", command=continuer1).pack()

        settingsGui.destroy()
        screenoptionswindow = Toplevel()
        screenoptionswindow.geometry("500x500")
        screenoptionswindow.resizable(False, False)
        screenoptionswindow.title("PandoOS - Paramètres d'affichage")
        screenoptionswindow.config(bg="white")
        screenoptionswindow.iconbitmap("img/information.ico")
        screenoptionswindow.protocol("WM_DELETE_WINDOW", lambda: [screenoptionswindow.destroy(), closesysteminformationswindow()])
        Button(screenoptionswindow, text="Enregistrer votre caméra", command=recordcameraofuser).pack()

    def systeminformationsevent():
        settingsGui.destroy()
        systeminformationswindow = Toplevel()
        systeminformationswindow.geometry("500x500")
        systeminformationswindow.resizable(False, False)
        systeminformationswindow.title("PandoOS - Informations système")
        systeminformationswindow.iconbitmap("img/information.ico")
        systeminformationswindow.protocol("WM_DELETE_WINDOW", lambda: [systeminformationswindow.destroy(), closesysteminformationswindow()])
        # systeminformations.config()

        system_ = platform.uname()

        versionos = Label(systeminformationswindow, text="Version: PandoOS v1.5 (Build 15.0_official)")
        versionos.pack()

        machineos = Label(systeminformationswindow, text=f"Machine: {system_.machine}")
        machineos.pack()
        
        cpuinfos = Label(systeminformationswindow, text=f"Processeur: {system_.processor}")
        cpuinfos.pack()

        closebtn = Button(systeminformationswindow, text="Revenir au menu de sélection", command=lambda: [systeminformationswindow.destroy(), closesysteminformationswindow()])
        closebtn.pack(side="bottom")

    def personalizationevent():
        settingsGui.destroy()
        personalizationoptionswindow = Toplevel()
        personalizationoptionswindow.geometry("950x500")
        personalizationoptionswindow.resizable(False, False)
        personalizationoptionswindow.title("PandoOS - Personalisation système")
        personalizationoptionswindow.config(bg="white")
        personalizationoptionswindow.iconbitmap("img/information.ico")
        
        changebackgroundtext = Label(personalizationoptionswindow, text="Changez la couleur du fond d'écran")
        changebackgroundtext.pack()
        changebackgroundbtn1 = Button(personalizationoptionswindow, text="Mettre en blanc (Par défaut)", command=cbtowhite)
        changebackgroundbtn2 = Button(personalizationoptionswindow, text="Mettre en gris", command=cbtogray)

        changebackgroundbtn1.pack()
        changebackgroundbtn2.pack()

        closebtn = Button(personalizationoptionswindow, text="Revenir au menu de sélection", command=lambda: [personalizationoptionswindow.destroy(), closepersonalizationoptionswindow()])
        closebtn.pack(side="bottom")

    # --> UI

    l = 0

    # --> UI Config

    toolbar1 = Menu(settingsGui)

    screenoptions = Menu(toolbar1, tearoff=0)
    systeminformations = Menu(toolbar1, tearoff=0)
    personalizationoptions = Menu(toolbar1, tearoff=0)

    personalizationoptions.add_command(label="Personaliser PandoOS", command=personalizationevent)
    systeminformations.add_command(label="Informations système", command=systeminformationsevent)
    screenoptions.add_command(label="Paramètres d'affichage", command=screenoptionsevent)

    toolbar1.add_cascade(label="Affichage", menu=screenoptions)
    toolbar1.add_cascade(label="Infos systèmes", menu=systeminformations)
    toolbar1.add_cascade(label="Personalisation", menu=personalizationoptions)

    settingsGui.config(bg="white", menu=toolbar1)

# Toolbar

menu = Menu(PandoOS)

# Apps Menu

appsMenu = Menu(menu, tearoff=0)
appsMenu.add_command(label="Horloge", command=clock)
appsMenu.add_command(label="PandoPad", command=notepad)

# Tools Menu

ToolsMenu = Menu(menu, tearoff=0)
ToolsMenu.add_command(label="Explorateur de fichiers", command=fileexplorer)

# Start Menu

Start = Menu(menu, tearoff=0)
Start.add_command(label="Éteindre", command=shutdown)
Start.add_command(label="Redémarrer", command=restart)
Start.add_separator()
Start.add_command(label="Paramètres", command=settings)

# Add menu(s) in menu

menu.add_cascade(label="Démarrer", menu=Start)
menu.add_cascade(label="Outils", menu=ToolsMenu)
menu.add_cascade(label="Applications", menu=appsMenu)

# UI

# def currentTime():
#     def t():
#         string = strftime('%H:%M:%S')
#         currenttime.config(text=string)
#         currenttime.after(1000, t)
#     currenttime = Label(PandoOS)
#     currenttime.pack(side="bottom")
#     t()

# currentTime()

# Show menu

PandoOS.config(menu=menu)

# Run UI

PandoOS.mainloop()
