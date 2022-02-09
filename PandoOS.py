from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from time import *
from time import strftime
from subprocess import Popen, PIPE
from tkvideo import *
from pygame import mixer
from tkinterweb import HtmlFrame
from tkinter import ttk
import tkinter as tk
import numpy as np
import cv2
import tkinter.messagebox as mb
import os
import platform
import shutil

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

# App(s) and Tool(s) -->

def calculator():
    calculatorapp = Toplevel()
    calculatorapp.title("Calculatrice - Accueil")
    calculatorapp.iconbitmap("img/calculator/calculator-icon.ico")
    calculatorapp.geometry("300x300")
    calculatorapp.resizable(False, False)

    def getResultMultiplicationfunc():
        addition.pack()
        soustraction.pack()
        multiplication.pack()
        division.pack()
        text1.pack_forget()
        operation1.pack_forget()
        text2.pack_forget()
        text3.pack_forget()
        operation2.pack_forget()
        getResultAddition.pack_forget()
        getResultSoustraction.pack_forget()
        getResultMultiplication.pack_forget()
        getResultDivision.pack_forget()
        operationget1 = int(operation1.get())
        operationget2 = int(operation2.get())
        operation = str(operationget1 * operationget2)

        # print(operationget1 + " - " + operationget2)
        resultofmultiplicationwindow = Toplevel()
        resultofmultiplicationwindow.geometry("300x100")
        resultofmultiplicationwindow.title("Calculatrice - Résultat")
        resultofmultiplicationwindow.iconbitmap("img/calculator/calculator-icon.ico")
        resultofmultiplicationwindow.resizable(False, False)

        result = Label(resultofmultiplicationwindow, text="Le résultat est: " + operation)
        result.pack()

        continue1 = Button(resultofmultiplicationwindow, text="Fermer", command=resultofmultiplicationwindow.destroy)
        continue1.pack()

    def getResultAdditionfunc():
        addition.pack()
        soustraction.pack()
        multiplication.pack()
        division.pack()
        text1.pack_forget()
        operation1.pack_forget()
        text2.pack_forget()
        text3.pack_forget()
        operation2.pack_forget()
        getResultAddition.pack_forget()
        getResultSoustraction.pack_forget()
        getResultMultiplication.pack_forget()
        getResultDivision.pack_forget()
        operationget1 = int(operation1.get())
        operationget2 = int(operation2.get())
        operation = str(operationget1 + operationget2)

        # print(operationget1 + " - " + operationget2)
        resultofadditionwindow = Toplevel()
        resultofadditionwindow.geometry("300x100")
        resultofadditionwindow.title("Calculatrice - Résultat")
        resultofadditionwindow.iconbitmap("img/calculator/calculator-icon.ico")
        resultofadditionwindow.resizable(False, False)

        result = Label(resultofadditionwindow, text="Le résultat est: " + operation)
        result.pack()

        continue1 = Button(resultofadditionwindow, text="Fermer", command=resultofadditionwindow.destroy)
        continue1.pack()

    def getResultSoustractionfunc():
        addition.pack()
        soustraction.pack()
        multiplication.pack()
        division.pack()
        text1.pack_forget()
        operation1.pack_forget()
        text2.pack_forget()
        text3.pack_forget()
        operation2.pack_forget()
        getResultAddition.pack_forget()
        getResultSoustraction.pack_forget()
        getResultMultiplication.pack_forget()
        getResultDivision.pack_forget()
        operationget1 = int(operation1.get())
        operationget2 = int(operation2.get())
        operation = str(operationget1 - operationget2)
        # print(operationget1 + " - " + operationget2)
        resultofsoustractionwindow = Toplevel()
        resultofsoustractionwindow.geometry("300x100")
        resultofsoustractionwindow.title("Calculatrice - Résultat")
        resultofsoustractionwindow.iconbitmap("img/calculator/calculator-icon.ico")
        resultofsoustractionwindow.resizable(False, False)

        result = Label(resultofsoustractionwindow, text="Le résultat est: " + operation)
        result.pack()

        continue1 = Button(resultofsoustractionwindow, text="Fermer", command=resultofsoustractionwindow.destroy)
        continue1.pack()

    def getResultDivisionfunc():
        addition.pack()
        soustraction.pack()
        multiplication.pack()
        division.pack()
        text1.pack_forget()
        operation1.pack_forget()
        text2.pack_forget()
        text3.pack_forget()
        operation2.pack_forget()
        getResultAddition.pack_forget()
        getResultSoustraction.pack_forget()
        getResultMultiplication.pack_forget()
        getResultDivision.pack_forget()
        operationget1 = int(operation1.get())
        operationget2 = int(operation2.get())
        operation = str(operationget1 / operationget2)
        # print(operationget1 + " - " + operationget2)
        resultofdivisionwindow = Toplevel()
        resultofdivisionwindow.geometry("300x100")
        resultofdivisionwindow.title("Calculatrice - Résultat")
        resultofdivisionwindow.iconbitmap("img/calculator/calculator-icon.ico")
        resultofdivisionwindow.resizable(False, False)

        result = Label(resultofdivisionwindow, text="Le résultat est: " + operation)
        result.pack()

        continue1 = Button(resultofdivisionwindow, text="Fermer", command=resultofdivisionwindow.destroy)
        continue1.pack()

    def divisionfunc():
        multiplication.pack_forget()
        addition.pack_forget()
        soustraction.pack_forget()
        division.pack_forget()
        text1.pack()
        operation1.pack()
        text2.pack()
        text3.pack()
        operation2.pack()
        getResultAddition.pack_forget()
        getResultSoustraction.pack_forget()
        getResultMultiplication.pack_forget()
        getResultDivision.pack()

    def multiplicationfunc():
        multiplication.pack_forget()
        addition.pack_forget()
        soustraction.pack_forget()
        division.pack_forget()
        text1.pack()
        operation1.pack()
        text2.pack()
        text3.pack()
        operation2.pack()
        getResultAddition.pack_forget()
        getResultSoustraction.pack_forget()
        getResultMultiplication.pack()
        getResultDivision.pack_forget()

    def soustractfunc():
        multiplication.pack_forget()
        addition.pack_forget()
        soustraction.pack_forget()
        division.pack_forget()
        text1.pack()
        operation1.pack()
        text2.pack()
        text3.pack()
        operation2.pack()
        getResultAddition.pack_forget()
        getResultSoustraction.pack()
        getResultMultiplication.pack_forget()
        getResultDivision.pack_forget()

    def additionfunc():
        multiplication.pack_forget()
        addition.pack_forget()
        soustraction.pack_forget()
        division.pack_forget()
        text1.pack()
        operation1.pack()
        text2.pack()
        text3.pack()
        operation2.pack()
        getResultAddition.pack()
        getResultSoustraction.pack_forget()
        getResultMultiplication.pack_forget()
        getResultDivision.pack_forget()

    text1 = Label(calculatorapp, text="Entrez le premier chiffre:")
    operation1 = Entry(calculatorapp)
    text2 = Label(calculatorapp, text="")
    text3 = Label(calculatorapp, text="Entrez le deuxième chiffre:")
    operation2 = Entry(calculatorapp)

    text1.pack_forget()
    text2.pack_forget()
    text3.pack_forget()

    operation1.pack_forget()
    operation2.pack_forget()

    getResultAddition = Button(calculatorapp, text="Voir le résultat", command=getResultAdditionfunc)
    getResultAddition.pack_forget()
    getResultSoustraction = Button(calculatorapp, text="Voir le résultat", command=getResultSoustractionfunc)
    getResultSoustraction.pack_forget()
    getResultMultiplication = Button(calculatorapp, text="Voir le résultat", command=getResultMultiplicationfunc)
    getResultMultiplication.pack_forget()
    getResultDivision = Button(calculatorapp, text="Voir le résultat", command=getResultDivisionfunc)
    getResultDivision.pack_forget()


    addition = Button(calculatorapp, text="Additioner 2 nombres.", command=additionfunc)
    addition.pack()

    soustraction = Button(calculatorapp, text="Soustraire 2 nombres.", command=soustractfunc)
    soustraction.pack()

    multiplication = Button(calculatorapp, text="Multiplier 2 nombres.", command=multiplicationfunc)
    multiplication.pack()

    division = Button(calculatorapp, text="Diviser 2 nombres.", command=divisionfunc)
    division.pack()

