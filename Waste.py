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
