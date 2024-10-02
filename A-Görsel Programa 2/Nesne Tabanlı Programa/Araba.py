class Araba():
    def  __init__(self,model,yakit,renk,yil,motor):
        self.modeli = model
        self.yakitTuru = yakit
        self.rengi = renk
        self.yili = yil
        self.motorHacmi = motor

    def tumBilgileriGoster(self):
        print("""
        Arabanin Modeli: {}
        Arabanin Yakit Turu: {}
        Arabanin rengi: {}
        Arabanin Yili {}
        Arabinin Motor Hacmi {}
        """.format(self.modeli,self.yakitTuru,self.rengi,self.yili,self.motorHacmi))

    def arabaninRenginiDegistir(self,yeniRenk):
        self.rengi = yeniRenk
    def arabaninYiliniArtir(self,artisMiktari):
        self.yili += artisMiktari
    def yakitTuruEkle(self,yeniTur):
        self.yakitTuru.append(yeniTur)

cesur = Araba("Tesla Model x", ["Elektrikli"],"Siyah",2022,"1.8")
cesur.arabaninRenginiDegistir("Yesil")
cesur.arabaninYiliniArtir(5)
cesur.yakitTuruEkle("Benzin")
cesur.tumBilgileriGoster()


