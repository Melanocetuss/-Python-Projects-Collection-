#Kategorik Degisken Analizi
#Sayisal Degisken Analizi
#Hedef Degisken Analizi
#Korelasyon Analizi
#1- Genel Resim
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)

def check_df(dataframe):
    print("#############Shape#############")
    print(dataframe.shape)
    print("#############Type#############")
    print(dataframe.dtypes)
    print("#############Head#############")
    print(dataframe.head())
    print("#############Tail#############")
    print(dataframe.tail())
    print("#############NA#############")
    print(dataframe.isnull().sum())
    print("#############DESCRIBE#############")
    print(dataframe.describe().T)


def cat_summary(dataframe,col_name,plot=False):
    if dataframe[col_name].dtypes=="bool":
        dataframe[col_name]= dataframe[col_name].astype(int)

        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)
    else:
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)


def num_summary(dataframe,numarical_col,plot=False):
    print(dataframe[numarical_col].describe().T)
    if plot:
        dataframe[numarical_col].hist()
        plt.xlabel(numarical_col)
        plt.ylabel(numarical_col)
        plt.show(block=True)


def grab_col_names(dataframe,cat_th=10,car_th=20):
    cat_cols = [col for col in dataframe.columns if str(dataframe[col].dtypes) in ["catagory", "object", "bool"]]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and dataframe[col].dtypes in ["int", "float"]]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and str(dataframe[col].dtypes) in ["catagory", "object", "bool"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]
    return cat_cols, num_cols, cat_but_car


def outlier_thresholds(dataframe,col_names,q1=0.25,q3=0.75):
    q1 = dataframe[col_names].quantile(q1)
    q3 = dataframe[col_names].quantile(q3)
    iqr = q3 - q1
    up_limit = q3 + 1.5 * iqr
    low_limit = q1 - 1.5 * iqr
    return up_limit,low_limit


df= sns.load_dataset("titanic")
#check_df() TEST
check_df(df)

#grap_col_names() TEST
cat_cols,num_cols,cat_but_car=grab_col_names(df)
print("Cat",cat_cols)
print("Num",num_cols)
print("Car",cat_but_car)

#cat_summary() TEST
df2= sns.load_dataset("diamonds")
cat_summary(df2,"cut",plot=True)

#num_summary() TEST
for col in num_cols:
    num_summary(df,col)

#outlier_thresholds() TEST
up_limit,low_limit=outlier_thresholds(df,"age")
print("UP LIMIT:",up_limit)
print("LOW LIMIT",low_limit)