def pandoweb():
    pandowebapp = Toplevel()
    pandowebapp.title("PandoWeb - Bienvenue !")
    pandowebapp.geometry("1000x500")
    pandowebapp.resizable(False, False)
    pandowebapp.iconbitmap("img/navigator/logo.ico")

    # "startwebsiteevent" func

    def startwebsiteevent():
        websitenameget = websitename.get()
        if websitenameget == "":
            mb.showerror("PandoWeb","Merci de rentrer une URL correcte !")
        else: 
            pandowebapp.destroy()
            websitewindow = Toplevel()
            websitewindow.title("PandoWeb - Nouvel onglet")
            websitewindow.geometry("1000x500")
            websitewindow.resizable(False, False)
            websitewindow.iconbitmap("img/navigator/logo.ico")

            def goonpandooswebsite():
                websitewindow.title("PandoWeb - PandoOS")
                frame.load_website("https://statswarstv.wixsite.com/pandoos")

            def gobackongoogle():
                websitewindow.title("PandoWeb - Google")
                frame.load_website("google.com")

            backongoogle = Button(websitewindow, text="Aller sur Google", command=gobackongoogle)
            backongoogle.pack()

            goonpandoos = Button(websitewindow, text="Aller sur le site de PandoOS", command=goonpandooswebsite)
            goonpandoos.pack()

            frame = HtmlFrame(websitewindow)
            frame.load_website(websitenameget)
            frame.pack(fill="both", expand=True)

    # GUI

    Label(pandowebapp, text="\n").pack()
    websitename = Entry(pandowebapp)
    websitename.pack()
    startwebsite = Button(pandowebapp, text="Ouvrir l'URL", command=startwebsiteevent)
    startwebsite.pack()

    # Close PandoWeb

    def quitpandoweb():
        pandowebapp.destroy()

    # Menu(s)

    menuPandoWebApp = Menu(pandowebapp)

    menu1 = Menu(menuPandoWebApp, tearoff=0)
    menu1.add_command(label="Quitter", command=quitpandoweb)

    # <-- end Menu(s)

    # Config UI

    pandowebapp.config(menu=menuPandoWebApp)

    # Config menu

    menuPandoWebApp.add_cascade(label="Menu", menu=menu1)

