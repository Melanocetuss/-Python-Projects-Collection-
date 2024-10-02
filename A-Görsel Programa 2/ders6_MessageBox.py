from tkinter import *
from tkinter import messagebox

win= Tk()
win.title("APP")
win.geometry("400x400")
win.config(bg="black")

kontrolLabel = Label(win,text="",bg="black",fg="white")
kontrolLabel.grid(row=7,column=0,sticky=W)

def popup1():
    messagebox.showinfo("Bilgi","Bu yazalim Cesur tarafindan yapilmistir")
def popup2():
    messagebox.showwarning("Bilgi","Uyari")
def popup3():
    messagebox.showerror("Bilgi","hata")
def popup4():
    cevap = messagebox.askquestion("Bilgi", "devam etmek istiyor musunuz")
    if cevap == "yes":
        win.destroy()
        newWin1 = Tk()
        newWin1.title("Yes")
        newWin1.geometry("200x200")
        newWin1.config(bg="green")

        newWin1.mainloop()
    elif cevap == "no":
        win.destroy()
        newWin2 = Tk()
        newWin2.title("No")
        newWin2.geometry("200x200")
        newWin2.config(bg="red")

        newWin2.mainloop()
def popup5():
    cevap = messagebox.askokcancel("Bilgi", "devam etmek istiyor musunuz")
    if cevap == "yes":
        win.destroy()
        newWin1 = Tk()
        newWin1.title("Yes")
        newWin1.geometry("200x200")
        newWin1.config(bg="green")

        newWin1.mainloop()
    elif cevap == "no":
        win.destroy()
        newWin2 = Tk()
        newWin2.title("No")
        newWin2.geometry("200x200")
        newWin2.config(bg="red")

        newWin2.mainloop()
def popup6():
    cevap = messagebox.askyesno("Bilgi", "devam etmek istiyor musunuz")
    if cevap == "yes":
        win.destroy()
        newWin1 = Tk()
        newWin1.title("Yes")
        newWin1.geometry("200x200")
        newWin1.config(bg="green")

        newWin1.mainloop()
    elif cevap == "no":
        win.destroy()
        newWin2 = Tk()
        newWin2.title("No")
        newWin2.geometry("200x200")
        newWin2.config(bg="red")

        newWin2.mainloop()


popUpButton= Button(win,text="Show Info",command=popup1)
popUpButton2= Button(win,text="Show Warning",command=popup2)
popUpButton3= Button(win,text="Show Error",command=popup3)
popUpButton4= Button(win,text="Show Question",command=popup4)
popUpButton5= Button(win,text="Show Question",command=popup5)
popUpButton6= Button(win,text="Show Question",command=popup6)

popUpButton.grid(row=0,column=0,sticky=W)
popUpButton2.grid(row=1,column=0,sticky=W)
popUpButton3.grid(row=2,column=0,sticky=W)
popUpButton4.grid(row=3,column=0,sticky=W)
popUpButton4.grid(row=4,column=0,sticky=W)
popUpButton5.grid(row=5,column=0,sticky=W)
popUpButton6.grid(row=6,column=0,sticky=W)

win.mainloop()