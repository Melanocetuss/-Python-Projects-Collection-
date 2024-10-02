# Dictionary - key:Value
sozluk = {"BRK":"BURAK",
          "UGR":"UGUR",
          "CSR":"CESUR"}

print(sozluk["BRK"])

sozluk2 = {"BRK":["GAZIANTEP",34],
           "UGR":["IZMIR",23],
           "CSR":["ISTANBUL",25]}

print(sozluk2["BRK"][0])

#KEY sotgulama
print("BRK" in sozluk2)
print("TRK" in sozluk2)

#Value Degistirme
sozluk["BRK"] = ["ANKARA",56]
print(sozluk)

#key ve value ulasmak
sozluk.keys()
sozluk.values()

#key - value gunceleme
sozluk.update({"UGR":35})