def camerarecorder():
    def continuer1():
        def startrecording():
            nameoffile = nameOfFile.get()
            if nameoffile == "":
                confirmation_.destroy()
                mb.showerror("Enregistreur de caméra - Erreur !","Merci de donner un nom à votre enregistrement !")
                continuer1()
            else:
                mb.showinfo(f"Enregistreur de caméra - Information",f"Vous avez nommé votre vidéo en \"{nameoffile}.mp4\" !")
                confirmation_.destroy()
                mb.showwarning("Enregistreur de caméra - Attention !","Appuyez sur la touche \"Q\" pour stopper l'enregistrement quand vous l'avez terminer.")
                cap = cv2.VideoCapture(0)
                cap.set(3,640)
                cap.set(4,480)

                fourcc = cv2.VideoWriter_fourcc(*'MP4V')
                out = cv2.VideoWriter(f'video/{nameoffile}.mp4', fourcc, 20.0, (640,480))

                while(True):
                    ret, frame = cap.read()
                    out.write(frame)
                    cv2.imshow('Enregistrement en cours...', frame)
                    c = cv2.waitKey(1)
                    if c & 0xFF == ord('q'):
                        mb.showinfo("Enregistreur de caméra - Information","l'enregistrement à été sauvergarder dans le dossier \"video\" avec succès !")
                        camerarecorder()
                        break

                cap.release()
                out.release()
                cv2.destroyAllWindows()

        camerarecorderwindow.destroy()
        confirmation_ = Toplevel()
        confirmation_.geometry("300x100")
        confirmation_.title("Enregistreur de caméra - Information")
        confirmation_.resizable(False, False)
        confirmation_.iconbitmap("img/warning2.ico")
        confirmation_.protocol("WM_DELETE_WINDOW", lambda: confirmation_.destroy())
        i2 = Label(confirmation_, text="Entrez le nom de votre fichier \n(Pour donner le nom à la fin de l'enregistrement):")
        i2.pack()
        nameOfFile = Entry(confirmation_)
        nameOfFile.pack()
        Button(confirmation_, text="Continuer", command=startrecording).pack()

    camerarecorderwindow = Toplevel()
    camerarecorderwindow.geometry("300x100")
    camerarecorderwindow.resizable(False, False)
    camerarecorderwindow.title("Enregistreur de caméra")
    camerarecorderwindow.iconbitmap("img/camerarecorder-icon.ico")
    camerarecorderwindow.protocol("WM_DELETE_WINDOW", lambda: camerarecorderwindow.destroy())
    Label(camerarecorderwindow, text="\n").pack()
    Button(camerarecorderwindow, text="Enregistrer votre caméra", command=continuer1).pack()

