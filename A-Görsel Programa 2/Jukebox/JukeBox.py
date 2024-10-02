from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk
import customtkinter
import sqlite3
import pandas as pd
from tabulate import tabulate

def tkinterMekanSil():
    def delete(id):
        conn = sqlite3.connect("Jukebox.db")
        cursor = conn.cursor()

        cursor.execute("Delete From tbl_mekan WHERE rowid=" + id)
        messagebox.showinfo("Jukebox", "Islem Basarili")

        conn.commit()
        conn.close()

    rootD = Tk()
    rootD.resizable(False, False)
    rootD.title("JukeBox")
    rootD.geometry("300x150+1310+530")
    #rootD.iconbitmap("img/JukeBox.ico")
    rootD.config(bg="black")

    lblSil = customtkinter.CTkLabel(rootD, text="Silme Ekrani", text_color="White", font=("Arial", 25))
    lblSil.pack()
    frameD = Frame(rootD, bg="black")
    frameD.pack(pady=30)

    lblID = customtkinter.CTkLabel(frameD, text="ID", text_color="White")
    entryID = customtkinter.CTkEntry(frameD)
    btnSil = customtkinter.CTkButton(frameD, text="Sil", width=50, command=lambda: delete(entryID.get()))

    lblID.grid(row=0, column=0, sticky=W)
    entryID.grid(row=0, column=1)
    btnSil.grid(row=1, column=1,pady=5,sticky=E)

    rootD.mainloop()


def tkinterGuncelle():
    def mekanGuncelle(id, uyelikTuru, uyelikSonTarih):
        mekanKayit = [uyelikTuru, uyelikSonTarih, id]
        conn = sqlite3.connect("Jukebox.db")
        cursor = conn.cursor()

        cursor.execute("UPDATE tbl_mekan SET mekanUyelikTuru=?, uyelikSonBulmaTar=? WHERE rowid=?", mekanKayit)

        conn.commit()
        conn.close()
        messagebox.showinfo("Mekan Ekleme", "Islem Basarili")

    rootu = Tk()
    rootu.resizable(False, False)
    rootu.title("JukeBox")
    rootu.geometry("400x230+50+200")
    rootu.iconbitmap("img/JukeBox.ico")
    rootu.config(bg="black")

    lblMekanEkle = customtkinter.CTkLabel(rootu, text="Mekan Guncelleme Ekrani", font=("Arial", 20))
    lblMekanEkle.pack()
    frameMekanEkle = Frame(rootu, bg="black")
    frameMekanEkle.place(x=80, y=60)

    lblID = customtkinter.CTkLabel(frameMekanEkle, text="ID:", text_color="White")
    entryID = customtkinter.CTkEntry(frameMekanEkle)
    lblMekanUyelikTuru = customtkinter.CTkLabel(frameMekanEkle, text="Mekan Uyelik Türü:", text_color="White")
    uyelikTurleri = ["Kullanim Bedeli Odemeli", "Gelen Istek Ucretinden Komisyonlu"]
    combaBoxMekanUyelikTuru = customtkinter.CTkComboBox(frameMekanEkle, values=uyelikTurleri)
    lblMekanUyelikSonBulmaTarihi = customtkinter.CTkLabel(frameMekanEkle, text="Uyelik Son Tarih:", text_color="White")
    entryMekanUyelikSonBulmaTarihi = customtkinter.CTkEntry(frameMekanEkle)
    btnGuncelle = customtkinter.CTkButton(frameMekanEkle, text="Guncelle", width=50,
                                          command=lambda: mekanGuncelle(entryID.get(),
                                                                        combaBoxMekanUyelikTuru.get(),
                                                                        entryMekanUyelikSonBulmaTarihi.get()))

    lblID.grid(row=0, column=0, pady=3, sticky=W)
    entryID.grid(row=0, column=1, pady=3, padx=3)
    lblMekanUyelikTuru.grid(row=1, column=0, pady=3)
    combaBoxMekanUyelikTuru.grid(row=1, column=1, pady=3, padx=3)
    lblMekanUyelikSonBulmaTarihi.grid(row=2, column=0, sticky=W, pady=3)
    entryMekanUyelikSonBulmaTarihi.grid(row=2, column=1, pady=3, padx=3)
    btnGuncelle.grid(row=3, column=1, pady=3, sticky=E)

    rootu.mainloop()    


