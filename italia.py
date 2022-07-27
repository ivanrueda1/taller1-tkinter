# se importa la librería tkinter con todas sus funciones
from tkinter import *
from turtle import width

# ------------------
# ventana_principal
# ------------------

# se declara una variable llamada ventana_principal y que adquiere las caracteristicas de un objeto Tk() ventana_principal = Tk()
ventana_principal= Tk()

# titulo de la ventana
ventana_principal.title("Bandera de Italia")

# establece tamaño a la ventana 
ventana_principal.geometry("800x500")

# icono de la ventana_principal
# ventana_principal.

# deshabilitar boton de maximar
ventana_principal.resizable(0,0)

# color de fondo de la pantalla principal
ventana_principal.config (bg="white")

frame_1 = Frame(ventana_principal)
frame_1.config(bg="red", width=780, height=780)
frame_1.place(x=5, y=10)

frame_2 = Frame(ventana_principal)
frame_2.config(bg="white", width=520, height=780)
frame_2.place(x=6, y=10)

frame_3 = Frame(ventana_principal)
frame_3.config(bg="green", width=260, height=780)
frame_3.place(x=6, y=10)

# se ejecuta el metodo mainloop de la clase Tk() a través de la instancia ventana_principal.  Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton, escribir, etc).  Cada accion del usuario se conoce como un evento.  El metodo mainloop() es un bucle infinito.
ventana_principal.mainloop()