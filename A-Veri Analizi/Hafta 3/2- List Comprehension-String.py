#LC - 2

ogrenciler = ["Şehmus","Uğur","Berke","Beste","Sibel","Müge","Enes"]
ogrenciler_no = ["Şehmus","Berke","Müge"]

#1. Yöntem
[eleman.lower() if eleman in ogrenciler_no else eleman.upper() for eleman in ogrenciler]

#2.Yöntem
[eleman.upper() if eleman not in ogrenciler_no else eleman.lower() for eleman in ogrenciler]

