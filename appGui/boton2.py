import tkinter as tk
def funcion(n):
    print(n)

def funcion1():
    print('consola')

if __name__== '__main__' :
    ventana = tk.Tk()
    x=5
    boton = tk.Button(ventana, text='Boton 1', command = lambda :funcion(x))
    boton.grid(column=0, row=0)
    ventana.mainloop()

