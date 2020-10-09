'''
GUI Component of Text2Podcast developed by Christoferis
c 2020 MIT - License

Stand: 4 October 2020

Used Libraries: python os + python tkinter
python ver 3.8+

TODO:
- sourcepath dictionary with language (French and Stuff)
- GitHub Commit
- setup.py
- pytesseract integration
- gtts integration
- Implement proper Preprocessing
- Toplevel Help
- Dark Mode
- Toplevel Savelocation Filename + Autoplay
'''
#File Imports
from Midend import midend

#External Imports
from tkinter import Tk as tk, Menu, Frame, Button, filedialog as fd, Listbox, Toplevel, ttk, Label
from os import startfile, getenv
from random import randint

#Construct main window as global
main = tk()
main.title("Text2Podcast by Christoferis V1.0")
main.geometry("1280x720")


#Filenamegenerator 
def rangen():
    Filename = r"\temp"

    for i in range(4):
        Filename += str(randint(0, 999))

    Filename += ".txt"
    return str(Filename)
    
#Main Open class
class File:
    #External accesed vars
    sourcepaths = list()

    def __init__(self, listbox):
        #var
        self.listbox = listbox
        self.listbox.insert("end", "Welcome to Text2Podcast! Start by Importing some Files")


    def opFile(self):
        #File Dialog
        currentfiles = list(fd.askopenfilenames(defaultextension="*.*", filetypes=[("Image Files", "*.png *.jpg *.jpeg"), ("Text Files", "*.txt")]))
        
        #delete welcome message
        if self.listbox.get(0) in ("Welcome to Text2Podcast! Start by Importing some Files",) and len(currentfiles) != 0:
            self.listbox.delete(0)
        
        #add Files to list and sourcepaths
        for data in currentfiles:
            File.sourcepaths.append(data)
            self.listbox.insert("end", data)

    def delFile(self):
        #delete from sourcepaths
        try:
            File.sourcepaths.remove(str(self.listbox.get("active")))
        except ValueError:
            pass
        self.listbox.delete("active")

    def preview(self):
        #If File not found do nothing else startfile
        try:
            startfile(str(self.listbox.get("active")))
        except FileNotFoundError:
            pass

#
def backendStart():
    #----> File structure: GUI ---> midend constructs final file -----> Backend with ocr and gtts
    midend(files=File.sourcepaths)


#Toplevel GUI for choosing language the language of the file
def langGUI():
    global main
    tempGUI = Toplevel(main)
    tempGUI.title("Set language")
    tempGUI.geometry("400x120")

    #Construct Interface
    info = Label(tempGUI, text="In what language is this file in?\n Choose from Combobox or type a IETF Language tag in the Box below")
    choice = ttk.Combobox(tempGUI, values=("de", "en", "fr", "es"))
    confirmBut = Button(tempGUI, text="Set language for current files", background="green", foreground="white", height=2)
    #pack area
    info.pack()
    choice.pack()
    confirmBut.pack(pady=10)

    #returns lang the files should be associated as
    #return fileLang



#Main GUI Function
def GUI():
    #Import main window
    global main

    #Listbox Frame construction
    noteframe = Frame(main)
    pathlist = Listbox(noteframe)

    
    #initialization of the class
    inst = File(listbox=pathlist)

    #bottombar construction
    bottombar = Frame(main)
    confirm = Button(bottombar, text="Make Podcast", height=2, background="green", foreground="white", command=backendStart)


    #Topbar construction
    topbar = Frame(main)
    
    #Three Topbar Buttons
    impFiles = Button(topbar, text="Import Files", command=inst.opFile, height=2)
    remFiles = Button(topbar, text="Remove Files", height=2, command=inst.delFile)
    prevFiles = Button(topbar, text="Preview File", height=2, command=inst.preview)

    
    #Packaging
    
    #Topbar Pack
    topbar.pack(side="top")
    prevFiles.pack(side="right")
    impFiles.pack(side="left")
    remFiles.pack(side="top")

    
    #Listbox Packs
    noteframe.pack(fill="both", expand="true")
    pathlist.pack(fill="both", expand="true")
    
    #Bottombar Packs
    bottombar.pack(side="right")
    confirm.pack()
    
    #menubar
    menubar = Menu(main)
    
    #Open Image or Text
    menubar.add_command(label="Import Images / Textdata", command=inst.opFile)
    #Close Current
    menubar.add_command(label="Remove Selected File", command=inst.delFile)
    #Preview Imported Image using standard Image Opener
    menubar.add_command(label="Preview selected File", command=inst.preview)
    #Help and Credits
    menubar.add_command(label="Help / Credits")
    
    #other win config
    main.config(menu=menubar)
    

#Start of Programm
#GUI()
langGUI()

#mainloop
main.mainloop()