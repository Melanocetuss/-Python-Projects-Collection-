#List Comprehension

#1. Yöntem - Klasi Yöntem
maaslar = [1000,2000,3000,4000,5000]

def yeni_maas(maas):
    yeniMaas = maas + maas*20/100
    return yeniMaas

for eleman in maaslar:
    print(yeni_maas(eleman))

bos_liste = []

for eleman in maaslar:
    bos_liste.append(yeni_maas(eleman))

print(bos_liste)

bos_liste = []

for maas in maaslar:
    if maas>3000:
        bos_liste.append(yeni_maas(maas))
    else:
        bos_liste.append(maas)

#2- List Comprehension Yöntemi
maaslar = [1000,2000,3000,4000,5000]

# Tüm elemanları 2 ile çarp LC

[eleman*2 for eleman in maaslar]

#maas<3000 2 ile çarp - 1 tane koşul varsa

[maas * 2 for maas in maaslar if maas<3000]

#maas<3000 ise %20 zam yapan fonksiyonu kullan değilse maaş değerini 2 ile çarp


[maas*2 if maas <=3000 else maas*3 for maas in maaslar]

#[maas+maas*20/100 if maas <3000 else maas*2 for maas in maaslar]

[maas + maas*20/100 if maas<3000 else maas*2 for maas in maaslar]

#Araştırma: LC elif kullanılmaz. Bu durumlarda nasıl bir kullanım gerçekleştirilir.

[maas + maas*20/100 if maas<3000 else maas*10 if maas<2000 else maas*2 for maas in maaslar]

