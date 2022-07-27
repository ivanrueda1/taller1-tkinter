# se importa la librería tkinter con todas sus funciones
from tkinter import *

# ------------------
# ventana_principal
# ------------------

# se declara una variable llamada ventana_principal y que adquiere las caracteristicas de un objeto Tk() ventana_principal = Tk()
ventana_principal= Tk()

# titulo de la ventana
ventana_principal.title("Ivan Ramiro Rueda")

# establece tamaño a la ventana 
ventana_principal.geometry("800x300")

# icono de la ventana_principal
# ventana_principal.

# deshabilitar boton de maximar
ventana_principal.resizable(0,0)

# color de fondo de la pantalla principal
ventana_principal.config (bg="PaleGreen")

# agregamos un widget a la ventana principal
letrero= Label (text="\n\nSistemas, la mejor!!\n\n", bg="coral")
letrero.pack()

# agregsmos un widget a la ventana pricipal
letrero2 = Label (text="\n\nIvan Rueda\n\n", bg= "coral")
letrero2.pack()

# agregamos un witget a la ventana principal
letrero3 = Label (text="\n\nColegio San jose de Guanenta\n\n", bg="tomato3")
letrero3.pack()

# se ejecuta el metodo mainloop de la clase Tk() a través de la instancia ventana_principal.  Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton, escribir, etc).  Cada accion del usuario se conoce como un evento.  El metodo mainloop() es un bucle infinito.
ventana_principal.mainloop()