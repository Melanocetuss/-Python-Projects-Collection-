import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
from sklearn.preprocessing import LabelEncoder

df= sns.load_dataset("titanic")
le = LabelEncoder()
le.fit_transform(df["sex"])[0:5]
le.inverse_transform([0,1])


def label_encoder(dataframe, binary_col):
    le = LabelEncoder()
    dataframe[binary_col]=le.fit_transform(dataframe[binary_col])
    return dataframe
df= sns.load_dataset("titanic")

label_encoder(df,"sex")

binary_col = [col for col in df.columns if df[col].dtype not in ["int","float"] and df[col].nunique()==2]

for col in binary_col:
    label_encoder(df,col)

df.head()

df["embarked"].nunique()
df["embarked"].value_counts()
#len(df["embarked"].unique())

#One-HOt Encoder
#Pandas içindeki get_dummies() fonkisyonu

df= sns.load_dataset("titanic")

pd.get_dummies(df,columns=["embarked"]).head()
pd.get_dummies(df,columns=["embarked"],drop_first=True).head()
pd.get_dummies(df,columns=["embarked"],dummy_na=True).head()

#2 sınıflı

pd.get_dummies(df,columns=["sex"],drop_first=True)

pd.get_dummies(df,columns=["sex","embarked"],drop_first=True)

def one_hot_encoder(dataframe,categorical_col,drop_first=True):
    dataframe= pd.get_dummies(dataframe,columns=[categorical_col],drop_first=drop_first)
    return dataframe

one_hot_encoder(df,"sex")

