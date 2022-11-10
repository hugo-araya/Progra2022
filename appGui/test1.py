from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
from tkinter import Menu

# maneja el evento de clic del botón
# maneja el cuadro de texto
# debe colocarse antes del botón

def clicked():
    res = "Bievenido a " + txt.get()
    lbl.configure(text = res)
    print(selected.get())
    # print hacia el terminal o consola
    # Caja o cuadro de mensaje
    #messagebox.showinfo('Titulo del mensaje', 'Contenido del mensaje')

# Agrgea un cuadro de dialogo (file dialog)
def openfile():
    filedialog.askopenfilenames()

# Especifica el tipo de archivo (filtrar por extension)
def openfile2():
    filedialog.askopenfilename(filetypes = (("Archivo texto","*.txt"),("Todos los archivos","*.*")))    

# pregunta por un directorio
def openfile3():
    filedialog.askdirectory()

# Agrega Notebook widget (tab) --> uses ttk
# -- tab_control = ttk.Notebook(window) 
# -- tab1 = ttk.Frame(tab_control)
# -- tab_control.add(tab1, text='Primero')
# -- tab_control.pack(expand=1, fill='both')

# Agrea widgets to Notebook
# -- tab_control = ttk.Notebook(window)
# -- tab1 = ttk.Frame(tab_control)
# -- tab2 = ttk.Frame(tab_control)
# -- tab_control.add(tab1, text='Primero')
# -- tab_control.add(tab2, text='Segundo')
# -- lbl1 = Label(tab1, text= 'label1')
# -- lbl1.grid(column=0, row=0)
# -- lbl2 = Label(tab2, text= 'label2')
# -- lbl2.grid(column=0, row=0)
# -- tab_control.pack(expand=1, fill='both')

# Agrega espacioado entre widget
# -- lbl1 = Label(tab1, text= 'label1', padx=5, pady=5)
# using padx and pady


if __name__ == '__main__':
    # crea una ventana
    window = Tk()
    window.title("Bienvenido (Hugo Araya Carrasco)")

    # crea un label con un tamaño y tipo de letra
    lbl = Label(window, text = "Hola", font = ("Arial Bold",20))
    lbl.grid(column = 0, row = 0)

    # Fija las dimensiones de la ventana
    window.geometry('500x500')

    # agregar un widget de botón con colores
    # ¿Por qué no puede cambiar el bg?
    btn = Button(window, text = "Presioname", bg = "black", fg = "black", command = clicked, font = ("Arial",20))   
    btn.grid(column = 0, row = 2)
    # lo ubica en la saegunda fila de la ventana

    # Captura un valor usando el widget entry
    txt = Entry(window, width = 0)
    # utiliza el metodo grid para posicionar el widget en la ventana
    txt.grid(column = 0, row = 1)

    # deja el foco (focus) de la aplicacion en el widget indicado
    txt.focus()

    # Deshabilita el entry widget 
    # -- txt = Entry(window, width=10, state='disabled')

    # Agrega un combobox
    # -- combo = Combobox(window)
    # -- combo['values'] = (1,2,3,4,5, "Text")
    # -- combo.current(1)
    # -- combo.grid(column = 0, row = 3)

    # Agrega a Checkbutton widget
    chk_state = BooleanVar()
    chk_state.set(True)
    chk = Checkbutton(window, text = 'Seleccione', var = chk_state)
    chk.grid(column = 0, row = 4)
    # establecer el estado marcado (var=_chk_state) pasando el valor de control al botón de control
    # usar IntVar para establecer el valor en 0 o 1 en lugar de BooleanVar

    # Agrega un radio buttons widgets
    selected = IntVar()
    rad1 = Radiobutton(window,text='Primero', value=1, variable=selected)
    rad2 = Radiobutton(window,text='Sundo', value=2, variable=selected)
    rad3 = Radiobutton(window,text='Tercero', value=3, variable=selected)

    rad1.grid(column = 0, row = 5)
    rad2.grid(column = 1, row = 5)
    rad3.grid(column = 2, row = 5)

    # ScrolledText widget
    txt = scrolledtext.ScrolledText(window, width = 40, height = 10)
    txt.grid(column = 0, row = 6)
    # conffigura el contenidi del scrolledtext
    txt.insert(INSERT, 'Escriba su texto aqui')
    # borra/limpia el contenido del scrolledtext
    # -- txt.delete(1.0, END)

    # Crea un MessageBox
    # -- messagebox.showinfo('Titulo del mensaje', 'Contenido del mensaje')
    # -- messagebox.askquestion('Titulo del mensaje', 'Contenido del mensaje') 
    # -- messagebox.askyesno('Titulo del mensaje', 'Contenido del mensaje')
    # -- messagebox.askokcancel('Titulo del mensaje', 'Contenido del mensaje')
    # -- messagebox.askretrycancel('Titulo del mensaje', 'Contenido del mensaje')
    messagebox.askyesnocancel('Titulo del mensaje', 'Contenido del mensaje')
    # ok, yes, retry returns TRUE
    # no, cancel returns FALSE

    # Agrega un spinbox
    spin = Spinbox(window, from_ = 0, to = 100, width = 10)
    spin.grid(column = 0, row = 7)
    # Se puede especificar el numero para el Spinbox
    spin3 = Spinbox(window, values = (3,8,11), width = 5)
    spin.grid(column = 2, row = 7)

    # Fija el valor para el Spinbox
    var = IntVar()
    var.set(36)
    spin2 = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
    spin2.grid(column = 1, row = 7)

    # Agrega una bara de progreso, progressbar y cambia el color
    # -- style = ttk.Style()
    # -- style.theme_use('default')
    # -- style.configure("black.Horizontal.TProgressbar", background = 'black')
    # -- bar = Progressbar(window, length = 200, style = 'black.Horizontal.TProgressbar')
    bar = Progressbar(window, length = 200)
    bar['value'] = 70
    bar.grid(column = 0, row = 8)
    
    # -- file = filedialog.askopenfilename()
    # -- files = filedialog.askopenfilenames() 
    # para multiples archivs
    openfiles = Button(window, text = "Abir archivo", bg = "black", fg = "black", command = openfile, font = ("Arial",20))
    openfiles.grid(column = 0, row = 9)

    openfiles2 = Button(window, text = "Abrir archivo 2", bg = "black", fg = "black", command = openfile2, font = ("Arial",20))
    openfiles2.grid(column = 0, row = 10)

    openfiles3 = Button(window, text = "Pregunta por directorio", bg = "black", fg = "black", command = openfile3, font = ("Arial",20))
    openfiles3.grid(column = 0, row = 11)
    # Especifica directorio inicial initial
    # from os import path
    # -- file = filedialog.askopenfilename(initialdir= path.dirname(__file__))

    # Agrega un a menu
    menu = Menu(window) 
    new_item = Menu(menu) 
    new_item.add_command(label='Nuevo', command = clicked) 
    menu.add_cascade(label='File', menu=new_item) 
    window.config(menu=menu)

    window.mainloop()