from tkinter import *

root= Tk()
root.title("Color App")
root.geometry("200x200")
def rButton():
    cLabel["bg"]="red"
    eLabel["text"]="RED"

def bButton():
    cLabel["bg"] = "blue"
    eLabel["text"] = "BLUE"


def yButton():
    cLabel["bg"] = "yellow"
    eLabel["text"] = "YELLOW"


def gButton():
    cLabel["bg"] = "green"
    eLabel["text"] = "GREEN"

def pButton():
    cLabel["bg"] = "purple"
    eLabel["text"] = "PURPLE"





buttonsLabel = Label(root,text="Buttons")
colorsLabel = Label(root,text="Color")
englishLabel = Label(root,text="English")
rButton = Button(root,text="Kirmizi",command=rButton)
bButton = Button(root,text="Mavi",command=bButton)
yButton = Button(root,text="Sari",command=yButton)
gButton = Button(root,text="Yesil",command=gButton)
pButton = Button(root,text="Mor",command=pButton)
cLabel = Label(root,text="         ")
eLabel = Label(root,text="")


buttonsLabel.grid(row=0,column=0,sticky=W)
colorsLabel.grid(row=0,column=1,sticky=W)
englishLabel.grid(row=0,column=2,sticky=W)

rButton.grid(row=1,column=0,sticky=W)
bButton.grid(row=2,column=0,sticky=W)
yButton.grid(row=3,column=0,sticky=W)
gButton.grid(row=4,column=0,sticky=W)
pButton.grid(row=5,column=0,sticky=W)

cLabel.grid(row=1,column=1,sticky=W)
eLabel.grid(row=1,column=2,sticky=W)

root.mainloop()