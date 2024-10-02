import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
from sklearn.preprocessing import LabelEncoder, StandardScaler , RobustScaler , MinMaxScaler

#Klasik Standartlamştırma yöntemi : Standart Scaling - > Mean()

df = sns.load_dataset("titanic")
ss = StandardScaler()
df["age_standart_scaler"] = ss.fit_transform(df[["age"]])
df["fare_standart_scaler"] = ss.fit_transform(df[["fare"]])
df.head()

#Robust Yöntemi *-> Median()
rs=RobustScaler()
df["age_robust_scaler"] = rs.fit_transform(df[["age"]])
df.head()


#MinMaxSclaer
mms = MinMaxScaler()
df["age_min_max_scaler"] = mms.fit_transform(df[["age"]])
df.head()



