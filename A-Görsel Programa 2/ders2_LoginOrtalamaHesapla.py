from tkinter import *

win = Tk()
win.title("Giris Ekrani")
win.geometry("400x400")

"""Veri kontrolu icin yazilan degiskenler"""
sistemKullaniciAdi="cesur"
sistemKullaniciSifre ="1234"
"""--------------------------------------"""
def kontrol():
    if sistemKullaniciAdi==kAEntry.get() and sistemKullaniciSifre==sEntry.get():
        def hesapla():
            ortalama = (int(not1Entry.get()) + int(not2Entry.get()) + int(not3Entry.get()))/3
            hesaplaSonucLabel["text"] = "Ortalama:",int(ortalama)

        win.destroy()
        hesapSayfasi = Tk()
        hesapSayfasi.title("Giris Ekrani")
        hesapSayfasi.geometry("400x400")

        not1Label = Label(hesapSayfasi,text="Not 1:")
        not1Entry = Entry(hesapSayfasi)
        not2Label = Label(hesapSayfasi, text="Not 2:")
        not2Entry = Entry(hesapSayfasi)
        not3Label = Label(hesapSayfasi, text="Not 3:")
        not3Entry = Entry(hesapSayfasi)
        hesaplaButton = Button(hesapSayfasi,text="Hesapla",command=hesapla)
        hesaplaSonucLabel = Label(hesapSayfasi,text="")

        not1Label.grid(row=0,column=0,sticky=E)
        not1Entry.grid(row=0,column=1,sticky=W)
        not2Label.grid(row=1,column=0,sticky=W)
        not2Entry.grid(row=1,column=1,sticky=W)
        not3Label.grid(row=2, column=0, sticky=W)
        not3Entry.grid(row=2, column=1, sticky=W)
        hesaplaButton.grid(row=3, column=1,sticky=E)
        hesaplaSonucLabel.grid(row=4,column=1,sticky=W)

        hesapSayfasi.mainloop()

    elif sistemKullaniciAdi!=kAEntry.get() and sistemKullaniciSifre==sEntry.get():
        sonucLabel["text"] = "Kullanici Adi hatali."

    elif sistemKullaniciAdi==kAEntry.get() and sistemKullaniciSifre!=sEntry.get():
        sonucLabel["text"] = "Sifre hatali."

    else:
        sonucLabel["text"] = "Boyle bir kullanici yok"


kALabel = Label(win,text="Kullanci Adi:")
sLabel = Label(win,text="Sifre")
kAEntry = Entry(win,bg="blue",fg="white",width=30,borderwidth=5)
kAEntry.insert(0,"cesur") #Tekrar tekrar girmemezi engeliyor
sEntry = Entry(win,bg="blue",fg="white",width=30,borderwidth=5,show="*")
sEntry.insert(0,"1234") #Tekrar tekrar girmemezi engeliyor
girisButton = Button(win,text="Giris",command=kontrol)
sonucLabel = Label(win,text="")

kALabel.grid(row=0,column=1,sticky=E)
kAEntry.grid(row=0,column=2,sticky=W)
sLabel.grid(row=1,column=1,sticky=E)
sEntry.grid(row=1,column=2,sticky=W)
girisButton.grid(row=2,column=2,sticky=E)
sonucLabel.grid(row=3,column=2,sticky=W)

win.mainloop()