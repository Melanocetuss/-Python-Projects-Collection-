myString = "hello word iam burak"

#Upper
print(myString.upper())

#lower
print(myString.lower())

#Capitalize - ilk harfi buyuk yapar
print(myString.capitalize())

#Title
print(myString.title())

#SwapCase = buyuk harf ve kucuk harfleri kucultur
print(myString.swapcase())

#len
print(len(myString))

#slicing - string kesme
print(myString[0:7])
print(myString[6:])
print(myString[6:len(myString)])
print(myString[:10])

#index iele cagirma
print(myString[0])

#Split - Parcalar
list =myString.split(" ")
print(list[0])
