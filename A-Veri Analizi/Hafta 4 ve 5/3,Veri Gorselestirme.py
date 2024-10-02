#VERİ GÖRSELLEŞTİRME

#MATPLOTLIB & SEABORN

#MATPLOTLIB

#Kategorik : sütun grafik, countplot bar
#Sayısal: hist, boxplot

#KATEGORİK VERİ GÖRSELLEŞTİRME

#Kategorik : sutun grafik, countplot bar
#Sayisal: hist, boxplot

#KATEGORIK VERI GORSERLESTIRME
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind="bar")
plt.show()

#Sayisal  Degisken Gorselestirme
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df.head()

df["age"]

plt.hist(df["age"])
plt.show()

plt.hist(df["fare"])
plt.show()

#
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")
df.head()

#Kategorik Degisken ->Sutin, countplot bar
#sayisal -> hist, boxplot

df["sex"].value_counts()

df["sex"].value_counts().plot(kind="bar")
plt.show()

plt.hist(df["age"])
plt.show()

#Istatistik
#betimsel Istatistik - ortalama min max
#Cikarimsal IStatistik - 