import random
from tkinter import *
from tkinter import messagebox
import random


def baslat():

    def kontrol():
        tahmin = int(entryTahmin.get())

        if sayi>tahmin:
            can = hakSayisi
            can -=1
            lblCan["text"] = "Can:", can
            messagebox.showinfo("Bilgi", "Tahminin sayidan Kucuk")

        elif sayi<tahmin:
            can = hakSayisi
            can -= 1
            lblCan["text"] = "Can:", can
            messagebox.showinfo("Bilgi","Tahminin Sayidan Buyuk")

        elif sayi == tahmin:
            messagebox.showinfo("Bilgi", "Tebrikler Oyunu Kazandiniz")
            game.destroy()


    hakSayisi = int(entryHakSaysi.get())
    baslangicDegeri = int(entryBaslangicDegeri.get())
    bitisDegeri = int(entryBitisDegeri.get())
    sayi = random.randint(baslangicDegeri, bitisDegeri)
    win.destroy()

    game=Tk()
    game.title("Game")
    game.geometry("250x140")
    game.resizable(False,False)
    game.iconbitmap("JukeBox.ico")
    game.config(bg="black")

    lblTahmin = Label(game,text="Tahmin:",bg="black",fg="white")
    entryTahmin = Entry(game)
    lblCan = Label(game, text="", bg="black", fg="white")
    lblCan["text"]= "Can:",hakSayisi
    btnOnayla= Button(game,text="Onayla",command=kontrol)

    lblTahmin.grid(row=0,column=0,sticky=W)
    entryTahmin.grid(row=0,column=1,sticky=E)
    lblCan.grid(row=1,column=0,sticky=W)
    btnOnayla.grid(row=1,column=1,sticky=E)

    game.mainloop()


win = Tk()
win.title("APP")
win.geometry("250x140")
win.resizable(False,False)
win.iconbitmap("JukeBox.ico")
win.config(bg="black")

lblHakSaysi = Label(win,text="Hak Sayisi:",bg="black",fg="white")
lblBaslangicDegeri =Label(win,text="Baslangic Degeri:",bg="black",fg="white")
lblBitisDegeri =Label(win,text="Bitis Degeri:",bg="black",fg="white")
entryHakSaysi = Entry(win)
entryBaslangicDegeri = Entry(win)
entryBitisDegeri = Entry(win)
btnBaslat = Button(win,text="Baslat",bg="green",command=baslat)

lblHakSaysi.grid(row=0,column=0,sticky=W,padx=5,pady=5)
lblBaslangicDegeri.grid(row=1,column=0,sticky=W,padx=5,pady=5)
lblBitisDegeri.grid(row=2,column=0,sticky=W,padx=5,pady=5)
entryHakSaysi.grid(row=0,column=1,sticky=W,padx=5,pady=5)
entryBaslangicDegeri.grid(row=1,column=1,sticky=W,padx=5,pady=5)
entryBitisDegeri.grid(row=2,column=1,sticky=W,padx=5,pady=5)
btnBaslat.grid(row=3,column=1,sticky=E,padx=5,pady=5)

win.mainloop()