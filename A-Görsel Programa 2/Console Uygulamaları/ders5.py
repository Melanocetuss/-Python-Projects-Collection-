def cevreHesapla(kenar):
    cevre = 4*kenar
    print("Cevre:",cevre)


def alanHesapla(kenar):
    alan = kenar*kenar
    print("Alan:",alan)

while(True):
    print("""
        --- Menu ---
    1)Kare cevre bul
    2)kare alan bul
    3)Cikis
    --- --- --- --- ---
    """)
    choose = int(input("Seciminizi giriniz: "))
    kenar = int(input("Kenar degeri giriniz: "))
    if choose == 1:
        cevreHesapla(kenar)
    elif choose == 2:
        alanHesapla(kenar)
    elif choose == 3:
        break
    else:
        print("Yanlis Secim Yaptiniz")
