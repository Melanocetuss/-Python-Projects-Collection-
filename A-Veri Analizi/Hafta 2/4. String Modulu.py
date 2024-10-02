import string
import random

def sifreOlustur(uzunluk):
    harfler = string.ascii_letters #ascii karakterlerini sarayla yazar
    numaralar = string.digits
    semboller = string.punctuation
    tumKarakterler =harfler+numaralar+semboller
    sifre = " "

    for i in range(uzunluk):
        sifre += random.choice(tumKarakterler)
    return sifre

print(sifreOlustur(8))

