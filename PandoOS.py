from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from time import *
from time import strftime
import tkinter.messagebox as mb
import os

try:
	os.mkdir("Desktop")
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

# def pandoshopapp():
# 	shop = Toplevel()
# 	shop.title("PandoShop - Accueil")
# 	shop.geometry("1000x500")
# 	shop.minsize(1000, 500)
# 	shop.maxsize(1000, 500)
# 	shop.iconbitmap("img/information.ico")
# 	shop.config(bg="white")

# 	# Menu(s)

# 	shopnav = Menu(shop)

# 	# -->

# 	principalmenu = Menu(shopnav, tearoff=0)

# 	shopnav.add_cascade(label="Outils", menu=principalmenu)

# 	# <--

# 	# print("PandoOS> An error occured. Error #1: PandoShop is not found in PandoOS.py !")
# 	# Menu config
# 	shop.config(menu=shopnav)


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

def sessionsmanager():
	def closeSession():
		def yes():
			PandoOS.destroy()
			os.system('boot.py')
		def no():
			confirmation.destroy()
		confirmation = Toplevel()
		confirmation.maxsize(300, 100)
		confirmation.minsize(300, 100)
		confirmation.title("PandoOS - Attention !")
		confirmation.iconbitmap("img/warning.ico")
		Label(confirmation, text="Etes-vous sûr de fermer votre session ?").pack()
		Button(confirmation, text="Oui.", command=yes).pack()
		Button(confirmation, text="Non.", command=no).pack()

	session_file = open('sessions/sessions.PandoOS-session', "r")
	session_id = session_file.readlines(0)
	# print(session_id)
	session_file.close()
	sm = Toplevel()
	sm.title("PandoOS - Gestionnaire de sessions")
	sm.geometry("800x500")
	sm.iconbitmap("img/information.ico")
	sm.maxsize(800, 500)
	sm.minsize(800, 500)
	# sm.config(bg="white")
	nbsessions = Label(sm, text="Sessions: 1")
	nbsessions.grid()
	session_name = Label(sm, text="session1 (ID: " + str(session_id) + ")")
	session_name.grid()
	closesession = Button(sm, text="Close Session", command=closeSession)
	closesession.grid()

def fileexplorer():
	# (Func) Open a file

	def openfile():
		file = filedialog.askopenfilename(title="Sélectionner un fichier", initialdir="C:/Users/")
		os.system('start ' + file)
		mb.showinfo('PandoOS','Vous avez ouvert avec succès "' + file + '" !')

	# (Func) Create Folder

	def folder():
		Name.pack()
		FileRequest2.pack()

	def createFolder():
		name = Name.get()
		if name == "default" or name == "":
			mb.showerror("PandoOS","Veuillez donner un nom correct à votre dossier !")
		else:
			userprofile = os.system('%userprofile%')
			os.system('cls')
			print('PandoOS> %userprofile% not found.')
			name = Name.get()
			os.mkdir(f"Desktop/{name}")
			fe.destroy()
			mb.showinfo("PandoOS","Dossier crée avec succès !")

	def RequestFolder():
		createFolder()

	# (Func) Create File

	def file():
		Name.pack()
		FileRequest1.pack()

	def createFile():
		name = Name.get()
		if name == "":
			mb.showerror("PandoOS","Veuillez donner un nom à votre fichier !")
			fe.destroy()
		else:
			# --> Button "Oui"


			def yes():
				def requestfilewithfolder():
					nameFolder = namefolder.get()
					confirmation2.destroy()
					try:
					    os.mkdir("Desktop/" + nameFolder)
					    file = open("Desktop/" + nameFolder + "/" + name, 'w+')
					    file.write(".")
					    file.close()
					    mb.showinfo("PandoOS","Fichier crée avec succès !")
					except FileExistsError:
					    # directory already exists
					    file = open("Desktop/" + nameFolder + "/" + name, 'w+')
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
				folder = "Desktop"
				file = open(folder + "/" + name, 'w+')
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
	fe.iconbitmap("img/information.ico")

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
	File.add_command(label="Ouvrir un ficher", command=openfile)

	# <-- end Menu(s)

	l = 0

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
	PandoOS.destroy()
	os.system('py boot.py')

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
	settingsGui.iconbitmap("img/information.ico")
	Label(settingsGui, text="\n").pack()
	changebackground = Label(settingsGui, text="Changez le fond d'écran:").pack()
	Label(settingsGui, text="-------------------------------").pack()
	cbtogray = Button(settingsGui, text="Gris", command=cbg).pack()
	cbtodefault = Button(settingsGui, text="Défaut (Blanc)", command=cbd).pack()
	Label(settingsGui, text="-------------------------------").pack()
	Label(settingsGui, text="\n").pack()


# Toolbar

menu = Menu(PandoOS)

# Apps Menu

appsMenu = Menu(menu, tearoff=0)
appsMenu.add_command(label="Horloge", command=clock)
# appsMenu.add_command(label="PandoShop", command=pandoshopapp)

# Tools Menu

ToolsMenu = Menu(menu, tearoff=0)
ToolsMenu.add_command(label="Explorateur de fichiers", command=fileexplorer)
ToolsMenu.add_command(label="Gestionnaire de sessions", command=sessionsmanager)

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

def currentTime():
	def t():
		string = strftime('%H:%M:%S')
		currenttime.config(text=string)
		currenttime.after(1000, t)
	currenttime = Label(PandoOS)
	currenttime.pack(side="bottom")
	t()

currentTime()

# Show menu

PandoOS.config(menu=menu)

# Run UI

PandoOS.mainloop()
