from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel, CTkTextbox, CTkComboBox, CTkImage
from tkinter import PhotoImage
from analizador import *
from form import  formulario

#Colors definition
black = '#E2E8ED'
white = '#FFFFFF'

#Variables estáticas

root = CTk()
root.geometry('800x480+610+200')
root.config(bg = black)
root.resizable(False,False)
root.title('Interfaz v1.0')

#Functions
lista_nombres_archivos = get_nombres()

def button_event():
    opc = Combo_option.get()
    if opc == 'Agregar texto a analizar':
        formulario()
        root.mainloop()
    elif opc == 'Estadísticas generales':
        textbox.insert(index = "0.0", text = estadisticas(Combo_archives.get()), tags=None)
        print(estadisticas(Combo_archives.get()))
    elif opc == 'Barra de tendencia del discurso':
        print(opc)
    elif opc == 'Gráfica serie-tiempo':
        print(opc)
    elif opc == 'Gráfica dispersión léxica':
        print(opc)
    elif opc == 'Nube de palabras':
        hacer_wordcloud(Combo_archives.get())        
    elif opc == 'Actualizar archivos':
        lista_nombres_archivos = get_nombres()
        Combo_archives.configure(values = lista_nombres_archivos)
    else:
        print('ERROR')

#Graphic
graphic = PhotoImage(file = 'C:/Users/Usuario/Documents/uni/4tosem/Ing_software/PROYECTOFINAL/kiwi.png')
graph_img = graphic.zoom(30)
graph_img = graph_img.subsample(64)

#Buttons frame
buttons_frame = CTkFrame(root, bg_color= white)
buttons_frame.configure(width=290) 
buttons_frame.grid(column=0, row=0, sticky='nsw', padx=10,pady=10)

#Graphic frame
graphic_frame = CTkFrame(root, bg_color= white)
graphic_frame.configure(width=500) 
graphic_frame.grid(column=0, row=0, sticky='nse', padx=10,pady=10)


#Components
Combo_archives = CTkComboBox(buttons_frame, values = lista_nombres_archivos, corner_radius=8, border_width=2)
Combo_archives.grid(columnspan=1, row=1, pady=8,padx=4)

Combo_option = CTkComboBox(buttons_frame, values = lista_funciones, corner_radius=8, border_width=2)
Combo_option.grid(columnspan=1,row=2,pady=8,padx=4) 

btn_analize = CTkButton(buttons_frame, text="Analizar", corner_radius=8, border_width=2, command = button_event)
btn_analize.grid(columnspan=1, row=3, pady=8,padx=4)

label_tokens = CTkLabel(buttons_frame, text="Ingrese linea por linea los tokens para la grafica", fg_color="transparent", wraplength=200, justify="left")
label_tokens.grid(columnspan=1, row=4, pady=4,padx=4)

textbox = CTkTextbox(buttons_frame)
textbox.grid(columnspan=1, row=5, pady=1, padx=4)

CTkLabel(graphic_frame, image=graph_img, text="").grid(columnspan=1, row=0)

btn_zoom = CTkButton(graphic_frame, text="Mostrar en otra ventana", corner_radius=8, border_width=2)
btn_zoom.grid(columnspan=1, row=1,sticky='se', pady=35, padx=10)

#More Configs
root.columnconfigure(0,weight=1)
root.rowconfigure(0, weight=1)
root.call('wm', 'iconphoto', root._w, graphic)
root.mainloop()