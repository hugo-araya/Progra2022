from tkinter import *

if __name__ == '__main__':
    ventana = Tk()
    ventana.geometry('200x200+300+300')
    lbl1 = Label(ventana, text='Hello World!')
    lbl1.grid(row =0, column =0)
    lbl2 = Label(ventana, text='Hola mundo!')
    lbl2.grid(row =0, column =3)
    #lbl1.grid(row = 0, column = 0)
    ventana.mainloop()