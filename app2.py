from tkinter import *
from tkinter import messagebox


def sumar ():
    z=pow(int(c.get()),1/int(x.get()))
    t_resultado.insert(INSERT, "Resultados:\n La raiz es "+str(z)+"\c")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados...")
    x.set("")
    c.set("")
    t_resultado.delete("1.0", "end")

def salir():
    messagebox.showinfo("Suma 1.0", "La App se cerrará...")
    ventana_principal.destroy()

#---------------------
# Ventana Principal
#---------------------

#Se declara una variable que llamamos ventana_principal y que adquiere las caracteristicas de un objeto Tk
ventana_principal=Tk()

#Titulo de la ventana
ventana_principal.title("Ivan Rueda")

#Establecer tamaño a la pantalla
ventana_principal.geometry("800x500")

#Icono de la ventana principal

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#Color de fondo de la ventana principal
ventana_principal.config(bg="black")

#---------------------
# Variables Globales
#---------------------  
x=IntVar()
c=IntVar()
z=IntVar()

#---------------------
# Frame Entrada
#---------------------

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="bisque3", width=780, height=240)
frame_entrada.place(x=10,y=10)

titulo= Label(frame_entrada, text="Raiz X de un número")
titulo.config(bg="bisque3", fg="maroon", font=("Arial", 20))
titulo.place(x=270,y=10)

subtitulo2= Label(frame_entrada, text="Hallar la raíz X de un Número enésimo,\n")
subtitulo2.config(bg="bisque3", fg="maroon", font=("Arial", 15), anchor=CENTER)
subtitulo2.place(x=270,y=70)

logo= PhotoImage(file="iconoo.png")
etiq_logo=Label(frame_entrada, image=logo)
etiq_logo.config(bg="ivory2")
etiq_logo.place(x=10,y=10)


etiq_a=Label(frame_entrada, text="Valor del índice (x): = ")
etiq_a.config(bg="bisque3", fg="blue", font=("Arial", 15), anchor=CENTER)
etiq_a.place(x=280, y=110)

entry_a=Entry(frame_entrada, width=7, textvariable=x)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=480,y=105)

etiq_b=Label(frame_entrada, text="Valor del número N = ")
etiq_b.config(bg="bisque3", fg="blue", font=("Arial", 15), anchor=CENTER)
etiq_b.place(x=280, y=160)

entry_b=Entry(frame_entrada, width=7, textvariable=c)
entry_b.config(font=("Arial", 20), justify=CENTER)
entry_b.focus_set()
entry_b.place(x=480,y=155)


frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="cornflower blue", width=780, height=120)
frame_operaciones.place(x=10,y=260)


bt_sum= PhotoImage(file="raiz.png")
bt_sumar= Button(frame_operaciones, image=bt_sum, width=105, height=105, command=sumar)
bt_sumar.place(x=116, y=7)


bt_bor= PhotoImage(file="borrar.png")
bt_borrar= Button(frame_operaciones, image=bt_bor, width=105, height=105, command=borrar)
bt_borrar.place(x=337, y=7)


bt_sal= PhotoImage(file="salir.png")
bt_salir= Button(frame_operaciones, image=bt_sal, width=105, height=105, command=salir)
bt_salir.place(x=585, y=7)


frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="indian red", width=780, height=100)
frame_resultados.place(x=10,y=390)

t_resultado=Text(frame_resultados, width=77, height=5)
t_resultado.config(bg="green", fg="white", font=("Courier", 12))
t_resultado.pack(expand=True)


ventana_principal.mainloop()