def audioplayer():
    ap = Toplevel()
    ap.title("Lecteur audio")
    ap.geometry("500x200")
    ap.resizable(False, False)
    ap.iconbitmap("img/audioplayer.ico")

    def stopaudio():
        mixer.music.stop()
        music.configure(text="??? - Aucune musique en cours.")
        music.pack_forget()
        stopbutton.pack_forget()
        ap.title("Lecteur audio")
        startaudio.pack()
        pausebutton1.pack_forget()
        pausebutton2.pack_forget()

    def readaudio():

        startaudio.pack_forget()
        mixer.init()
    
        def raudio():
            mixer.music.load(file)
            mixer.music.play()

            ap.title(f"Lecteur audio - {file}")

            music.configure(text="\n" + file + " - Lecture en cours...")
            music.pack()
            stopbutton.pack()
            startaudio.pack_forget()
            pausebutton1.pack()

        file = filedialog.askopenfilename(defaultextension='*.mp3*', title="Sélectionner un fichier audio", initialdir="C:/Users/", filetypes=[('Fichiers MP3', '*.mp3*'), ("Fichier WAW", "*.waw*")])
        if file == "":
            mb.showerror("PandoOS","Vous avez sélectionner aucun fichier à lancer ! Relancez le lecteur audio pour réessayer !")
        else:
            mb.showinfo('PandoOS','Vous avez sélectionner avec succès "' + file + '" !')
            raudio()

    def pauseaudio2():
        mixer.music.unpause()
        pausebutton1.pack()
        pausebutton2.pack_forget()

    def pauseaudio1():
        mixer.music.pause()
        pausebutton1.pack_forget()
        pausebutton2.pack()

    Label(ap, text="\n").pack()

    startaudio = Button(ap, text="Lire un fichier audio", command=readaudio)
    startaudio.pack()

    music = Label(ap, text="??? - Aucune musique en cours.")
    music.pack_forget()

    Label(ap, text="\n").pack()

    stopbutton = Button(ap, text="Arrêter la musique", command=stopaudio)
    stopbutton.pack_forget()

    pausebutton1 = Button(ap, text="Mettre en pause la musique", command=pauseaudio1)
    pausebutton1.pack_forget()

    pausebutton2 = Button(ap, text="Reprendre la musique", command=pauseaudio2)
    pausebutton2.pack_forget()

