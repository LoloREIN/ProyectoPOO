"""
POO- Proyecto de periodo
Concientización del plástico en el mundo
Miembros del Equipo
ID          Nombre                      Carrera
0243040     Diego Chipolini Pérez       LMECC
0243054     Lorena Martínez Loera       LIGIC
0212511     Lorenzo Reinoso Fuentes     LIDCI

Profesor: Gerardo Bárcena Ruiz

"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import pandas as pd
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import seaborn as sns
from tkhtmlview import HTMLLabel
import plotly.express as px
import dash


from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import warnings
import pycountry

warnings.filterwarnings('ignore')

frame_styles = {"relief": "groove",
                "bd": 3, "bg": "grey",
                "fg": "#073bb3", "font": ("Arial", 9, "bold")}
'''
Generales
*args se usa para pasar, de forma opcional, un número variable de argumentos posicionales.
*args recibe los argumentos como una tupla
**kwargs se usa para pasar, de forma opcional, un número variable de argumentos con nombre.
**kwargs recibe los argumentos como un diccionario.
se hereda de tkinter para facilitar las propiedades tales como self.geometry y self.title
grid y place son muy similares la diferencia es que 
    place necesita parametros por relacion o poscion exacta
    Grid se divide el "padre" en columnas y filas, con base a eso coloca el objeto
    Pack es para colocar el objeto completamente sobre el "padre"
    
Lamba expresions: 
similares a los metodos, pero no requieren nombre, y se pueden usar de manera inmediata en el cuerpo de un metodo 
'''


class LoginPage(tk.Tk):

    def __init__(self, *args, **kwargs):
        # Crea una ventana general de Tkinter
        tk.Tk.__init__(self, *args, **kwargs)
        # Da las caracteristicas de la ventana del Login
        main_frame = tk.Frame(self, bg="#708090", height=431, width=626)
        main_frame.pack(fill="both")
        self.geometry("626x431")  # Tamaño de la Ventana
        self.resizable(0, 0)  # lo hace de tamaño fijo

        # Codigo para poner la imagen de fondo
        image1 = Image.open("botellas.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(main_frame, image=test)
        label1.image = test
        label1.pack(fill="both")

        # tipos de letras para el documento
        title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "grey"}

        text_styles = {"font": ("Verdana", 14),
                       "background": "grey",
                       "foreground": "#E1FFFF"}
        # Inicio del "frame" que contine los detalles de Login
        frame_login = tk.Frame(main_frame, bg="grey", relief="groove", bd=2)
        frame_login.place(rely=0.30, relx=0.17, height=130, width=400)
        # Titulo del Frame
        label_title = tk.Label(frame_login, title_styles, text="Iniciar sesión")
        label_title.grid(row=0, column=1, columnspan=1)
        # Label de usuario (solo texto)
        label_user = tk.Label(frame_login, text_styles, text="Usuario:")
        label_user.grid(row=1, column=0)
        # Label de contraseña (solo texto)
        label_pw = tk.Label(frame_login, text_styles, text="Contraseña:")
        label_pw.grid(row=2, column=0)
        # espacio para poner el usuario
        entry_user = ttk.Entry(frame_login, width=30, cursor="xterm")
        entry_user.grid(row=1, column=1)
        # espacio para la contraseña show cambia los carácteres a *
        entry_pw = ttk.Entry(frame_login, width=30, cursor="xterm", show="*")
        entry_pw.grid(row=2, column=1)
        # creación de un boton para hacer el login (con getlogin())
        # el lambda crea funciones anonimas
        button = ttk.Button(frame_login, text="Login", command=lambda: getlogin())
        button.place(rely=0.70, relx=0.51)
        # creación de un boton para hacer el registro de un nuevo usuario (con signup())
        # el lambda crea funciones anonimas
        signup_btn = ttk.Button(frame_login, text="Registro", command=lambda: get_signup())
        signup_btn.place(rely=0.70, relx=0.73)

        # funcion que despliega la pagina de Inicio de sesion
        def get_signup():
            Registro()

        # funcion del boton del login
        def getlogin():
            # toma el valor de el Entry del usuario
            username = entry_user.get()
            # toma el valor de el Entry de la contraseña
            password = entry_pw.get()
            # usa la funcion validación la cual retorna Verdadero o Falso
            validation = validate(username, password)
            # si la validación es verdadera
            if validation:
                # Crea un pop up message que dice bienvenido usuario
                tk.messagebox.showinfo("Atención", "Bienvenido {}".format(username))
                # Trae la ventana hacia enfrente y la deja hasta que el usuario l
                root.deiconify()
                top.destroy()
            # si la validación es falsa
            else:
                # El usuario o contraseña que ingresaste es incorrecto
                tk.messagebox.showerror("Atención", "El usuario o contraseña que ingresaste es incorrecto ")

        # Funcion de validacion, recibe usuario y contraseña como parametros
        def validate(username, password):
            # intenta abrir el archo de Credenciales como crendenciales
            try:
                with open("credentials.txt", "r") as credentials:
                    # por cada linea de credenciales separa la linea en cada coma
                    for line in credentials:
                        line = line.split(",")
                        # y en cada linea en el espacio uno, o segundo elemento revisa que el usuario coincida
                        # si el usuario coincide revisa que la contraseña coincida
                        # *con los parametros de la funcion
                        if line[1] == username and line[3] == password:
                            # si en algun momento se cumplem ambas condiciones la validacion se vuelve verdadera
                            return True
                    return False
            # si no encuentra el archivo de credenciales esto indica que no haz creado ningun usuario
            # Por lo que te recomienda crear un
            except FileNotFoundError:
                print("Necesitas crear un usuario primero")
                # El retun False genera que la validacion sea falsa
                return False


# crea una nueva clase registro
class Registro(tk.Tk):

    def __init__(self, *args, **kwargs):
        # Se crea una nueva ventana de Registro
        tk.Tk.__init__(self, *args, **kwargs)
        # Se crea un frame con las caracteristicas
        main_frame = tk.Frame(self, bg="grey", height=150, width=250)
        # pack_propagate prevents the window resizing to match the widgets
        # pack_propagate, previene que la ventana cambie de tamaño
        main_frame.pack_propagate(0)
        # pack hace que esta nueva frame se incerte en la vetana de registo
        main_frame.pack(fill="both", expand="true")
        # le da tamaño a la venta de registro
        self.geometry("250x100")
        # evita que la ventana cambie de tamaño
        self.resizable(0, 0)
        # le da de titulo registro
        self.title("Registro")
        # es el estilo de texto, color, tamaño tipografia etc
        text_styles = {"font": ("Verdana", 10),
                       "background": "grey",
                       "foreground": "#E1FFFF"}
        # se crea el label de usuario
        label_user = tk.Label(main_frame, text_styles, text="Nuevo Ususario:")
        # se le da la Posición al label en el main frame
        label_user.grid(row=1, column=0)
        # se crea el label de contraseña
        label_pw = tk.Label(main_frame, text_styles, text="Contraseña:")
        # se le da la Posición al label en el main frame
        label_pw.grid(row=2, column=0)
        # se crea un Entry para el usuario
        entry_user = ttk.Entry(main_frame, width=15, cursor="xterm")
        # se le da la Posición al Entry en el main frame
        entry_user.grid(row=1, column=1)
        # se crea un Entry para la contraseña
        entry_pw = ttk.Entry(main_frame, width=15, cursor="xterm", show="*")
        # se le da la Posición al Entry en el main frame
        entry_pw.grid(row=2, column=1)
        # se crea un boton con el que se puede hacer el registro con signup()
        button = ttk.Button(main_frame, text="Crear Cuenta", command=lambda: signup())
        # se le da la Posición al Botón en el main frame
        button.grid(row=4, column=1)

        # declara la función signup
        def signup():
            # Creates a text file with the Username and password
            # toma el usuario del Entry de usuario
            user = entry_user.get()
            # toma la contraseña del Entry de Contraseña
            pw = entry_pw.get()
            # invoca la funcion validar Usuario con el parametro usuario
            validation = validate_user(user)
            # si la validacion es Falsa(el usuario ya exite)
            if not validation:
                # Despliega un pop up message que dice "El usuario ya existe"
                tk.messagebox.showerror("Atención", "El usuario ya existe")
            # Si la validacion es Verdadera
            else:
                # lista de los carateres especiales
                SpecialSym = ['$', '@', '#', '%']
                # Creacion de parametros para una contraseña segura
                # incializada en True, y si no cumple algún parámetro se vuelve falso
                val = True
                # si la contraseña tiene menos de 7 caracteres-> No segura
                if len(pw) < 7:
                    tk.messagebox.showerror("Atención", 'La contraseña debe de tener por lo menos 7 caracteres')
                    val = False
                # si la contraseña tiene mas de 20 caracteres-> segura, pero ineficiente
                if len(pw) > 20:
                    tk.messagebox.showerror("Atención", 'La contraseña no puede tener mas de 20 caracteres')
                    val = False
                # si la contraseña no tiene numero o numeros-> No segura
                if not any(char.isdigit() for char in pw):
                    tk.messagebox.showerror("Atención", 'La contraseña debe de tener por lo menos un número')
                    val = False
                # si la contraseña no tiene mayuscula-> No segura
                if not any(char.isupper() for char in pw):
                    tk.messagebox.showerror("Atención", 'La contraseña debe de tener por lo menos una Mayúscula')
                    val = False
                # si la contraseña no tiene minuscula-> No segura
                if not any(char.islower() for char in pw):
                    tk.messagebox.showerror("Atención", 'La contraseña debe de tenr por lo menos una minúscula')
                    val = False
                # si la contraseña no tiene caracter especial-> No segura
                if not any(char in SpecialSym for char in pw):
                    tk.messagebox.showerror("Atención", 'La contraseña debe al menos tener un caracter especial: $@#')
                    val = False
                # si cumple todos los parametros entonces
                if val:
                    # se abre el archi de las credenciales, y se usa *Apend Text* para no sobre escribir el archivo
                    credentials = open("credentials.txt", "at")
                    # escribirá Usuario, el usuario, Password, la contraseña y se pasará al siguiente renglon
                    credentials.write(f"Username,{user},Password,{pw},\n")
                    # se cierra el archivo
                    credentials.close()
                    # pop up message avisandole al usuario que se guardaron sus datos
                    tk.messagebox.showinfo("Atención", "Los detalles de la cuenta se han guardado")
                    # se cierra la ventana de registro
                    Registro.destroy(self)
                # si no se cumple la contraseña segura
                else:
                    # pop up message avisandole al usuario que no se guardaron sus datos
                    tk.messagebox.showerror("Atención", "Su registro no se completo")

        # funcion para validar el usuario y que no se repita
        def validate_user(username):
            try:
                # con el archivo abierto, leera el contendio del archivo
                with open("credentials.txt", "r") as credentials:
                    # en cada linea del archivo
                    for line in credentials:
                        # separá cada coma
                        line = line.split(",")
                        # en el segundo espacio de la linea que es el "Username" va a ver si existe
                        if line[1] == username:
                            # si existe la validacion es Falsa(ya exite el usuario)
                            return False
                # si termina el ciclo y no fue Falso entonces el usuario no exite y devuelve True
                return True
            # si el archivo no existe lo interpreta como que es el primer usuario y devuelve true
            except FileNotFoundError:
                return True


# crea una nueva clase que hereda las caracteristicas de menu de Tkinter
class MenuBar(tk.Menu):
    # se inicializa el menu
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        # se crea el menu, el tearoff es para que no nos salga un elemento vacio por defecto
        menu_file = tk.Menu(self, tearoff=0)
        # se crea una "cascada"/elemntos deplegados en el primer espacio con el nombre main,
        self.add_cascade(label="Main", menu=menu_file)
        # se agrega un elemento a la cascada llamado Paises, el cual al ser seleccionado,
        # invoca la funcion Show frame con "paises" como parametro
        menu_file.add_command(label="Paises", command=lambda: parent.show_frame(Paises))
        # se añade una linea separadora
        menu_file.add_separator()
        # se agrega un elemento a la cascada llamado Salir, el cual al ser seleccionado,
        # invoca la funcion Quit
        menu_file.add_command(label="Salir", command=lambda: parent.Quit())
        # se crea otro menu, el tearoff es para que no nos salga un elemento vacio por defecto
        YearComparison = tk.Menu(self, tearoff=0)
        # se crea una "cascada"/elemntos deplegados en el segundo espacio con el nombre Barplot,
        self.add_cascade(label="Barplot", menu=YearComparison)
        # se agrega un elemento a la cascada llamado años, el cual,
        # invoca la funcion Show frame con "years" como parametro
        YearComparison.add_command(label="Años", command=lambda: parent.show_frame(years))

        # crea un menu de tkinter
        menu_proyect = tk.Menu(self, tearoff=0)
        # se crea una "cascada"/elemntos deplegados en el tercer espacio con el nombre Info,
        self.add_cascade(label="Info", menu=menu_proyect)
        # se agrega un elemento a la cascada llamado Promedios, el cual,
        # invoca la funcion Show frame con "Promedio" como parametro
        menu_proyect.add_command(label="Promedios", command=lambda: parent.show_frame(Promedio))
        # crea un menu de tkinter
        menu_maps = tk.Menu(menu_proyect, tearoff=0)
        # se crea una "cascada"/elemntos deplegados dentro del 3er menu con el nombre Mapas,
        menu_proyect.add_cascade(label="Mapas", menu=menu_maps)
        # se agrega un elemento a la cascada llamado 2010, el cual,
        # invoca la funcion Show frame con "Map2010" como parametro
        menu_maps.add_command(label="2010", command=lambda: parent.show_frame(Map2010))
        # se agrega un elemento a la cascada llamado 2019, el cual,
        # invoca la funcion Show frame con "Map2019" como parametro
        menu_maps.add_command(label="2019", command=lambda: parent.show_frame(Map2019))


# se crea el objeto de tipo class MyApp() el cual hereda la ventana principal de tk inter
class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # se crea un main frame
        main_frame = tk.Frame(self, bg="#84CEEB", height=600, width=1024)
        # Determina con un booleano si la informacion geometrica de los componentes determinara el tamaño de la Frame
        # False = no
        main_frame.pack_propagate(0)
        # El main frame va a llenar nuestra MyApp
        main_frame.pack(fill="both", expand="true")
        # el blue print de la Frame para anexar elementos
        main_frame.grid_rowconfigure(0, weight=1)
        # el blue print de la Frame para anexar elementos
        main_frame.grid_columnconfigure(0, weight=1)
        # crea una propiedad que se llama frames en la que se guardarán las paginas de nuestra APP
        self.frames = {}
        # las paginas de nuestra app
        pages = (Paises, years, Promedio, Map2010, Map2019)
        # Por cada elemnteo de pages, se crea una frame, se le da la caracteristica y se le da la caractesitica de frame
        for F in pages:
            frame = F(main_frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        # Mostrar el Frame de paises como primera frame
        self.show_frame(Paises)
        # crea el menubar con la clase declarada anteriormente
        menubar = MenuBar(self)
        # se agrega el menu a nuestra ventana de MyAPP
        tk.Tk.config(self, menu=menubar)

    # funcion que recibe el nombre de la "frame" a invocar
    def show_frame(self, name):
        # el frame se va a identificar como frame y el nombre
        frame = self.frames[name]
        # tkraise lleva el frame a primer plano
        frame.tkraise()

    # Funcion que destruye al elemento/objeto del que se invoca
    def Quit(self):
        self.destroy()


# Clase GUI(Graphic User Interface) la cual hereda la clase frame de Tkinter
# Clase "Padre" - Nuestro set up
class GUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # Se le dan caracteristicas al Main Frame
        self.main_frame = tk.Frame(self, bg="grey", height=600, width=1024)
        # se le da Posicion y tamaño
        self.main_frame.pack(fill="both", expand="true")
        # se confirgura el espacio renglon para los componentes
        self.main_frame.grid_rowconfigure(0, weight=1)
        # se confirgura el espacio columna para los componentes
        self.main_frame.grid_columnconfigure(0, weight=1)

# Objeto de tipo clase Pais que hereda a GUI
class Paises(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        frame1 = tk.LabelFrame(self, frame_styles, text="Lista de los Paises")
        frame1.place(rely=0.05, relx=0.02, height=500, width=400)

        dataFile = pd.read_csv('mismanaged_plasticwasteG.csv')

        frame2 = tk.LabelFrame(self, frame_styles, text="Graficas por País")
        frame2.place(rely=0.05, relx=0.45, height=500, width=500)
        mylabel = Label(frame2, text="Elige un País",
                        font=("Helvetica", 14),bg = "grey", fg="light blue")
        mylabel.pack(pady=10)
        countries = []
        countriesFile = dataFile['Country'].tolist()
        countries.append("--Pais--")
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
                                       master=frame2)
            canvas.draw()

            canvas.get_tk_widget().pack()

            toolbar = NavigationToolbar2Tk(canvas,
                                           frame2)
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

            data = frame2.pack_slaves()

            if len(data) > 2:
                data[2].destroy()
                data[3].destroy()
            plot(wasteList, perCapitaList)

        choices = countries
        variable = StringVar(frame2)
        variable.set('Select a country')
        w = OptionMenu(frame2, variable, *choices, command=display_selected)
        w.pack(expand=True)

        # This is a treeview.
        tv1 = ttk.Treeview(frame1)
        column_list_account = ["Country", "country_code", "Flag"]
        tv1['columns'] = column_list_account
        tv1["show"] = "headings"  # removes empty column
        for column in column_list_account:
            tv1.heading(column, text=column)
            tv1.column(column, width=50)
        tv1.place(relheight=1, relwidth=0.995)
        treescroll = tk.Scrollbar(frame1)
        treescroll.configure(command=tv1.yview)
        tv1.configure(yscrollcommand=treescroll.set)
        treescroll.pack(side="right", fill="y")

        def Load_data():
            def AsignarSiglas(country_code):
                try:
                    return pycountry.countries.get(name=country_code).alpha_3
                except:
                    return 'NaN'

            def AsignarBandera(country_code):
                try:
                    return pycountry.countries.get(name=country_code).flag
                except:
                    return 'NaN'

            df = pd.read_csv('mismanaged_plasticwaste.csv')
            df['country_code'] = df.apply(lambda row: AsignarSiglas(row.Country), axis=1)
            df['Flag'] = df.apply(lambda row: AsignarBandera(row.Country), axis=1)
            WWW_list = []
            Country_List = df['Country'].tolist()
            Flag_List = df['Flag'].tolist()
            Tag_List = df['country_code'].tolist()
            for i in range(df['Country'].size):
                WWW_list.append(list())
                WWW_list[i].append(Country_List[i])
                WWW_list[i].append(Tag_List[i])
                WWW_list[i].append(Flag_List[i])
            for row in WWW_list:
                tv1.insert("", "end", values=row)

        Load_data()


class years(GUI):

    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        df = pd.read_csv('mismanaged_plasticwaste.csv')
        label1 = tk.Label(self.main_frame, bg="grey", font=("Verdana", 20), text="Analisis por años")
        label1.pack(side="top")
        frame1 = tk.LabelFrame(self, frame_styles, text="Analisis de basura total")
        frame1.place(rely=0.1, relx=0.05, height=500, width=450)

        x1 = df['Total_MismanagedPlasticWaste_2010 (millionT)'].sum()
        x2 = df['Total_MismanagedPlasticWaste_2019 (millionT)'].sum()
        x = ['2010', '2019']
        height = [x1, x2]
        fig = plt.figure(figsize=(10, 7))
        sns.set_style("darkgrid")
        sns.barplot(x=x, y=height)
        plt.xlabel("Año")
        plt.ylabel("Total de Basura no Gestionada")
        plt.title('Total de basura Plastica desatendida \n 2010 vs 2019')
        canvas = FigureCanvasTkAgg(fig, master=frame1)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both")
        FrameWeb = HTMLLabel(frame1, html="<h2><strong>Grafica de Basura total(Promedio)</strong></h2>\
                                      <p>En esta grafica se ve el total de basura sumada de cada pais por año\
                                      </p>\
                                          </div>")
        FrameWeb.pack(fill="both", side = "bottom")

        frame2 = tk.LabelFrame(self, frame_styles, text="Analisis de Basura per Capita")
        frame2.place(rely=0.1, relx=0.52, height=500, width=450)
        v1 = df.iloc[:, 3].sum()
        v2 = df.iloc[:, 4].sum()
        x = ['2010', '2019']
        height = [v1, v2]
        fig = plt.figure(figsize=(11, 7))
        sns.set_style("darkgrid")
        sns.barplot(x=x, y=height)
        plt.xlabel("Año")
        plt.ylabel("\nPromedio de Basura", labelpad=0)
        plt.title('Promedio de Basura de Plastico Desatendida per capita \n 2010 vs 2019')
        canvas = FigureCanvasTkAgg(fig, master=frame2)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both")
        FrameWeb = HTMLLabel(frame2, html="<h3>Grafica de Basura total per capita(promedio)</h3>\
                                              <p>En esta grafica se ve el total de basura sumada de cada pais por año\
                                              </p>\
                                                  </div>")
        FrameWeb.pack(fill="both", side="bottom")


class Map2010(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, bg="grey", font=("Verdana", 20), text="Analisis por años")
        label1.pack(side="top")

        frame1 = tk.LabelFrame(self, frame_styles, text="Mapa creado con Plotly express")
        frame1.place(rely=0.1, relx=0.05, height=500, width=900)
        FrameWeb = HTMLLabel(frame1, html='<img src = "">\
                                          <h3>Grafica de Basura total per capita(promedio)</h3>\
                                              <p>En esta grafica se ve el total de basura sumada de cada pais por año\
                                              </p>\
                                                  </div>')
        FrameWeb.pack(fill="both")
'''        label = Label(frame1, image=ImageTk.PhotoImage(Image.open("diez.png")))
        label.pack()'''
'''     mapuno = px.choropleth(data_frame=df,
                               locations="Country",
                               locationmode='country names',
                               color="Total_MismanagedPlasticWaste_2010 (millionT)",
                               color_continuous_scale='Viridis',
                               width=1000,
                               height=500,
                               title="Mismanaged plastic waste for each country in 2010"
                               )
        # open in website
        app = dash.Dash()
        app.layout = html.Div([
            dcc.Graph(figure= mapuno)
        ])'''


class Map2019(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), bg="grey", text="Mapa 2019")
        label1.pack(side="top")
        frame7 = tk.LabelFrame(self, frame_styles, text="Mapa creado con Plotly express")
        frame7.place(rely=0.1, relx=0.05, height=500, width=900)
        frame = Frame(frame7, width=600, height=400)


'''     photo = ImageTk.PhotoImage(Image.open("botellas.png"))
        vlabel = tk.Label(self, text="", image=photo)
        vlabel.image = photo
        vlabel.place(x=-1, y=-5, relwidth=1, relheight=1)
'''
'''

        mapdos = px.choropleth(data_frame=df,
                       locations="Country",
                       locationmode='country names',
                       color="Total_MismanagedPlasticWaste_2019 (millionT)",
                       color_continuous_scale='Viridis',
                       width=1000,
                       height=500,
                       title="Mismanaged plastic waste for each country in 2019"
                       )


app.run_server(debug=True, use_reloader=False)'''


class Promedio(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Analisis por promedio", bg="grey")
        label1.pack(side="top")
        frame_Prom = tk.LabelFrame(self, frame_styles, text="Promedio")
        frame_Prom.place(rely=0.1, relx=0.05, height=500, width=900)
        WPW = 'mismanaged_plasticwaste.csv'
        datos = pd.read_csv(WPW)
        datos['Promedio(millionT)'] = ((datos['Total_MismanagedPlasticWaste_2010 (millionT)'] +
                                        datos['Total_MismanagedPlasticWaste_2019 (millionT)']) / 2).astype(float)
        datos['Prom PerCapita'] = ((datos['Mismanaged_PlasticWaste_PerCapita_2010 (kg per year) '] +
                                      datos['Mismanaged_PlasticWaste_PerCapita_2019 (kg per year) ']) / 2).astype(float)
        datos.sort_values(["Promedio(millionT)"],
                          axis=0,
                          ascending=[False],
                          inplace=True)
        x1 = datos["Prom PerCapita"].head(15)
        y1 = datos['Promedio(millionT)'].head(15)
        county = datos["Country"].head(15)
        figura = plt.figure()
        sns.scatterplot(x=y1, y=county, data=datos, size=x1, palette="deep")
        sns.set_style("darkgrid")
        plt.xlabel("Promedio de basura(2010+2019)/2")
        plt.ylabel("Paises", labelpad=0)
        plt.title('Promedio de Basura de Plastico Desatendida')
        canvas = FigureCanvasTkAgg(figura, master=frame_Prom)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both")
        FrameWeb = HTMLLabel(frame_Prom, html="<h3>Promedio de Basura de Plastico Desatendida</h3>\
                                                      <p>En esta grafica se ve el total de basura sumada de cada pais por año\
                                                      </p>\
                                                          </div>")
        FrameWeb.pack(fill="both", side="bottom")

# se crea el login
top = LoginPage()
# se le adjunta un titulo
top.title("Proyecto de POO")
# se crea el obejo Raiz con MyAPP()
root = MyApp()
# esconde el objeto de la pantalla hasta que se le llame
root.withdraw()
# se le adjunta un titulo
root.title("Concientización del plástico en el mundo")

# llama al main loop de tk para que corra
root.mainloop()
