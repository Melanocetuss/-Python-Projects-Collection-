import random
import time
class kumanda():

    def __init__(self, tvDurum = "Kapali", tvSes = 0, kanalListesi=["TRT"], kanal="TRT"):
        self.tvDurumu = tvDurum
        self.tvSesi = tvSes
        self.kanalListe = kanalListesi
        self.kanali = kanal

    def tvAc(self):
        if self.tvDurumu == "Acik":
            print("Tv zaten acik")
        else:
            print("Tv Aciliyor")
            time.sleep(1)
            self.tvDurumu = "Acik"
            print("Tv acildi")

    def tvKapat(self):
        if self.tvDurumu == "Kapali":
            print("zaten kapali")
        else:
            print("Tv Kapatiliyor")
            time.sleep(1)
            self.tvDurumu = "Kapali"
            print("Tv Kapandi")

    def sesAyarla(self):
        while True:
            cevap = input("Ses Acmak icin > \nSes Kapama icin < \nCikisi icin herhangi bir tus bas")
            if cevap == ">":
                if self.tvSesi <=100:
                    self.tvSesi +=1
                    print("Ses Seviyesi {}%".format(self.tvSesi))

            elif cevap == "<":
                if self.tvSesi != 0:
                    self.tvSesi -=1
                    print("Ses Seviyesi {}%".format(self.tvSesi))

            else:
                print("Ses Guncellendi\Ses Seviyesi {}%".format(self.tvSesi))
                break

    def kanalEkle(self,yeniKanal):
        print("Kanal Ekleniyor")
        time.sleep(1)
        self.kanalListe.append(yeniKanal)
        print("Kanal eklendi")

    def rastgeleKanalSec(self):
        rastgele = random.randint(0,len(self.kanalListe))
        self.kanali=self.kanalListe[rastgele]
        print("Suanki Kanal",self.kanali)

    def __len__(self):
        return len(self.kanalListe)

    def __str__(self):
        return "Tv Durumu {}\nSes Seviyesi {}%\nKanal Listesi {}\nSuanki Kanal {}".format(self.tvDurumu,self.tvSesi,self.kanalListe,self.kanali)


myKumanda = kumanda()
while True:
    print("""
    1. Tv Ac
    2. Tv Kapat
    3. Ses Ayarlari
    4. Kanal Ekle
    5. Kanal Sayisi Ogren
    6. Rastgele Kanal Sec
    7. Tv Bilgileri
    q. Cikis""")
    islem = input("Islem Seciniz\n")

    if islem == "q":
        print("Programdan Cikiliyor")
        break

    elif islem == "1":
        myKumanda.tvAc()

    elif islem == "2":
        myKumanda.tvKapat()

    elif islem == "3":
        myKumanda.sesAyarla()

    elif islem == "4":
        kanalIsimleri = input("Virgul Ile Kanalari Giriniz")
        kanalListem = kanalIsimleri.split(",")
        for i in kanalListem:
            myKumanda.kanalEkle(i)

    elif islem == "5":
        print("Kanal Sayisi:",len(myKumanda))

    elif islem == "6":
        myKumanda.rastgeleKanalSec()

    elif islem == "7":
        print(myKumanda)

    else:
        print("Yanlis Islem")
