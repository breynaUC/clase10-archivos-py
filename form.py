from tkinter import *
import operaciones
win = Tk()
'''El siguiente codigo permite centrar el formulario en la pantalla de 
la computadora.'''
x = (win.winfo_screenwidth() - win.winfo_reqwidth()) / 2
y = (win.winfo_screenheight() - win.winfo_reqheight()) / 2
win.geometry("+%d+%d" % (x, y))
'''El siguiente código es para el tamaño de la pantalla.'''
win.geometry('350x420')
texto1 = StringVar()
texto2 = StringVar()
opcion = IntVar()
def limpiar():
    text.delete("1.0","end")
    entry_texto.focus()
def imprimir():
    text.insert("insert", "lista= ")
    total = 0
def operacion():
    if opcion.get()==1:
        operaciones.crearCarpeta(texto1.get())
        text.insert("insert", "Carpeta: "+str(texto1.get())+" Creado")
    elif opcion.get()==2:
        operaciones.crearFile(texto1.get())
        text.insert("insert", "Archivo: "+str(texto1.get())+".txt Creado")
    elif opcion.get()==3:
        operaciones.add(texto1.get(),texto2.get())
        text.insert("insert", "texto: "+str(texto2.get())+"Insertado en el archivo " +str(texto1.get())+".txt")
    elif opcion.get()==4:
        operaciones.adds(texto1.get(),texto2.get())
        text.insert("insert", "texto: "+str(texto2.get())+"Insertado en el archivo " +str(texto1.get())+".txt")
    elif opcion.get()==5:
        operaciones.delDirectorioVacio(texto1.get());
        text.insert("insert", "Se a Eliminado el directorio: "+str(texto1.get()))
    elif opcion.get()==6:
        operaciones.delete(texto1.get());
        text.insert("insert", "Se a Eliminado el directorio: "+str(texto1.get()))
    elif opcion.get()==7:
        text.insert("insert", "Archivo: "+str(texto1.get()+":"+str(operaciones.leer(texto1.get()))))
    elif opcion.get()==8:
        operaciones.delDirectorioFile(texto1.get());
        text.insert("insert", "Se a Eliminado el directorio: "+str(texto1.get()))
    elif opcion.get()==9:
        operaciones.renombrarArchivo(texto1.get(), texto2.get());
        text.insert("insert", "Se ha renombrado el archivo: "+str(texto1.get())+"Por el"+str(str(texto2.get())))

label_texto = Label(win, text="Texto: ")
label_texto.grid(column=1, row=3, sticky=E)
entry_texto = Entry(win, textvariable=texto1, width=45)
entry_texto.grid(row=3, column=2, sticky=E+W)
label_texto = Label(win, text="Texto: ")
label_texto.grid(column=1, row=4, sticky=E)
entry_texto = Entry(win, textvariable=texto2, width=45)
entry_texto.grid(row=4, column=2, sticky=E+W)

radio_crear_carpet = Radiobutton(win, text="Crear carpeta", variable=opcion, value=1);
radio_crear_carpet.grid(row=5, column=2, sticky=W)

radio_crear_file = Radiobutton(win, text="Crear File", variable=opcion, value=2);
radio_crear_file.grid(row=6, column=2, sticky=W)

radio_crear_texto = Radiobutton(win, text="Insertar Texto", variable=opcion, value=3);
radio_crear_texto.grid(row=7, column=2, sticky=W)

radio_crear_texto = Radiobutton(win, text="Agregar Texto", variable=opcion, value=4);
radio_crear_texto.grid(row=8, column=2, sticky=W)

radio_eliminar_carpeta = Radiobutton(win, text="Eliminar Carpeta", variable=opcion, value=5);
radio_eliminar_carpeta.grid(row=9, column=2, sticky=W)

radio_eliminar_archivo = Radiobutton(win, text="Eliminar Archivo", variable=opcion, value=6);
radio_eliminar_archivo.grid(row=10, column=2, sticky=W)

radio_leer_archivo = Radiobutton(win, text="Leer Archivo", variable=opcion, value=7);
radio_leer_archivo.grid(row=11, column=2, sticky=W)

radio_delete_carpeta = Radiobutton(win, text="Delete Carpeta", variable=opcion, value=8);
radio_delete_carpeta.grid(row=12, column=2, sticky=W)

radio_renombrar_archivo = Radiobutton(win, text="Renombrar Archivo", variable=opcion, value=9);
radio_renombrar_archivo.grid(row=13, column=2, sticky=W)

boton_crear = Button(win, text="Crear", command=operacion, background="yellow", fg='black', 
relief="groove", borderwidth=5, width=10)
boton_crear.grid(row=14,column=2, sticky=W)

boton_imprimir = Button(win, text="Imprimir", command=limpiar, background="green", fg='black', 
relief="groove", borderwidth=5, padx=2, width=10)
boton_imprimir.grid(row=14,column=2, sticky=N)

boton_limpiar = Button(win, text="Limpiar", command=limpiar, background="red", fg='white', 
relief="groove", borderwidth=5, padx=2, width=10 )
boton_limpiar.grid(row=14,column=2, sticky=E)

text = Text(win, width=46, height=7, font=('Time', 10), wrap='word', fg='#4A7A8C')
text.grid(columnspan=6, pady=11, padx=13)


win.mainloop()
