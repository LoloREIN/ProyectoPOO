from tkinter import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataFile = pd.read_csv('mismanaged_plasticwasteG.csv')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

mywindow = Tk()
mywindow.title("mismanaged plasticwaste")
mywindow.geometry("600x400")
mylabel = Label(mywindow, text="Select a country",
                font=("Helvetica", 14), fg="grey")
mylabel.pack(pady=20)

countries = []
countriesFile = dataFile['Country'].tolist()
countries.append("Select a country")
countries.extend(countriesFile)


def plot(wasteList, perCapitaList):
    fig = Figure(figsize=(5, 5),
                 dpi=100)

    x = [2010, 2019]
    y1 = wasteList
    y2 = perCapitaList

    plot1 = fig.add_subplot(111)

    plot1.plot(x, y1, marker='o', label="Total MismanagedPlastic Waste")
    plot1.plot(x, y2, marker='o', label="Mismanaged PlasticWaste PerCapita")
    plot1.legend()
    plot1.grid()

    canvas = FigureCanvasTkAgg(fig,
                               master=mywindow)
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas,
                                   mywindow)
    toolbar.update()

    canvas.get_tk_widget().pack()


def display_selected(choice):
    choice = variable.get()
    index = countries.index(choice) - 1
    # print(dataFile.loc[index]['Total_MismanagedPlasticWaste_2010 (millionT)'])
    Waste_2010 = dataFile.loc[index]['Total_MismanagedPlasticWaste_2010 (millionT)']
    Waste_2019 = dataFile.loc[index]['Total_MismanagedPlasticWaste_2019 (millionT)']
    PerCapita_2010 = dataFile.loc[index]['Mismanaged_PlasticWaste_PerCapita_2010 (kg per year) ']
    PerCapita_2019 = dataFile.loc[index]['Mismanaged_PlasticWaste_PerCapita_2019 (kg per year) ']

    wasteList = [Waste_2010, Waste_2019]
    perCapitaList = [PerCapita_2010, PerCapita_2019]

    data = mywindow.pack_slaves()

    if len(data) > 2:
        data[2].destroy()
        data[3].destroy()
    plot(wasteList, perCapitaList)


choices = countries
variable = StringVar(mywindow)
variable.set('Select a country')
w = OptionMenu(mywindow, variable, *choices, command=display_selected)
w.pack(expand=True)

mywindow.mainloop()
