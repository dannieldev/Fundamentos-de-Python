import sys

from tkinter import *

root = Tk()

root.title("Mi primera appGrafica")

#cambia la anchura y altura del la ventana
#root.resizable(1,0)
root.resizable(1,True)
#cambiar el icono 
root.iconbitmap("icono.ico")
#cambiar tamaño por defecto
root.geometry("650x350")
#cambiar el fond de la ventana
root.config(bg="green")

root.mainloop()#
