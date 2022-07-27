# se importa la librería tkinter con todas sus funciones
from tkinter import *
from turtle import width

# ------------------
# ventana_principal
# ------------------

# se declara una variable llamada ventana_principal y que adquiere las caracteristicas de un objeto Tk() ventana_principal = Tk()
ventana_principal= Tk()

# titulo de la ventana
ventana_principal.title("Bandera de Suecia")

# establece tamaño a la ventana 
ventana_principal.geometry("800x500")

# icono de la ventana_principal
# ventana_principal.

# deshabilitar boton de maximar
ventana_principal.resizable(0,0)

# color de fondo de la pantalla principal
ventana_principal.config (bg="yellow")

frame_1 = Frame(ventana_principal)
frame_1.config(bg="blue", width=250, height=210)
frame_1.place(x=0, y=0)

frame_2 = Frame(ventana_principal)
frame_2.config(bg="blue", width=250, height=210)
frame_2.place(x=0, y=300)

frame_3 = Frame(ventana_principal)
frame_3.config(bg="blue", width=470, height=200)
frame_3.place(x=330, y=300)

frame_4 = Frame(ventana_principal)
frame_4.config(bg="blue", width=470, height=200)
frame_4.place(x=330, y=0)

ventana_principal.mainloop()