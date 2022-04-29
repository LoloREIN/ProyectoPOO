import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import pycountry
warnings.filterwarnings('ignore')


df=pd.read_csv('mismanaged_plasticwaste.csv')
print(df.head())


print(len(pycountry.countries))
print(list(pycountry.countries)[0])

def AsignarSiglas (country_code):
    try:
        return pycountry.countries.get(name=country_code).alpha_3
    except:
        return 'NaN'
def AsignarBandera (country_code):
    try:
        return pycountry.countries.get(name=country_code).flag
    except:
        return 'NaN'
df['country_code'] = df.apply(lambda row: AsignarSiglas(row.Country), axis = 1)
df['Flag'] = df.apply(lambda row: AsignarBandera(row.Country), axis = 1)
WWW_list = []
Country_List = df['Country'].tolist()
Flag_List = df['Flag'].tolist()
Tag_List = df['country_code'].tolist()
for i in range(df['Country'].size):
    WWW_list.append(list())
    WWW_list[i].append(Country_List[i])
    WWW_list[i].append(Tag_List[i])
    WWW_list[i].append(Flag_List[i])

print(WWW_list)
print(len(WWW_list))