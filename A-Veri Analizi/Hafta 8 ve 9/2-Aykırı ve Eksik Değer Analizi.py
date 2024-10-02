#Aykırı Değer - Outliers

import numpy as np
import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)

df = sns.load_dataset("titanic")
sns.boxplot(x=df["age"])
q1 = df["age"].quantile(0.25)
q3 = df["age"].quantile(0.75)
iqr = q3-q1
low =q1-1.5*iqr
up = q3+1.5*iqr

df[(df["age"]<low) |(df["age"]>up)]
df[(df["age"]<low) |(df["age"]>up)].index

#Değişkenim de Aykırı Değer Var mı ?

df[(df["age"]<low) |(df["age"]>up)].any(axis=None)

def outlier_threshold(dataframe,col_name,q1=0.25,q3=0.75):
    q1 = dataframe[col_name].quantile(q1)
    q3 = dataframe[col_name].quantile(q3)
    iqr = q3 - q1
    low_limit = q1 - 1.5 * iqr
    up_limit = q3 + 1.5 * iqr
    return low_limit, up_limit

outlier_threshold(df,"fare")
low_limit, up_limit = outlier_threshold(df,"fare")

df[(df["fare"]<low_limit) | (df["fare"]>up_limit)]
df[(df["fare"]<low_limit) | (df["fare"]>up_limit)].index

def check_outlier(dataframe,col_name):
    low_limit, up_limit = outlier_threshold(dataframe, col_name)
    result = dataframe[(dataframe[col_name] < low_limit) | (dataframe[col_name] > up_limit)].any(axis=None)
    if result:
        return True
    else:
        return False

check_outlier(df,"age") # -> True
check_outlier(df,"fare") # ->True

def grap_col_names(dataframe,cat_th=10,car_th=20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.

    :parameter

    ------------
    dataframe : dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th : int, float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeridir.
    car_th : int,float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri

    :returns

    cat_cols : list
        Kategorik değişken listesi
    num_cols : list
        Numerik değişken listesi
    cat_but_car : list
        Kategorik görünümlü kardinal değişken listesi

    notes:
    Ek bilgi içermemektedir.


    """
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in df.columns if df[col].nunique() < cat_th and df[col].dtypes in ["int", "float"]]

    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > car_th and str(df[col].dtypes) in ["category", "object", "bool"]]

    cat_cols = cat_cols + num_but_cat

    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]

    num_cols = [col for col in num_cols if col not in cat_cols]

    print("Gözlem Sayısı",dataframe.shape[0])
    print("Değişken Sayısı",dataframe.shape[1])
    print("Kategorik Değişken Sayısı", len(cat_cols))
    print("Numerik Değişken Sayısı", len(num_cols))
    print("Kardinal olan Kategorik Değişkenler", len(cat_but_car))

    return cat_cols, num_cols , cat_but_car

cat_cols, num_cols , cat_but_car = grap_col_names(df)

for col in num_cols:
    print(col,check_outlier(df,col))

#Grap Outliers

def grab_outliers(dataframe,col_name,index=False):
    low_limit, up_limit = outlier_threshold(dataframe, col_name)
    aykiri = ((dataframe[col_name]<low_limit) | (dataframe[col_name]>up_limit))
    if aykiri.shape[0]>10:
        print(dataframe[aykiri].head())
    else:
        print(dataframe[aykiri])
    if index:
        aykiri_index = dataframe[aykiri].index
        return aykiri_index

grab_outliers(df,"age", index=True)

#Aykırı Değer Problemleri

#Silme
df = sns.load_dataset("titanic")

low_limit, up_limit = outlier_threshold(df,"fare")

aykiri = (df["fare"]<low_limit) | (df["fare"]>up_limit)
df[aykiri]
#1. Yöntem
yeni_df= df[~aykiri] #alt gr + ctrl + ü

#2. Yöntem
yeni_df= df[~((df["fare"]<low_limit) | (df["fare"]>up_limit))]

#alt gr + ctrl + ü -> tilda

def remove_outlier(dataframe,col_name):
    low_limit, up_limit = outlier_threshold(dataframe, col_name)
    yeni_df = dataframe[~((dataframe[col_name] < low_limit) | (dataframe[col_name] > up_limit))]
    return yeni_df

dff = remove_outlier(df,"fare")
def check_outlier(dataframe,col_name):
    low_limit, up_limit = outlier_threshold(dataframe, col_name)
    result = dataframe[(dataframe[col_name] < low_limit) | (dataframe[col_name] > up_limit)].any(axis=None)
    if result:
        return True
    else:
        return False

check_outlier(dff,"fare")

#Baskılama Yöntemi

df.loc[(df["fare"]<low_limit),"fare"] = low_limit

df.loc[(df["fare"]>up_limit),"fare"] = up_limit

check_outlier(df,"fare")

def replace_with_threshold(dataframe,col_name):
    low_limit, up_limit = outlier_threshold(dataframe, col_name)
    dataframe.loc[(dataframe[col_name] < low_limit), col_name] = low_limit
    dataframe.loc[(dataframe[col_name] > up_limit), col_name] = up_limit


replace_with_threshold(df,"age")
check_outlier(df,"age")

def grap_col_names(dataframe,cat_th=10,car_th=20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.

    :parameter

    ------------
    dataframe : dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th : int, float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeridir.
    car_th : int,float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri

    :returns

    cat_cols : list
        Kategorik değişken listesi
    num_cols : list
        Numerik değişken listesi
    cat_but_car : list
        Kategorik görünümlü kardinal değişken listesi

    notes:
    Ek bilgi içermemektedir.


    """
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in df.columns if df[col].nunique() < cat_th and df[col].dtypes in ["int", "float"]]

    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > car_th and str(df[col].dtypes) in ["category", "object", "bool"]]

    cat_cols = cat_cols + num_but_cat

    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]

    num_cols = [col for col in num_cols if col not in cat_cols]

    print("Gözlem Sayısı",dataframe.shape[0])
    print("Değişken Sayısı",dataframe.shape[1])
    print("Kategorik Değişken Sayısı", len(cat_cols))
    print("Numerik Değişken Sayısı", len(num_cols))
    print("Kardinal olan Kategorik Değişkenler", len(cat_but_car))

    return cat_cols, num_cols , cat_but_car


