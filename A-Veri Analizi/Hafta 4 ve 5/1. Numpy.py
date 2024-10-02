# Veri Analizi
#Numpy -> Matematik kutuphanesi : Hizli yapar
#Pandas -> Veri Analizi
#Seaborn (Mathplotlib) - > Veri Goresellestirme

#numpy
import numpy as np
a = [1,2,3,4]
b = [2,3,4,5]
ab=[]
for i in range(0,len(a)):
    ab.append(a[i]*b[i])
print(ab)

x = np.array([1,2,3,4])
y = np.array([2,3,4,5])
print(x*y)

#Numpy Array Olusturma

z = np.array(1,2,3,4,5)
type(z)

####Tek boyutlu Array####

#Bir ve Sifirdan olusuan Arrau
#np.zeros(10, dtype=int)
#np.ones(5, dtype=int)

#Random Array
#np.random.randint(0, 10, size=10)

#Iki boyutlu Array (Matris)
#np.random.randint(0, 10, size=(3,4))

#Numpy Array ozelikleri

#ndim -> boyut sayisini
#shape -> boyut bilgisi
#size -> toplam elaman sayisi
#dtype -> veri turu

a = np.random.randint(0, 10, size=10)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)

b = np.random.randint(0, 10, size=(5,6))
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)

#Reshaping  ***
a = np.random.randint(1, 10, size=9)
b = a.reshape(3,3)
print(a)
print(b)

#Index Secim
list = np.random.randint(0, 10, size=10)
list[0]
list[0:5]
list[0]=999

list2 = np.random.randint(10, size=(3,5))
print(list2)
print(list2[:,0])
print(list2[1,:])

#matris liste bolme
print(list2[1:3, 1:4])

#fancy Index
v=np.arange(0,30,3)
getir = [0,3,6]
v[getir]

v=np.arange(0,30,3)
ab=[]

for i in v:
    if i<10:
        ab.append(i)
#Numpy
v[v<10]
v[v>10]
v[v!=9]
v[v==3]

#Matematiksel islemler
t = np.array([1,2,3,4,5])
t/5
t**2
t-1
t*5/10

#Fonsiyonlar
np.subtract(t,1) #Cıkarma
np.add(t,2) #toplama
np.mean(t) #ortalama
np.sum(t) #toplam
np.min(t)
np.max(t)
np.var(t) #varyans

#Iki bilinmeyenli denklemler
# 5*x0 + x1 =12
# x0 + 3*x1 =10

a = np.array([[5,1],[1,3]])
b = np.array([12,10])

np.linalg.solve(a,b)