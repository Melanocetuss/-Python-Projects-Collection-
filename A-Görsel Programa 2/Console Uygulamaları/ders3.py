"""
liste = [54,76,54,32,56,7,90,654,32]
print("---Liste:",liste)
print("---|Listenin Son Elemani:",liste[-1],"|---",sep="")
print("---|Listenin Ilk Elemani:",liste[0],"|---",sep="")
print("---|Listenin Eleman Sayısı:",len(liste),"|---\n",sep="")


print("---|LISTEYE VERI EKLEME|---")
liste.append(586)
print("---|Liste Guncel Hali:",liste,"|---\n",sep="")

print("---|LISTE GUNCELEME|---")
liste[2]= 64
print("---|Liste Guncel Hali:",liste,"|---\n",sep="")


print("---|LISTEDEN VERI SILMEK|---")
liste.pop() # Son indexteki veriyi silme.
print("---|Liste Guncel Hali:",liste,"|---",sep="")
liste.pop(2)
print("---|Liste Guncel Hali:",liste,"|---",sep="")
liste.remove(7) # Listedeki girlen degeri listeden siler.
print("---|Liste Guncel Hali:",liste,"|---\n",sep="")


print("---|LISTE SIRALAMA|---")
liste.sort()
print("---|Liste Guncel Hali:",liste,"|---",sep="")
print("---|Listenin En Kucuk Elemani:",liste[0],"|---",sep="")
print("---|Listenin En Buyuk Elemani:",liste[-1],"|---",sep="")
liste.sort(reverse=True)
print("---|Ters siralama|---",liste,"\n")

liste2=[56,43,21]
print("---|Liste2 Normak Hali",liste2,"|---")
liste2.reverse()
print("---|Liste Ters Cevirme",liste2,"|---\n")
"""

notlar = [25,36,45,58,65,32,65,35,48]
isimler = ["Berk","Cem","Sibel"]

berk = notlar[0:3]
berkOrt = (berk[0]+berk[1]+berk[2])/3

cem = notlar[3:6]
cemOrt = (cem[0]+cem[1]+cem[2])/3

sibel= notlar[6:9]
sibelOrt = (sibel[0]+sibel[1]+sibel[2])/3

print("""
ADI: {}
N1: {}
N2: {}
N3: {}
Ortalama {}
""".format(isimler[0],berk[0],berk[1],berk[2],berkOrt))

print("""
ADI: {}
N1: {}
N2: {}
N3: {}
Ortalama {}
""".format(isimler[1],cem[0],cem[1],cem[2],cemOrt))

print("""
ADI: {}
N1: {}
N2: {}
N3: {}
Ortalama: {}
""".format(isimler[2],sibel[0],sibel[1],sibel[2],berkOrt))