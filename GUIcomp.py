'''
GUI Component of Text2Podcast developed by Christoferis
c 2020 MIT - License

Stand: 4 October 2020

Used Libraries: python os + python tkinter
python ver 3.8+

TODO:
- Duplicate Path auswerfen
- if startfile none soll nichts gemacht werden
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
from OCRcomp import ocr

#External Imports
from tkinter import Tk as tk, Menu, Frame, Button, filedialog as fd, Listbox
from os import startfile, getenv
from random import randint

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

#OCR starter

def ocrstart():
    #----> Combiner which takes the stuff sorts it and puts it in one string for gtts to process
    ocr(queue=File.sourcepaths)


#Main GUI Function
def GUI():
    #Set stuff up
    main = tk()
    main.title("Text2Podcast by Christoferis V1.0")
    main.geometry("1280x720")

    #Main Frames
    
    #Listbox Frame construction
    noteframe = Frame(main)
    pathlist = Listbox(noteframe)

    
    #initialization of the class
    inst = File(listbox=pathlist)

    #bottombar construction
    bottombar = Frame(main)
    confirm = Button(bottombar, text="Make Podcast", height=2, background="green", foreground="white", command=ocrstart)


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
    
    main.mainloop()

GUI()
