import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Kategorik Değişken -> Sütun, Countplot bar
#Ssayısal-> Hist, boxplot

df = sns.load_dataset("titanic")
df.head()
df.info()

#Kategorik
df["sex"].value_counts()

df["sex"].value_counts().plot(kind="bar")
plt.show()

#Sayısal
df["age"]
plt.hist(df["age"])

#İSTATİSTİK

#Betimsel İstatistik -> ortalama, min, max, count
#Çıkarımsal İstatistik -> Betimsel istatistiksel değerleri kullanarak çıkarımlar yaptığımız türdür.

#Betimsel İstatistik

#Ortalama (Aritmetik Ortalama) - Mean(), 4 3 1 6 1 7 -> ortalama = 3.6
#Median - Ortanca -> 4 3 1 6 1 7 -> 1 1 3 4 6 7 > (3+4)/2 = 3.5    Tek = 4 3 1 6 1 7 9  -> 1 1 3 4 6 7 9 -> Median = 4
#Mod: Veri setinde en çok tekrar eden değerdir. 4 3 1 6 1 7 -> 1

#Median

#12,56,35,48,96,100,2000,9750,10000 -> Ortalama = 13.208
#Median hesaplama = 12 35  48 56 96 100 2000 9750 10000 _> Median 96

#Betimsel İstatistik

df.describe()

df.describe().T

#SEABORN

import seaborn as sns

df = sns.load_dataset("tips")
df.head()
df.info()

df["sex"].value_counts()
df["smoker"].value_counts()
df["day"].value_counts()
df["time"].value_counts()

df.describe().T

plt.hist(df["total_bill"])
plt.show()

#SEABORN

sns.countplot(x=df["sex"],data=df)
plt.show()

df["sex"].value_counts().plot(kind="bar")
plt.show()

#Seaborn kütüphanesinin içerisinde diamonds

df = sns.load_dataset("diamonds")
df.info()
df.describe().T

sns.distplot(df["price"])
plt.show()

sns.distplot(df["price"], kde=False)
plt.show()

sns.distplot(df["price"], kde=True)
plt.show()


sns.displot(df["price"],bins=100)
plt.show()

sns.displot(df["price"], bins=1000)
plt.show()

sns.displot(df["price"], bins=10000)
plt.show()


#Sadece yoğunluk grafiği için

sns.distplot(df["price"],hist=False)
plt.show()

sns.distplot(df["price"],hist=False)
plt.show()

sns.kdeplot(df["price"],shade=True)
plt.show()

#BOXPLOT
import seaborn as sns
df= sns.load_dataset("tips")
sns.boxplot(x=df["total_bill"],data=df)
plt.show()

#Hangi gün ne kadar kazanılmıştır? #day #total_bill

sns.boxplot(x="day",y="total_bill",data=df)
plt.show()

#Sabah mı yoksa akşam mı çok kazanılıyor?

sns.boxplot(x="time",y="total_bill",data=df)
plt.show()

sns.boxplot(x="time",y="total_bill",hue="sex",data=df)
plt.show()


#ScatterPlot -> Sayısal Değişkenler arasındaki ilişkiyi gösterir

import seaborn as sns
df= sns.load_dataset("tips")

sns.scatterplot(x="total_bill",y="tip",data=df)
plt.show()

sns.scatterplot(x="total_bill",y="tip",hue="time",data=df)
plt.show()

sns.scatterplot(x="total_bill",y="tip",hue="size",data=df)
plt.show()

sns.scatterplot(x="total_bill",y="tip",hue="size",style="time",data=df)
plt.show()

sns.scatterplot(x="total_bill",y="tip",hue="day",style="time",data=df)
plt.show()