def tkinterMekanEkle():
    def mekanEkle(mekanAd,MekanAdres,uyelikTuru,uyelikSonTarih):
        mekanKayit = [mekanAd, MekanAdres, uyelikTuru, uyelikSonTarih]
        conn = sqlite3.connect("Jukebox.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO tbl_mekan VALUES(?,?,?,?)", mekanKayit)

        conn.commit()
        conn.close()
        messagebox.showinfo("Mekan Ekleme", "Islem Basarili")


    root3 = Tk()
    root3.resizable(False, False)
    root3.title("JukeBox")
    root3.geometry("400x300+1310+200")
    root3.iconbitmap("img/JukeBox.ico")
    root3.config(bg="black")

    lblMekanEkle= customtkinter.CTkLabel(root3,text="Mekan Ekleme Ekrani",font=("Arial",25))
    lblMekanEkle.pack()
    frameMekanEkle = Frame(root3, bg="black")
    frameMekanEkle.place(x=80,y=60)

    lblMekanAd = customtkinter.CTkLabel(frameMekanEkle, text="Mekan Ad:", text_color="White")
    entryMekanAd = customtkinter.CTkEntry(frameMekanEkle)
    lblMekanAdres = customtkinter.CTkLabel(frameMekanEkle, text="Mekan Adres:", text_color="White")
    entryMekanAdres = customtkinter.CTkEntry(frameMekanEkle)
    lblMekanUyelikTuru = customtkinter.CTkLabel(frameMekanEkle, text="Mekan Uyelik Türü:", text_color="White")
    uyelikTurleri=["Kullanim Bedeli Odemeli","Gelen Istek Ucretinden Komisyonlu"]
    combaBoxMekanUyelikTuru = customtkinter.CTkComboBox(frameMekanEkle,values=uyelikTurleri)
    lblMekanUyelikSonBulmaTarihi = customtkinter.CTkLabel(frameMekanEkle, text="Uyelik Son Tarih:", text_color="White")
    entryMekanUyelikSonBulmaTarihi = customtkinter.CTkEntry(frameMekanEkle)
    btnEkle = customtkinter.CTkButton(frameMekanEkle,text="Ekle",width=50,command=lambda: mekanEkle(entryMekanAd.get(),
                                                                                                    entryMekanAdres.get(),
                                                                                                    combaBoxMekanUyelikTuru.get(),
                                                                                                    entryMekanUyelikSonBulmaTarihi.get()
                                                                                                    ))

    lblMekanAd.grid(row=0, column=0, sticky=W,pady=3)
    entryMekanAd.grid(row=0, column=1,pady=3,padx=3)
    lblMekanAdres.grid(row=1, column=0, sticky=W,pady=3)
    entryMekanAdres.grid(row=1, column=1,pady=3,padx=3)
    lblMekanUyelikTuru.grid(row=2, column=0,pady=3)
    combaBoxMekanUyelikTuru.grid(row=2, column=1,pady=3,padx=3)
    lblMekanUyelikSonBulmaTarihi.grid(row=3, column=0, sticky=W,pady=3)
    entryMekanUyelikSonBulmaTarihi.grid(row=3, column=1,pady=3, padx=3)
    btnEkle.grid(row=4, column=1, pady=3,sticky=E)

    root3.mainloop()


def showData():
    def refresh():
        textBox.delete(1.0, tk.END)
        conn = sqlite3.connect('Jukebox.db')
        cursor = conn.cursor()

        cursor.execute("SELECT rowid,* FROM tbl_mekan")
        veriler = cursor.fetchall()

        conn.close()
        # Veri tablosu oluşturma
        df = pd.DataFrame(veriler, columns=['ID','mekanAd', 'mekanAdres', 'mekanUyelikTuru', 'mekanSonBulmaTar'])
        # Veri tablosunu ASCII tablosu olarak formatlama
        ascii_tablo = tabulate(df, headers='keys', tablefmt='psql')
        # ASCII tablosunu Text widget'ına yazdırma
        textBox.insert(tk.END, ascii_tablo)

    rootM = Tk()
    rootM.resizable(False, False)
    rootM.iconbitmap("img/JukeBox.ico")
    rootM.title("JukeBox")
    rootM.geometry("860x440+450+200")
    rootM.config(bg="black")

    frameTextBox = Frame(rootM)
    frameTextBox.grid(row=0, column=0)
    textBox = tk.Text(frameTextBox, width=860, bg="black", fg="yellow")
    textBox.grid(row=0, column=0)
    refresh()

    frameButtons = Frame(rootM, bg="black")
    frameButtons.place(x=0, y=395)

    btnRefresh = customtkinter.CTkButton(frameButtons, text="Yenile", width=50, command=refresh)
    btnMekanEkle = customtkinter.CTkButton(frameButtons, text="Mekan Ekle",command=tkinterMekanEkle)
    btnMekanGuncelle= customtkinter.CTkButton(frameButtons, text="Mekan Guncelle",command=tkinterGuncelle)
    btnMekanSil = customtkinter.CTkButton(frameButtons, text="Mekan Sil",command=tkinterMekanSil)

    btnRefresh.grid(row=0, column=0, padx=5)
    btnMekanEkle.grid(row=0, column=1, padx=5)
    btnMekanGuncelle.grid(row=0, column=2, padx=5)
    btnMekanSil.grid(row=0, column=3, padx=5)

    rootM.mainloop()


