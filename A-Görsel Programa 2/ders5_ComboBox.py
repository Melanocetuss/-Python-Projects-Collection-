from tkinter import *
from tkinter import ttk

def getir():
    if myComboBox.get()=="Pazartesi":
        lblSonuc["text"] = "Sectiginiz gun " + myComboBox.get()

    elif myComboBox.get()=="Sali":
        lblSonuc["text"] = "Sectiginiz gun " + myComboBox.get()

    else:
        lblSonuc["text"] = "Sectiginiz gun " + myComboBox.get()


win = Tk()
win.title("APP")
win.geometry("400x400")

gunler= ["Pazartesi","Sali","Carsamba"]

myComboBox= ttk.Combobox(win,values=gunler)
myComboBox.current(0)
kontrolButton = Button(win,text="Getir",command=getir)
lblSonuc = Label(win,text="")

myComboBox.grid(row=0,column=0,sticky=W)
kontrolButton.grid(row=1,column=0,sticky=E)
lblSonuc.grid(row=1,column=3,sticky=W)




win.mainloop()