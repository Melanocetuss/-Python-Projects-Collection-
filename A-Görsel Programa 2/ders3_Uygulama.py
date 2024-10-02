from tkinter import *

def kontrol():
    tarih = entryDogumTar.get().split("-")[2]
    yas = 2022 - int(tarih)
    if v1.get() == 1 or yas<18:
        lblSonuc["text"]="Lutfen kvvk onaylayın ve 18 yasından kucuksundur"

    elif v1.get() == 0 and yas>18:
        lblSonuc["text"]="Onaylandı\nAd: {}\nYas: {}".format(entryAd.get(),yas)


win = Tk()
win.title("uygulama")
win.geometry("500x500")

v1 = IntVar()

lblAd = Label(win,text="AD: ")
lblDogumTar = Label(win,text="Dogum Tar: ")
entryAd = Entry(win)
entryDogumTar = Entry(win)
checkKvvk = Checkbutton(win,text="KVKK",variable=v1,onvalue=0,offvalue=1)
btnKaydet = Button(win,text="Kaydet",command=kontrol)
lblSonuc = Label(win,text="")

lblAd.grid(row=0,column=0,sticky=W)
lblDogumTar.grid(row=1,column=0,sticky=W)
entryAd.grid(row=0,column=1,sticky=E)
entryDogumTar.grid(row=1,column=1,sticky=E)
checkKvvk.grid(row=2,column=1,sticky=E)
btnKaydet.grid(row=3,column=1,sticky=E)
lblSonuc.grid(row=5,column=2,sticky=W)


def kontrol():
    tarih = entryDogumTar.get().split("-")[2]
    yas = 2022 - int(tarih)
    if v1.get() == 1 or yas<18:
        lblSonuc["text"]="Lutfen kvvk onaylayın ve 18 yasından kucuksundur"

    elif v1.get() == 0 and yas>18:
        lblSonuc["text"]="Onaylandı\nAd: {}\nYas: {}".format(entryAd.get(),yas)


win.mainloop()