def videoplayer():
    vp = Toplevel()
    vp.title("Lecteur vidéo")
    vp.geometry("800x500")
    vp.resizable(False, False)
    vp.iconbitmap("img/videoplayer.ico")

    def readvideo():
        vp.destroy()
        file = filedialog.askopenfilename(defaultextension='*.mp4*', title="Sélectionner un fichier vidéo", initialdir="C:/Users/", filetypes=[('Fichiers MP4', '*.mp4*'), ("Fichier GIF", "*.gif*")])
        if file == "":
            mb.showerror("PandoOS","Vous avez sélectionner aucun fichier vidéo à lancer !")
            readvideo()
        else:
            mb.showinfo('PandoOS','Vous avez sélectionner avec succès le fichier vidéo nommé "' + file + '" !')
        vpoutput = Toplevel()
        vpoutput.title(f"Lecteur vidéo - {file}")
        vpoutput.iconbitmap("img/videoplayer.ico")
        vpoutput.bind('<Escape>', lambda e: vpoutput.destroy())
        video = Label(vpoutput)
        video.pack()
        player = tkvideo(file, video, loop=1, size=(800,500))
        player.play()

    startvideo = Button(vp, text="Lire une vidéo", command=readvideo)
    startvideo.pack()

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
            confirmation3.iconbitmap("img/info3.ico")

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
                m.iconbitmap("img/info3.ico")

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

def codeeditor():
    def savefile():
        i = l.get()
        if i == "":
            cewindow.destroy()
            mb.showerror("PandoCode","Merci d'entrer un nom correct pour votre fichier !")
            notepad()
        else:
            t = text.get("1.0", "end-1c")
            cewindow.destroy()
            confirmation3 = Toplevel()
            confirmation3.title("PandoCode - Attention !")
            confirmation3.geometry("300x100")
            confirmation3.resizable(False, False)
            confirmation3.iconbitmap("img/info3.ico")

            def yes():
                confirmation3.destroy()
                def requesttextfile():
                    foldername = folderName.get()
                    m.destroy()
                    if foldername == "":
                        mb.showerror("PandoCode","Entrez un nom correct d'un dossier existant ou non !")
                        yes()
                    else:
                        try:
                            os.mkdir("root/Desktop/" + foldername)
                            file = open("root/Desktop/" + foldername + "/" + i, "w+")
                            file.write(t)
                            file.close()
                            mb.showinfo("PandoCode","Vous avez créer un fichier avec succès !")
                        except FileExistsError:
                            # directory already exists
                            file = open("root/Desktop/" + foldername + "/" + i, "w+")
                            file.write(t)
                            file.close()
                            mb.showinfo("PandoCode","Vous avez créer un fichier avec succès !")

                m = Toplevel()
                m.title("PandoCode - Information")
                m.geometry("300x100")
                m.resizable(False, False)
                m.iconbitmap("img/info3.ico")

                Label(m, text="Entrez le nom du dossier:").pack()

                folderName = Entry(m)
                folderName.pack()

                Button(m, text="Continuer", command=requesttextfile).pack()

            def no():
                confirmation3.destroy()
                file = open('root/Desktop/' + i, 'w+')
                file.write(t)
                file.close()
                mb.showinfo("PandoCode","Vous avez créer un fichier avec succès !")
                

            Label(confirmation3, text="Souhaitez-vous sauvegarder le fichier \ndans un dossier en particulier ?").pack()
            Button(confirmation3, text="Oui.", command=yes).pack()
            Button(confirmation3, text="Non.", command=no).pack()


    cewindow = Toplevel()
    cewindow.title('PandoCode')
    cewindow.geometry('850x500')
    cewindow.resizable(False, False)
    cewindow.iconbitmap('img/notepad-icon.ico')
    text = Text(cewindow)
    text.pack()
    Label(cewindow, text="Donnez un nom au fichier:").pack()
    l = Entry(cewindow)
    l.pack()
    button = Button(cewindow, text="Sauvegarder le fichier", command=savefile)
    button.pack()

def clock():
    clockapp = Toplevel()
    clockapp.title("PandoOS - Horloge")
    clockapp.geometry("600x300")
    clockapp.iconbitmap("img/clock.ico")

    def time():
        string=strftime('%H:%M:%S')
        label.config(text=string)
        label.after(1000, time)

    label = Label(clockapp, font=('arial', 80))
    label.pack(anchor='center', expand=True)
    time()

