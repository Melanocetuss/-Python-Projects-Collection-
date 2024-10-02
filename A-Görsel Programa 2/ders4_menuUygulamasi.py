from tkinter import *

def calculate():
    def hesapla():
        if var.get() == 1:
            lblSonuc["text"]= "Sonuc:", (int(entrySayi1.get()) + int(entrySayi2.get()))

        elif var.get() == 2:
            lblSonuc["text"]= "Sonuc:", (int(entrySayi1.get()) - int(entrySayi2.get()))

        elif var.get() == 3:
            lblSonuc["text"]= "Sonuc:", (int(entrySayi1.get()) * int(entrySayi2.get()))

        elif var.get() == 4:
            lblSonuc["text"]= "Sonuc:", (int(entrySayi1.get()) / int(entrySayi2.get()))
    win.destroy()
    win2=Tk()
    win2.title("My APP")
    win2.geometry("400x400")

    lblSayi1 = Label(win2,text="Sayi 1:")
    lblSayi2 = Label(win2,text="Sayi 2:")
    entrySayi1 = Entry(win2,borderwidth=5,bg="blue",fg="white")
    entrySayi2 = Entry(win2,borderwidth=5,bg="blue",fg="white")
    var = IntVar(win2)
    radioTop = Radiobutton(win2,text="Topla",variable=var,value=1)
    radioCik = Radiobutton(win2, text="Cikar", variable=var, value=2)
    radioCarp = Radiobutton(win2, text="Carp", variable=var, value=3)
    radioBol = Radiobutton(win2, text="Bol", variable=var, value=4)
    btnHesapla = Button(win2,text="Hesapla",command=hesapla)
    lblSonuc = Label(win2,text="")

    lblSayi1.grid(row=0,column=0,sticky=W)
    lblSayi2.grid(row=1,column=0,sticky=W)
    entrySayi1.grid(row=0,column=1,sticky=E)
    entrySayi2.grid(row=1, column=1, sticky=E)
    radioTop.grid(row=2,column=0)
    radioCik.grid(row=2,column=1)
    radioCarp.grid(row=2,column=2)
    radioBol.grid(row=2,column=3)
    btnHesapla.grid(row=3,column=3,sticky=E)
    lblSonuc.grid(row=4,column=3)
    win2.mainloop()


def openInformationPage():
    win.destroy()
    win3 = Tk()
    win3.title("My APP")
    win3.geometry("400x400")

    lblInformation = Label(win3,text="Cesur Alphan Ellik",font=("Ariel",20),fg="red")
    lblInformation.grid(row=0,column=0)

    win3.mainloop()


win = Tk()
win.title("My App")
win.geometry("400x400")

myMenu = Menu(win)
win.config(menu=myMenu)
actionMenu = Menu(myMenu)
myMenu.add_cascade(label="Aksiyonlar", menu=actionMenu)
actionMenu.add_command(label="Hesapla", command=calculate)
actionMenu.add_command(label="Bilgi", command=openInformationPage)
actionMenu.add_command(label="Kapat", command=win.destroy)

win.mainloop()