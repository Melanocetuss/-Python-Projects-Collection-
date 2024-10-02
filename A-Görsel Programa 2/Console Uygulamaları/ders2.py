"""
urunFiyat=150
urunSekizlikKdv = urunFiyat + urunFiyat*8/100
urunOnlukKdv = urunFiyat + urunFiyat*10/100
urunOnsekizlikKdv = urunFiyat + urunFiyat*18/100
kdvS =urunFiyat*8/100
kdvO =urunFiyat*10/100
kdvOs =urunFiyat*18/100
print("--------------------------------------------\n---|Urun Fiyat = {}TL|---\n---|KDV Dahil Fiyat= {}TL KDV= {}TL|---\n---|KDV Dahil Fiyat= {}TL KDV= {}TL|---\n---|KDV Dahil Fiyat= {}TL KDV= {}TL|---\n--------------------------------------------\n".format(urunFiyat,urunSekizlikKdv,kdvS,urunOnlukKdv,kdvO,urunOnsekizlikKdv,kdvOs))
"""

not1 = float(input("Lutfen ilk notu giriniz:"))
not2 = float(input("Lutfen ikinci notu giriniz:"))
not3 = float(input("Lutfen Ucuncu notu giriniz:"))
ort = (not1+not2+not3)/3

print("N1:{}\nN2:{}\nN3:{}\nOrtlama:{}".format(not1,not2,not3,ort))