def fileexplorer():
    def deletefolder():
        def continue2():
            NameOfFolder = nameoffolder.get()
            confirmation4.destroy()
            if NameOfFolder == "":
                mb.showerror("PandoOS","Veuillez mettre le nom d'un dossier correct !")
                deletefolder()
            else:
                if not os.path.isdir("root/Desktop/" + NameOfFolder):
                    mb.showerror("PandoOS","Ce dossier n'existe pas, veuillez réesayer.")
                    fileexplorer()
                else:
                    shutil.rmtree("root/Desktop/" + NameOfFolder)
                    mb.showinfo("PandoOS","Vous avez supprimé le dossier " + NameOfFolder + " avec succès !")
                    fileexplorer()

        fe.destroy()
        confirmation4 = Toplevel()
        confirmation4.title("PandoOS - Information")
        confirmation4.iconbitmap("img/info3.ico")
        confirmation4.geometry("300x100")
        confirmation4.resizable(False, False)
        confirmation4.protocol("WM_DELETE_WINDOW", lambda: [confirmation4.destroy(), fileexplorer()])
        Label(confirmation4, text="Entrez le nom du dossier:").pack()
        nameoffolder = Entry(confirmation4)
        nameoffolder.pack()
        Button(confirmation4, text="Continuer", command=continue2).pack()

    def showfilesandfolder():
        dir_list = os.listdir("root/Desktop")
        Label(fe, text="Fichiers et dossiers dans \"root/Desktop\" :").pack()
        Label(fe, text=dir_list).pack()
        Label(fe, text="\n\n").pack()

    def deletefile():
        fe.destroy()
        userShell = os.getenv('username')
        file = filedialog.askopenfilename(defaultextension='*.*', title="Sélectionner un fichier", initialdir=f"C:/Users/{userShell}/Desktop", filetypes=[('Tout les fichiers', '*.*'),('Fichier web', '*.html*')])
        if file == "":
            mb.showerror("PandoOS","Vous avez sélectionner aucun fichier à supprimer !")
            fileexplorer()
        else:
            name_of_file = file
            os.remove(file)
            mb.showinfo("PandoOS","Vous avez supprimé avec succès " + file + " !")
            fileexplorer()

    def openfile():
        fe.destroy()
        FileRequest1.pack_forget()
        FileRequest2.pack_forget()
        Name.pack_forget()
        userShell = os.getenv('username')
        file = filedialog.askopenfilename(defaultextension='*.*', title="Sélectionner un fichier", initialdir=f"C:/Users/{userShell}/Desktop", filetypes=[('Tout les fichiers', '*.*'),('Fichier web', '*.html*')])
        if file == "":
            mb.showerror("PandoOS","Vous avez sélectionner aucun fichier à lancer !")
            fileexplorer()
        else:
            name_of_file = file
            mb.showinfo("PandoOS","Vous avez ouvert avec succès " + file + " !")
            os.startfile(name_of_file)
            fileexplorer()

    # (Func) Create Folder

    def folder():
        Name.pack()
        FileRequest2.pack()
        FileRequest1.pack_forget()

    def createFolder():
        name = Name.get()
        if name == "default" or name == "":
            mb.showerror("PandoOS","Veuillez donner un nom correct à votre dossier !")
        else:
            fe.destroy()
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
                            fileexplorer()
                        except FileExistsError:
                            # os.mkdir(f"root/Desktop/{name}/{folder}")
                            os.mkdir(f"root/Desktop/{folder}/{name}")
                            mb.showinfo("PandoOS","Dossier crée avec succès !")
                            fileexplorer()

                confirmation4.destroy()
                d = Toplevel()
                d.title("PandoOS - Information")
                d.geometry("300x100")
                d.resizable(False, False)
                d.iconbitmap("img/info3.ico")
                Label(d, text="Entrez le nom du dossier:").pack()
                nameoffolder = Entry(d)
                nameoffolder.pack()
                Button(d, text="Continuer", command=requestfolder).pack()

            def no():
                confirmation4.destroy()
                os.mkdir(f"root/Desktop/{name}")
                fe.destroy()
                mb.showinfo("PandoOS","Dossier crée avec succès !")
                fileexplorer()

            confirmation4 = Toplevel()
            confirmation4.title("PandoOS - Attention !")
            confirmation4.geometry("300x100")
            confirmation4.resizable(False, False)
            confirmation4.iconbitmap("img/info3.ico")
            Label(confirmation4, text="Souhaitez-vous le créer dans un dossier en particulier ?").pack()
            Button(confirmation4, text="Oui.", command=yes).pack()
            Button(confirmation4, text="Non.", command=no).pack()

    def RequestFolder():
        createFolder()

    # (Func) Create File

    def file():
        Name.pack()
        FileRequest1.pack()
        FileRequest2.pack_forget()

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
                            fileexplorer()
                        except FileExistsError:
                            # directory already exists
                            file = open("root/Desktop/" + nameFolder + "/" + name, 'w+')
                            file.write(".")
                            file.close()
                            mb.showinfo("PandoOS","Fichier crée avec succès !")
                            fileexplorer()
                confirmation.destroy()
                fe.destroy()
                confirmation2 = Toplevel()
                confirmation2.maxsize(300, 100)
                confirmation2.minsize(300, 100)
                confirmation2.title("PandoOS - Information")
                confirmation2.iconbitmap("img/info3.ico")
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
            confirmation.iconbitmap("img/info3.ico")
            Label(confirmation, text="Souhaitez-vous le sauvegarder \ndans un dossier en particulier ?").pack()
            Button(confirmation, text="Oui.", command=yes).pack()
            Button(confirmation, text="Non.", command=no).pack()

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
    File.add_command(label="Supprimer un fichier", command=deletefile)
    File.add_command(label="Supprimer un dossier", command=deletefolder)
    File.add_separator()
    File.add_command(label="Ouvrir un fichier", command=openfile)
    File.add_command(label="Voir tout les fichiers et dossiers", command=showfilesandfolder)

    # <-- end Menu(s)

    # Config UI

    fe.config(menu=menuFe)
    Name.pack_forget()
    FileRequest1.pack_forget()
    FileRequest2.pack_forget()

    # Config menu

    menuFe.add_cascade(label="Fichier", menu=File)

    # <-- end

