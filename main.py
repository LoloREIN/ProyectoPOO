import tkinter
import matplotlib
import seaborn as sns

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

# from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

import numpy as np
from math import *

def prSetTxt(pTxt, pVal):
    pTxt.delete(0, len(pTxt.get()))
    pTxt.insert(0, pVal)

class PlotWin:

    def createWindow(self):
        self.window = tkinter.Tk()

        self.window.title("Ciber-Resilencia")
        self.window.geometry("430x250+100+200")

        self.lbl02 = tkinter.Label(self.window, text="Largo= ")
        self.lbl02.place(x=10, y=50)

        self.lbl03 = tkinter.Label(self.window, text="Ancho= ")
        self.lbl03.place(x=10, y=90)

        self.lbl04 = tkinter.Label(self.window, text="Alto= ")
        self.lbl04.place(x=10, y=130)

        self.txt02 = tkinter.Entry(self.window, bg="lightgray", width=17)

        self.txt02.place(x=160, y=48)
        prSetTxt(self.txt02, '4')

        self.txt03 = tkinter.Entry(self.window, bg="lightgray", width=17)

        self.txt03.place(x=160, y=88)
        prSetTxt(self.txt03, '5')

        self.txt04 = tkinter.Entry(self.window, bg="lightgray", width=17)

        self.txt04.place(x=160, y=128)
        prSetTxt(self.txt04, '6')

        self.btn01 = tkinter.Button(self.window, text="Muestra", command=self.btn01_click)

        self.btn01.place(x=350, y=10, width=75)

        self.window.mainloop()

    def showPlot(self, largo, ancho, alto):

        lWin = tkinter.Tk()
        lWin.title("Modelo de Ciber Resilencia")
        Basura = sns.load_dataset("/Users/lorenzoreinoso/PycharmProjects/ProyectoPOO/mismanaged_plasticwaste.csv")
        sns.boxplot(x="Total_MismanagedPlasticWaste_2010 (millionT)", y="Country", data=Basura)
        canvas = FigureCanvasTkAgg(lFig, master=lWin)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    def btn01_click(self):
        self.showPlot(int(self.txt02.get()), int(self.txt03.get()), int(self.txt04.get()))


myPlotWin = PlotWin()
myPlotWin.createWindow()