import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

for dirname, _, filenames in os.walk('mismanaged_plasticwaste.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
df = pd.read_csv('mismanaged_plasticwaste.csv')
print(df.head())
print(df.info())
df['Country'].unique()
df['Country'].value_counts()
df['Country'].nunique()
df.describe()

x1=df['Total_MismanagedPlasticWaste_2010 (millionT)'].sum()
x2=df['Total_MismanagedPlasticWaste_2019 (millionT)'].sum()
x=['2010','2019']
height = [x1,x2]
plt.figure(figsize=(10,6))
sns.barplot(x=x,y=height)
plt.xlabel("Year")
plt.ylabel("Total Mis managed Plastic Waste")
plt.title('Total Mis managed Plastic Waste in 2010, 2019')
plt.show()

x1=df.iloc[:,3].sum()
x2=df.iloc[:,4].sum()
x=['2010','2019']
height = [x1,x2]
plt.figure(figsize=(10,6))
sns.barplot(x=x,y=height)
plt.xlabel("Year")
plt.ylabel("Total Mis managed Plastic Waste")
plt.title('Total Mis managed Plastic Waste PerCapita in 2010, 2019')
plt.show()

mapuno = px.choropleth(data_frame=df,
              locations = "Country",
              locationmode='country names',
              color="Total_MismanagedPlasticWaste_2010 (millionT)",
              color_continuous_scale='Viridis',
              range_color=(0,13000000),
              width=1000,
              height=500,
              title ="Mismanaged plastic waste for each country in 2010"
             )
mapuno.show()

mapdos = px.choropleth(data_frame=df,
              locations = "Country",
              locationmode='country names',
              color="Total_MismanagedPlasticWaste_2019 (millionT)",
              color_continuous_scale='Viridis',
              range_color=(0,13000000),
              width=1000,
              height=500,
              title ="Mismanaged plastic waste for each country in 2019"
             )
mapdos.show()

to_20_country_2019 = df.sort_values('Total_MismanagedPlasticWaste_2019 (millionT)',ascending=False).head(25)
plt.figure (figsize = (16,8))
sns.barplot(x=to_20_country_2019["Total_MismanagedPlasticWaste_2019 (millionT)"],y=to_20_country_2019["Country"], color = "inferno")
plt.title("Top 25 has Mismanaged plastic waste around the world ")
plt.xlabel("Total Mismanaged Plastic Waste 2019")
plt.ylabel("Country")
plt.show()

to_25_country_2010 = df.sort_values('Total_MismanagedPlasticWaste_2010 (millionT)',ascending=False).head(25)
plt.figure (figsize = (16,8))
sns.barplot(x=to_25_country_2010["Total_MismanagedPlasticWaste_2010 (millionT)"],y=to_25_country_2010["Country"])
plt.title("Top 25 has Mismanaged plastic waste around the world ")
plt.xlabel("Total Mismanaged Plastic Waste 2010")
plt.ylabel("Country")
plt.show()