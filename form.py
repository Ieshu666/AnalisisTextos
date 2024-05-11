from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel, CTkTextbox
from tkinter import PhotoImage
from analizador import lista_ruta_datos, guardar_archivo_nuevo

#Variables


#Colors definition
black = '#E2E5DE'
white = '#FFFFFF'
def formulario():

    #Functions
    def button_event():
        if(entry_fecha.get() != '' and entry_archive.get() != '' and entry_autor.get() != '' and entry_nombre.get() != ''):
            archivo_ruta = entry_archive.get()
            nombre = entry_nombre.get()
            fecha = entry_fecha.get()
            autor = entry_autor.get()
            guardar_archivo_nuevo(lista_ruta_datos,archivo_ruta, nombre, fecha, autor)
        else:
            print("Datos inválidos")

    root_form = CTk()
    root_form.geometry('600x350+610+200')
    root_form.config(bg = black)
    root_form.resizable(False,False)
    root_form.title('Formulario')

    #Buttons frame
    buttons_frame = CTkFrame(root_form, bg_color= '#E2E5DE', fg_color='#E2E5DE')
    buttons_frame.configure(width=290) 
    buttons_frame.grid(column=0, row=0, sticky='nswe', padx=40,pady=40)


    #Components
    label_archive = CTkLabel(buttons_frame, text="Archivo")
    label_archive.grid(columnspan=1, column=1,row=0, pady=14, padx=14, sticky="w")
    label_nombre = CTkLabel(buttons_frame, text="Nombre")
    label_nombre.grid(columnspan=1, column=1,row=1, pady=14, padx=14, sticky="w")
    label_fecha = CTkLabel(buttons_frame, text="Fecha")
    label_fecha.grid(columnspan=1, column=1, row=2, pady=14, padx=14, sticky="w")
    label_autor = CTkLabel(buttons_frame, text="Autor")
    label_autor.grid(columnspan=1, column=1, row=3, pady=14, padx=14, sticky="w")

    entry_archive = CTkEntry(buttons_frame, placeholder_text="Ruta del documento", width=300)
    entry_archive.grid(column=2,row=0,columnspan=4,pady=10,padx=10)

    entry_nombre = CTkEntry(buttons_frame, placeholder_text="Nombre del archivo", width=300)
    entry_nombre.grid(column=2,row=1,columnspan=4,pady=10,padx=10)

    entry_fecha = CTkEntry(buttons_frame, placeholder_text="DD/MM/AAAA", width=300)
    entry_fecha.grid(column=2,row=2,columnspan=4,pady=10,padx=10)

    entry_autor = CTkEntry(buttons_frame, placeholder_text="Autor", width=300)
    entry_autor.grid(column=2,row=3,columnspan=4,pady=10,padx=10)

    btn_guardar = CTkButton(buttons_frame, text="Guardar", corner_radius=8, border_width=2, command = button_event)
    btn_guardar.grid(column=1,row=4, pady=8,padx=1)

    #More Configs
    root_form.columnconfigure(0,weight=1)
    root_form.rowconfigure(0, weight=1)
    root_form.mainloop()
    root_form.quit()