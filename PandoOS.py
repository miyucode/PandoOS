from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from time import *
from time import strftime
import tkinter.messagebox as mb
import os

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

class sys(object):
    """docstring for sys"""
    def __init__(self, arg):
        super(sys, self).__init__()
        self.arg = arg
    def exec_(command):
        os.system(command)
    def ls(directory):
        if directory == "":
            os.system('dir')
        else:
            os.system('dir ' + directory)

# --> App(s) and Tool(s)

def shell():

    # Shell

    def exec_():
        output = cmd.get("1.0", "end-1c")
        if output == "":
            shellgui.destroy()
            mb.showerror("Invite de commandes", "Vous n'avez inscrit aucune commande à exécuter !")
            shell()
        elif output == "shutdown":
            shutdown()
        elif output == "restart":
            restart()

    # GUI Config

    shellgui = Toplevel()
    shellgui.title("Invite de commandes (Mode Administrateur désactivée)")
    shellgui.geometry("500x500")
    shellgui.resizable(False, False)
    shellgui.iconbitmap("img/shell/cmd-icon.ico")

    # GUI
    
    cmd = Text(shellgui)
    cmd.pack()

    exec_command = Button(shellgui, text="Exécuter la commande", command=exec_)
    exec_command.pack()

    aide = Button(shellgui, text="Docs")
    aide.pack()

    # <-- end

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

# def pandoshopapp():
#   shop = Toplevel()
#   shop.title("PandoShop - Accueil")
#   shop.geometry("1000x500")
#   shop.minsize(1000, 500)
#   shop.maxsize(1000, 500)
#   shop.iconbitmap("img/information.ico")
#   shop.config(bg="white")

#   # Menu(s)

#   shopnav = Menu(shop)

#   # -->

#   principalmenu = Menu(shopnav, tearoff=0)

#   shopnav.add_cascade(label="Outils", menu=principalmenu)

#   # <--

#   # print("PandoOS> An error occured. Error #1: PandoShop is not found in PandoOS.py !")
#   # Menu config
#   shop.config(menu=shopnav)


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
            def yes():
                demande1.destroy()
                mb.showinfo('PandoOS','Vous avez ouvert avec succès "' + file + '" !')
                os.system("notepad " + file)
                fileexplorer()

            def no():
                demande1.destroy()
                mb.showinfo('PandoOS','Vous avez ouvert avec succès "' + file + '" !')
                os.system(file)
                fileexplorer()

            demande1 = Toplevel()
            demande1.title("PandoOS - Attention !")
            demande1.resizable(False, False)
            demande1.geometry("300x100")
            demande1.iconbitmap("img/warning.ico")

            Label(demande1, text="Est-ce que le fichier sélectionner est un fichier texte ?\n Si oui, souhaitez-vous l'offrir avec le Bloc-Notes?").pack()
            Button(demande1, text="Oui.", command=yes).pack()
            Button(demande1, text="Non.", command=no).pack()

    # (Func) Create Folder

    def folder():
        Name.pack()
        FileRequest2.pack()
        FileRequest1.pack_forget()
        # print("Alerte> Si un message bizarre apparaît ici, cela est normal et si il ne s'affiche pas, ignorer cet alerte.")

    def createFolder():
        name = Name.get()
        if name == "default" or name == "":
            mb.showerror("PandoOS","Veuillez donner un nom correct à votre dossier !")
        else:
            # userprofile = os.system('%userprofile%')
            # print('PandoOS> %userprofile% not found.')
            os.system('cls')
            name = Name.get()
            os.mkdir(f"root/Desktop/{name}")
            fe.destroy()
            mb.showinfo("PandoOS","Dossier crée avec succès !")

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
    # settingsGui.destroy()
    # mb.showinfo("PandoOS","Application indisponible pour le moment.")

    # --> Personalization Event

    def cbtowhite():
        PandoOS.config(bg="white")

    def cbtogray():
        PandoOS.config(bg="gray")

    def closepersonalizationoptionswindow():
        settings()

    def personalizationevent():
        settingsGui.destroy()
        personalizationoptionswindow = Toplevel()
        personalizationoptionswindow.geometry("950x500")
        personalizationoptionswindow.resizable(False, False)
        personalizationoptionswindow.title("PandoOS - Personalisation système")
        personalizationoptionswindow.config(bg="white")
        
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

    toolbar1.add_cascade(label="Affichage", menu=screenoptions)
    toolbar1.add_cascade(label="Infos systèmes", menu=systeminformations)
    toolbar1.add_cascade(label="Personalisation", menu=personalizationoptions)

    settingsGui.config(bg="white", menu=toolbar1)

# Toolbar

menu = Menu(PandoOS)

# Apps Menu

appsMenu = Menu(menu, tearoff=0)
appsMenu.add_command(label="Horloge", command=clock)
appsMenu.add_command(label="Bloc-Notes", command=notepad)
# appsMenu.add_command(label="PandoShop", command=pandoshopap)

# Tools Menu

ToolsMenu = Menu(menu, tearoff=0)
ToolsMenu.add_command(label="Explorateur de fichiers", command=fileexplorer)
ToolsMenu.add_command(label="Invite de commandes", command=shell)

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
