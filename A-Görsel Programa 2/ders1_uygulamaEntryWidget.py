from tkinter import *

win = Tk()
win.title("Entry Kulanimi")
win.geometry("500x500")
def goster():
    cumle="Hos Geldin " + nameEntry.get()
    sonucLabel["text"] = cumle

nameLabel = Label(win,text="Isim: ")
nameEntry = Entry(win)
sonucButton = Button(win,text="Goster",command=goster)
sonucLabel = Label(win,text="")

nameLabel.grid(row=0,column=1,sticky=W)
nameEntry.grid(row=0,column=2,sticky=W)
sonucButton.grid(row=1,column=0,sticky=W)
sonucLabel.grid(row=2,column=0,sticky=W)
sonucLabel.grid(row=3,column=0,sticky=W)

win.mainloop()