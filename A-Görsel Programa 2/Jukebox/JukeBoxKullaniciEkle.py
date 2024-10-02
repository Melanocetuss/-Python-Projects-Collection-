import sqlite3
#Kullanici buradan olusturuluyor

nickname=input("Nickname Girin\n")
password=input("Sifre Girin\n")
nickname_password=[nickname,password]
conn = sqlite3.connect("Jukebox.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO tbl_nickname_password VALUES(?,?)",nickname_password)
print("islem basarili")

conn.commit()
conn.close()
