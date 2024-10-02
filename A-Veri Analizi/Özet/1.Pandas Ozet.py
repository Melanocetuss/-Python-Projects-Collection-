import seaborn as sns
import pandas as pd

pd.set_option("display.max_columns",None) # -> CONSOLE AYARI
pd.set_option("display.width",500) # -> CONSOLE AYARI
df = sns.load_dataset("titanic")

df["sex"].value_counts() # Kategorik ->toplam sinif sayisini getirir

#Degiskenler Uzerinde islemler

#Degisken uretmek
df["yeni_age"] = df["age"]*2
#Degiken silme
df.drop(1,axis=0,inplace=True) # axis=0 -> Satir siler(Veri siler)
df.drop("age",axis=1,inplace=True) # axis=1 -> Stun siler
#------

#LOC ile birden fazla kosul
df.loc[(df["age"]>50) & (df["sex"] == "male") &
(df["pclass"] == 1) &
((df["embark_town"] == "Southampton") | (df["embark_town"] == "Queenstown")),
["age","sex","pclass","embark_town","deck","alive"]]
#--------

#GROUP BY
                            # -> count(),first(),last(),mean(),meadian(),min(),max(),std(),var(),sum() <-
#tek groupby tek fonksiyon
df.groupby("sex")["age"].mean()
#tek groupby birden fazla fonksiyon
df.groupby("sex").agg({"age":["sum","mean"]})
#Birden fazla groupby birden fazla fonksiyon
df.groupby(["sex","embark_town","pclass"]).agg({"age":["mean","sum"],"survived":"mean"})
#--------------

#Apply
df["age2"] = df["age"]*2
df["age3"] = df["age"]*5
df[["age","age2","age3"]].apply(lambda x: x/10)
#age1,age2,age3 -> degiskenlerin satirlanrini lambda islemi yapar

#Dataframe birlestirme
import numpy as np
import pandas as pd

m = np.random.randint(0,30, size=(5,3))
df1 = pd.DataFrame(m,columns=["var1","var2","var3"])

n = np.random.randint(0,30, size=(5,3))
df2 = pd.DataFrame(n,columns=["var1","var2","var3"])

dfson = pd.concat([df1,df2])

dfson = pd.concat([df1,df2], ignore_index=True)
# ignore_index=True indexleri kaldigi yerden devam eder

#Merge
df1 = pd.DataFrame({"calisanlar":["John","Dennis","Mark","Maria"],"grup":["Muhasebe","Muhendis","Muhendis","IK"]})
df2 = pd.DataFrame({"calisanlar":["John","Dennis","Mark","Maria"],"ise_giris":[2010,2009,2014,2019]})
df3 = pd.merge(df1,df2) # ->Calisanlari sozlunu kulanarak merge islemi

df4 = pd.DataFrame({"grup":["Muhasebe","Muhendis","IK"],"mudur":["Ugur","Beste","Burak"]})
df5 = pd.merge(df3,df4)# -> grup kulanarak merge islemi