# <-- end

# Restart

def restart():
    os.system("cls")
    PandoOS.destroy()
    os.system("python boot.py")

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

    def systeminformationsevent():
        settingsGui.destroy()
        systeminformationswindow = Toplevel()
        systeminformationswindow.geometry("500x500")
        systeminformationswindow.resizable(False, False)
        systeminformationswindow.title("PandoOS - Informations système")
        systeminformationswindow.iconbitmap("img/info3.ico")
        systeminformationswindow.protocol("WM_DELETE_WINDOW", lambda: [systeminformationswindow.destroy(), closesysteminformationswindow()])

        system_ = platform.uname()

        versionos = Label(systeminformationswindow, text="Version: PandoOS v5.0")
        versionos.pack()
        
        author = Label(systeminformationswindow, text="Auteur: MiyuCode (https://github.com/miyucode/PandoOS)")
        author.pack()

        latestversion = Label(systeminformationswindow, text="Dernière version de PandoOS: 5.0_official")
        latestversion.pack()

        build = Label(systeminformationswindow, text="Build: build_5000")
        build.pack()

        cpuinfos = Label(systeminformationswindow, text=f"Processeur: Non reconnu.")
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
        personalizationoptionswindow.iconbitmap("img/info3.ico")
        
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
    # screenoptions.add_command(label="Paramètres d'affichage", command=screenoptionsevent)

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
appsMenu.add_command(label="PandoCode", command=codeeditor)
appsMenu.add_command(label="Lecteur vidéo", command=videoplayer)
appsMenu.add_command(label="Lecteur audio", command=audioplayer)
appsMenu.add_command(label="Enregistreur de caméra", command=camerarecorder)
appsMenu.add_command(label="PandoWeb", command=pandoweb)
appsMenu.add_command(label="Calculatrice", command=calculator)

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