cat_cols, num_cols , cat_but_car= grap_col_names(df)

for col in num_cols:
    print(col,replace_with_threshold(df,col))

#Eksik Verilerin Yakalnması

import numpy as np
import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)

df = sns.load_dataset("titanic")

df.isnull()

df.isnull().values.any() #True - False

df.isnull().sum() #değişkenlerdeki eksik değer sayısı

df.notnull().sum() #değişkenlerdeki tam değer sayısı

df.isnull().sum().sum() #veri setindeki toplam eksik değer sayısı

df[df.isnull().any(axis=1)] #en az 1 tane eksik degeri sahip olan gözlem birimleri

df[df.notnull().all(axis=1)] #tam olan gözlem birimleri

df.isnull().sum().sort_values(ascending=True)

(df.isnull().sum() / df.shape[0]*100).sort_values(ascending=True)

na_cols = [col for col in df.columns if df[col].isnull().sum()>0]

def missing_values_table(dataframe,na_col=False):
    na_cols = [col for col in dataframe.columns if dataframe[col].isnull().sum() > 0]
    n_miss = dataframe[na_cols].isnull().sum().sort_values(ascending=True)
    ratio = (dataframe[na_cols].isnull().sum() / dataframe[na_cols].shape[0]*100).sort_values(ascending=True)
    missing_df = pd.concat([n_miss,np.round(ratio,2)],axis=1,keys=["n_miss","ratio"])
    print(missing_df,end="\n")
    if na_col:
        return na_cols

missing_values_table(df)

dff = sns.load_dataset("penguins")
missing_values_table(dff)

#Eksik Değer Problemlerini Çözmek

#1- Silme
df = sns.load_dataset("titanic")

df = df.dropna()

#2- Atama Yöntemleri ile Doldurma

df["age"].fillna(df["age"].mean()) #Ortalama ile doldurma

df["age"].fillna(df["age"].median()) #Median ile doldurma

df["age"].fillna(0) # Herhangi bir numerik değerle doldurma


#dff = df.apply(lambda x: x.fillna(x.median()) if x.dtype != "O" else x,axis=0)

#Kategorik Değişken Doldurma

df["embarked"].fillna(df["embarked"].mode()[0])

df["embarked"].fillna("missing")

#Kategorik Değişken Kırılımında Değer Atama

#age - doldurma -> kadınların ortalamasıi erkek ortalama

df.groupby("sex")["age"].mean()

df["age"].fillna(df.groupby("sex")["age"].transform("mean"))

import missingno as msno

msno.bar(df)

msno.matrix(df)