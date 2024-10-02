#File Operation
#1
file = open("file.txt", "w", encoding="utf-8")
file.close()

#2
file2 = open("\\Users\\alpha\\OneDrive\\Masaüstü\\file.txt","w",encoding="utf-8")
file2.close()

#w kipi
file = open("file.txt", "w", encoding="utf-8")
file.write("Cesur Alphan Ellik\n")
file.write("Burak Evrentug\n")
file.close()

#a kipi
file = open("file.txt", "a", encoding="utf-8")
file.write("Hasan Emre\n")
file.write("Utku Kasirga\n")
file.close()

#Dosya Okuma Yontem 1
file = open("file.txt", "r", encoding="utf-8")
for col in file:
    print(col, end="")
file.close()

#Dosya Okuma Yontem 2
file = open("file.txt", "r", encoding="utf-8")
okunan = file.readlines()
print(okunan)
file.close()

#Dosya Okuma Yontem 3
with open("file.txt", "r", encoding="utf-8") as file:
    for col in file:
        print(col, end="")