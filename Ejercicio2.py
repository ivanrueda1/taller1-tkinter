# se importa la libreria tkinter con todas sus funciones 

from os import pread
from tkinter import *
from tkinter import messagebox
from click import command

# -------------------
# funciones de la app
# -------------------

def sumar():
    messagebox.showinfo("Suma 1.0", "Hizo click en el boton sumar...")
    c = int(a.get()) + int(b.get())
    t_resultados.insert(INSERT, "La suma de " + (a.get()) + " + " + (b.get()) + " es " + str(c)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos seran borrados...")
    a.set("")
    b.set("")
    t_resultados.delete("1.0", "end")

def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrara...")
    ventana_principal.destroy()

# ------------------
# variables globales
# ------------------

#-----------------
#ventana principal
#-----------------

#se declara una variable llamada ventana principal y que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

#titulo de la ventana 
ventana_principal.title("Ivan ")

# Establecer tamaño a la ventana
ventana_principal.geometry("800x500")

#Desahabilitar boton de maximizar
ventana_principal.resizable(0,0)

#color de fondo de la pantalla principal
ventana_principal.config(bg="black")

#-------------
#frame entrada
#-------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="dark salmon", width=780, height=240)
frame_entrada.place(x=10, y=10)

a = StringVar()
b = StringVar()
c = StringVar()

#Etiqueta para el titulo de la app
titulo = Label(frame_entrada, text= "Colegio San Jose de Guanentá")
titulo.config(bg="sky blue", fg="yellow" , font=("Arial", 20))
titulo.place(x=390, y=10)

#Etiqueta para el subtitulo de la app
subtitulo = Label(frame_entrada,  text='Especialidad en Sistemas')
subtitulo.config(bg="turquoise2", fg="black" , font=("Arial", 13))
subtitulo.place(x=390, y=40)

#Etiqueta para subtitulo2 de la app
subtitulo2 = Label(frame_entrada,  text= 'SUMA DE ENTEROS')
subtitulo2.config(bg="pale green", fg="green" , font=("Arial", 15))
subtitulo2.place(x=240, y=70)

# Imagen logo de la app
logo = PhotoImage(file="suma.png")
etiq_logo = Label(frame_entrada, image=logo)
etiq_logo.place(x=10, y=10)

#etiqueta para valor a
etiq_a = Label (frame_entrada,  text="a =")
etiq_a.config(bg="white", fg="black", font=("Arial", 20), anchor=CENTER)
etiq_a.place(x=390, y=120)

# entry para el valor a
entry_a = Entry (frame_entrada, width=4, textvariable=a)
entry_a.config(font=("Arial", 20))
entry_a.place(x=487,  y=120)

#etiqueta para valor b
etiq_b = Label (frame_entrada,  text="b =")
etiq_b.config(bg="white", fg="black", font=("Arial", 20), anchor=CENTER)
etiq_b.place(x=585, y=120)

# entry para el valor b
entry_a = Entry (frame_entrada, width=4, textvariable=b)
entry_a.config(font=("Arial", 20))
entry_a.place(x=682,  y=120)

#-----------------
# frame operaciones
#-----------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="azure3", width=780, height=120)
frame_operaciones.place(x=10, y=260)

# boton para sumar los numeros - texto
bt_sum = PhotoImage(file="bt_sum.png")
btsumar = Button(frame_operaciones, text= "sumar", width=10)
bt_sumar = Button(frame_operaciones, image=bt_sum, width=100, command=sumar)
bt_sumar.place(x=116, y=7)


# boton para borrar entradas y resultado
bt_bor = PhotoImage(file="boton_borrar.png")
bt_borrar =Button(frame_operaciones, text="Borrar", width=10)
bt_borrar = Button(frame_operaciones, image=bt_bor, width=105, height=105, command=borrar)
bt_borrar.place(x=337, y=7)

# boton para salir - cerrar la app
bt_sal = PhotoImage(file="boton_salir.png")
# bt_salir = Button(frame_operaciones, text="Salir", width=10)
bt_salir = Button(frame_operaciones, image=bt_sal, width=105, height=105, command=salir)
bt_salir.place(x=585, y=7)

# ----------------
# frame resultado
# ----------------

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="azure3", width=780, height=100)
frame_resultados.place(x=10, y=390)

# area de texto de resultados
t_resultados = Text(frame_resultados, width=50, height=3)
t_resultados.config(bg="green", fg="white", font=("Arial", 20))
t_resultados.pack()



 #Se ejecuta el metodo mainloop() de la clase Tk() a traves de la instancia ventana principal.
#Este metodo despliega una ventana simple en la pantalla y queda a la espera de lo que el
#usuario haga, por ejemplo, click en boton, escribir en caja de texto, etc.
#cada accion del usuariose conoce como un evento.El metodo mainloop es un bucle infinito.
ventana_principal.mainloop()