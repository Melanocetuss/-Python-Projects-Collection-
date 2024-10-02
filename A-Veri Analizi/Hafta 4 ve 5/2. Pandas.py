#PANDAS -> Veri Manipulasyonu

#Seri kavrami
#Data Frame

#Pandas Series
#Veri Okuma (Reading Data)
#Veriye Hizli Bakis
#Secim islemleri
#Toplulastirma ve Gruplama
#Apply ve lambda
#Birlestirme (join) islemleri

#Pandas Serisi

import pandas as pd

a= pd.Series([10,77,12,4,5])
type(a)

a.index
a.dtype
a.size
a.ndim
a.values

type(a.values)

a.head() #ilk bes veriyi getirir
a.tail() #son bes veriyi getirir

#Reading Data
#CSV*** & SQL & PARGUET & Seaborn & EXCEL

df = pd.read_csv("YeniDonem/Veri Dosyalari/reklam.csv")
df.head()

import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

#Veri Biliminde Veri Turleri
#Sayisal veri -> int,float
#kategorik -> Kategorilere ayrilan veri turudur : sex, embark_town, alive, alone

#Veriye Hizli Bakis
df.head()
df.tail()
df.shape #->891 satir, 15 sutun(Baslik, feature, degisken, index)
df.info()
df.columns
df.index

df.isnull().values.any() # Veri doyamda bosluk var mi
df.isnull().values.sum() #Toplam 0 bos veri satır sayisi

df["sex"].head()

#Kategorik degisken sininifini bulmak
df["sex"].value_counts() #Kategorik

df["embark_town"].value_counts()

#5.Hafta
#Pandas'ta secim islemleri
df = sns.load_dataset("titanic")
df.head()

df["age"]

df[0:13]

#->Drop Etme
#Gecici silme
df.drop(0,axis=0).head() #axix 0 ise sutun 1 ise satir
#Kalici olarak silme
df.drop(0,axis=0,inplace=True)

#Degiskeni index Cevirme
df["age"].head()
df.index =df["age"]
df.drop("age",axis=1,inplace=True)

#index degerini degisken olarak atama
df.index
df["age"]= df.index
df.drop("age",axis=1,inplace=True)

df.reset_index() #Dataframe resetleme

#Degiskenler Uzerinde islemler
import pandas as pd
import  seaborn as sns

pd.set_option("display.max_columns",None)
df = sns.load_dataset("titanic")

"age" in df

df["age"]
df.age

getir = ["age","alive"]
df[getir]

df["age2"] = df["age"]*2 #Degisken uretmek
df["age3"] = df["age"] / df["age2"]

df.drop("age3",axis=1,inplace=True)

sil = ["age2","age3"]
df.drop(sil,axis=1,inplace=True)

#loc & iloc
#iloc -> Intager Based
df.iloc[0:3] #Ayni Yontem

#loc -> String Based
df.loc[0:3]

df.loc[0:3,0:3] #calismaz
df.loc[0:3,"age"]

getir = ["survived","pclass","sex"]
df.loc[0:3,getir]

#Pandasta Kosullu Islemler
import pandas as pd
import  seaborn as sns
pd.set_option("display.max_columns",None)
df = sns.load_dataset("titanic")

#Tek Kosul oldugunda
df["age"]>50
df[df["age"]>50]

df[df["age"]>50]["age"]

#1. Yontem
df[df["age"]>50][["age","sex"]]
#2. Yontem
catch=["age","sex"]
df[df["age"]>50][catch]

#loc kosular
df.loc[df["age"]>50,["age","sex"]]

#2 ya da daha fazla kosul oldugunda
"""
df["age"]>50
df["sex"]=="male"
"""
df.loc[(df["age"]>50) & (df["sex"]=="male"),"age"]

df.loc[(df["age"]>50) & (df["sex"]=="male"),["age","class"]]

#ben yasi 50 den buyuk ve cinsiyeti erkek olan ayni zamandada
#Cherboury yada Quennstown binenleri getir
"""
df["age"]>50
df["sex"]=="male"
df["embark_town"]=="Cherbourg"
df["embark_town"]=="Quennstown"
"""

#1. Yontem
df.loc[(df["age"]>50) & (df["sex"]=="male") &
       ((df["embark_town"]=="Cherbourg") | (df["embark_town"]=="Quennstown"))]
#2. Yontem
a=df["age"]>50
b=df["sex"]=="male"
c=df["embark_town"]=="Cherbourg"
d=df["embark_town"]=="Quennstown"
df.loc[(a) & (b) & ((c) | (d))]

#Toplulastirma - Gruplama (Aggregation & Grouping)
#count()
#first()
#last()
#mean()
#meadian()
#min()
#max()
#std()
#var()
#sum()
#- pivot table

import pandas as pd
import  seaborn as sns
pd.set_option('display.max_columns',None)
df = sns.load_dataset("titanic")

df.head()

df["age"].mean()
df["fare"].sum()
df["age"].sum()

df["fare"].std()
df["age"].std()

#Agg fonksiyonu
#1. Yontem
df.groupby("sex")["age"].mean()
df.groupby("sex")["fare"].mean()

#2. Yontem
df.groupby("sex").agg({"age":"mean"})
df.groupby("sex").agg({"age":["mean","sum"]})

df.groupby("sex").agg({"age":["mean","sum"],
                       "survived":"mean"})

df.groupby("embark_town").agg({"fare":["mean","sum"]})

df.groupby("embark_town").agg({"fare":["mean","sum"],
                               "pclass":"sum"})

df.groupby(["sex","embark_town"]).agg({"age":"mean",
                                     "survived":"mean"})

#Pivot Table
#Group By olarak yazilan degerler farkli bir bicimde gostermek
import pandas as pd
import  seaborn as sns
pd.set_option('display.max_columns',None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")

df.pivot_table("survived","sex","embark_town")

df.pivot_table("survived","sex",["embark_town","class"])

#Yas dagilimlari
#0-10, 10-18, 18-25, 25-40, 40-90

df["yeni_yas"] = pd.cut(df["age"],[0,10,18,25,40,90])
df.pivot_table("survived","sex",["yeni_yas","class"])

#Apply - lambda
#Eger df uzerinde degiskenlerinize bir islemler
import pandas as pd
import  seaborn as sns
pd.set_option('display.max_columns',None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

df.head()

#kolonlarin icinde age iceren degiskenler bakalim
#1. Yontem
for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        df[col] = df[col] / 10
#2. Yontem
df[["age","age2","age3"]].apply(lambda x: x/10)

df_son = df.loc[:,df.columns.str.contains("age")].apply(lambda a:a/10)

#Join Islemi
import numpy as np
import pandas as pd

m = np.random.randint(0,30, size=(5,3))
df1 = pd.DataFrame(m,columns=["var1","var2","var3"])

n = np.random.randint(0,30, size=(5,3))
df2 = pd.DataFrame(n,columns=["var1","var2","var3"])

dfson = pd.concat([df1,df2])

dfson = pd.concat([df1,df2], ignore_index=True)

#Merge islemi

df1 = pd.DataFrame({"calisanlar":["John","Dennis","Mark","Maria"],
                    "grup":["Muhasebe","Muhendis","Muhendis","IK"]})

df2 = pd.DataFrame({"calisanlar":["John","Dennis","Mark","Maria"],

                    "ise_giris":[2010,2009,2014,2019]})

df3 = pd.merge(df1,df2)

df4 = pd.DataFrame({"grup":["Muhasebe","Muhendis","IK"],
                    "mudur":["Ugur","Beste","Burak"]})

df5 = pd.merge(df3,df4)