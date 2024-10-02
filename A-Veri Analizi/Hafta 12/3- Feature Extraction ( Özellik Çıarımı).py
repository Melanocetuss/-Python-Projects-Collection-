import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
from sklearn.preprocessing import LabelEncoder, StandardScaler , RobustScaler , MinMaxScaler

df = sns.load_dataset("titanic")
df["new_alive_bool"] = df["alive"].notnull().astype("int")

df.head()

df.groupby("new_alive_bool").agg({"survived":"mean"})


#Textler Üzerinde Özellik Türetmek

df.head()

df["new_embarked_count"] = df["embarked"].str.len()
df.head()


df["NEW_FAMILY_SIZE"] = df["sibsp"] + df["parch"] +1
df["NEW_FAMILY_SIZE"].value_counts()

df.loc[(df["sex"]=="male") & (df["age"]<=21), "NEW_SEX_CAT"]= "youngmale"
df.loc[(df["sex"]=="male") & (df["age"]>21) & (df["age"]<50), "NEW_SEX_CAT"]= "maturemale"
df.loc[(df["sex"]=="male") & (df["age"]>=50) ,"NEW_SEX_CAT"]= "seniormale"


df.loc[(df["sex"]=="female") & (df["age"]<=21), "NEW_SEX_CAT"]= "youngfemale"
df.loc[(df["sex"]=="female") & (df["age"]>21) & (df["age"]<50), "NEW_SEX_CAT"]= "maturefemale"
df.loc[(df["sex"]=="female") & (df["age"]>=50) ,"NEW_SEX_CAT"]= "seniorfemale"

df["NEW_SEX_CAT"].value_counts()

df.groupby("NEW_SEX_CAT").agg({"survived":"mean"})
df.head()