while True:
    kilo = float(input("---|Kilonuzu giriniz(kg)|---\n"))
    boy = float(input("---|Boyunuzu Girniz(m)|---\n"))
    bki = kilo/(boy*boy)
    print("---|BKI:{}|---".format(bki))
    cikis = input("--- Cikmak icin c basin ---\n")
    if cikis == 'c':
        break
