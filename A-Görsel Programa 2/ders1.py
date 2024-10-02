from tkinter import *

pen = Tk()
pen.title("Deneme")
pen.geometry("500x500")
def tikla():
    myLabel["text"]= "Butona basildi"
    myLabel["fg"] = "orange"
    myLabel["bg"] = "green"


def kapat():
    myLabel["text"]= "Buton kapildi"
    myLabel["fg"] = "black"
    myLabel["bg"] = "red"


myLabel = Label(pen, text="")
myLabel.grid(row=1,column=0,sticky=W)

clickButton = Button(pen,text="Tikla",command=tikla)
clickButton.grid(row=0,column=0,sticky=W)

closeButton = Button(pen,text="kapat",command=kapat)
closeButton.grid(row=0,column=1,sticky=W)

pen.mainloop()