def Login():
    def control():
        #=====================    SQL   ==========================
        conn = sqlite3.connect("Jukebox.db")
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM tbl_nickname_password""")
        results = cursor.fetchall()

        nicknames = []
        passwords = []

        for result in results:
            nicknames.append(result[0])
            passwords.append(result[1])

        conn.close()
        #==========================================================

        listLen = len(nicknames)
        check = False
        index = 0
        for i in range(0, listLen):
            if entryNickName.get() == nicknames[i] and entryPassword.get() == passwords[i]:
                check = True
                index = i
                break
            else:
                check = False

        if check == True:
            root2.destroy()
            showData()

        else:
            messagebox.showinfo("Giris", "Giris Basarisiz")


    root.destroy()
    root2 = Tk()
    root2.resizable(False, False)
    root2.title("JukeBox")
    root2.geometry("350x300+800+300")
    root2.iconbitmap("img/JukeBox.ico")
    root2.config(bg="black")


    frameLogo = Frame(root2,bg="black")
    frameLogo.place(x=0, y=0)
    frameLoginScreen= Frame(root2,bg="black")
    frameLoginScreen.place(x=60,y=85)

    img2Logo = Image.open("img/JukeBox.png").resize((50, 50))
    img2LogoTk = ImageTk.PhotoImage(img2Logo)
    img2Label = Label(frameLogo,image=img2LogoTk,bg="black")
    img2Label.grid(row=0,column=0)

    lblGiris = customtkinter.CTkLabel(frameLogo,text="GIRIS EKRANI",text_color="white",font=("Arial",25))
    lblNickname= customtkinter.CTkLabel(frameLoginScreen,text="Kullanıcı Adı:",text_color="white",font=("Arial",15))
    entryNickName= customtkinter.CTkEntry(frameLoginScreen,placeholder_text="Kullanınıcı Adı giriniz")
    lblPassword= customtkinter.CTkLabel(frameLoginScreen,text="Şifre:",text_color="white",font=("Arial",15))
    entryPassword = customtkinter.CTkEntry(frameLoginScreen,placeholder_text="Şifre giriniz",show="*")
    btnBaslat= customtkinter.CTkButton(frameLoginScreen,text="Giriş",width=50,command=control)

    lblGiris.grid(row=1,column=1,padx=3)
    lblNickname.grid(row=1,column=0,sticky=W,pady=8)
    entryNickName.grid(row=1,column=1,sticky=E,pady=8)
    lblPassword.grid(row=2,column=0,sticky=W,pady=8)
    entryPassword.grid(row=2,column=1,sticky=E,pady=10)
    btnBaslat.grid(row=3,column=1,sticky=E)

    root2.mainloop()


root = Tk()
root.resizable(False, False)
root.title("JukeBox")
root.geometry("600x600+650+200")
root.iconbitmap("img/JukeBox.ico")
root.config(bg="black")

frameJukeBox= Frame(root,bg="black")
frameJukeBox.place(x=180,y=150)

frameIpucu= Frame(root,bg="black")
frameIpucu.place(x=-15,y=380)


img1JukeBox= Image.open("img/JukeBox.png")
img1JukeBoxTk = ImageTk.PhotoImage(img1JukeBox)
img1Label = Label(frameJukeBox,image=img1JukeBoxTk,bg="black")
btnBaslat = customtkinter.CTkButton(frameJukeBox,text="Baslat",command=Login)

lblIpucu= customtkinter.CTkLabel(frameIpucu,text="İpucu: Bu sistem JukeBox üye olan kullanıcılarımızın üyelik\n             "
                                                 "bilgilerini görüntülemek ve işlemek için geliştirilen bir uygulamadır.",bg_color="black",font=("Arial",18))
lblIpucu.grid(row=0,column=0)


img1Label.grid(row=0,column=0)
btnBaslat.grid(row=1,column=0)

root.mainloop()