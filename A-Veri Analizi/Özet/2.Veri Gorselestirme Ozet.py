import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df= sns.load_dataset("titanic")


#KATEGORIK -> Stun, plot(kind="bar")
df["sex"].value_counts().plot(kind="bar")
plt.show()
#2.Yontem
sns.countplot(x=df["sex"],data=df)
plt.show()


#SAYISAL -> hist(), boxplot()
plt.hist(df["age"])
plt.show()

df.describe().T  #-> Sayisal verlerin count, mean, min, max, std goruntuler

#->DISTPLOT<- SAYISAL
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df= sns.load_dataset("diamonds")

# kde=True ->  Grofige cizgi ekler
# bins-> Grafigi kac stunla gosterdigi
sns.distplot(df["price"],kde=True,bins=10)
plt.show()
#hist=False -> stunlari yok eder
sns.distplot(df["price"],kde=True,hist=False)
plt.show()
#shade=True cizginin altini doldurur
sns.kdeplot(df["price"],shade=True)

#->BOXPLOT()<- SAYISAL
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df= sns.load_dataset("tips")

# Tek degisken X Sayisal
sns.boxplot(x=df["total_bill"])
plt.show()

# X Kategorik , Y Sayisal
sns.boxplot(x="day", y="total_bill", data=df)
plt.show()

sns.boxplot(x="time", y="total_bill",data=df)
plt.show()

# X Kategorik , Y Sayisal , HUE Kategorik
sns.boxplot(x="day",y="total_bill",hue="sex",data=df)
plt.show()

# ->SCATTERPLOT<- SAYISAL
df.info()

sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df)
plt.show()

sns.scatterplot(x="total_bill", y="tip", hue="size", style="size",data=df)
plt.show()

sns.scatterplot(x="total_bill", y="tip", hue="size", style="time",data=df)
plt.show()

sns.scatterplot(x="total_bill", y="tip", hue="day", style="time",data=df)
plt.show()

