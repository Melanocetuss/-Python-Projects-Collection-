#######################
# Uygulama - Mülakat Sorusu
#######################

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

#Çift olan indekslerde -> Harf büyür
#Tek olan indekslerde -> Harf Küçülmüş

cumle = "hi my name is john and i am learning python"
def ciftIndexleriBuyukHarfYap(cumle):
    cumle2 = ""
    list = cumle.split(" ")
    for i in range(0,len(list),1):
        temp = list[i]
        for j in range(0,len(temp),2):
            temp = temp[:j] + temp[j].upper() + temp[j+1:]

        if cumle2 == "":
            cumle2 += temp
        else:
            cumle2 += " " + temp
    return cumle2
print(ciftIndexleriBuyukHarfYap(cumle))

