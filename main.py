from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel, CTkTextbox, CTkComboBox, CTkImage
from tkinter import PhotoImage
from analizador import *
from form import  formulario
from viewer import viewer_img

#Colors definition
black = '#E2E8ED'
white = '#FFFFFF'

#Variables estáticas
root = CTk()
root.geometry('800x480+610+200')
root.config(bg = black)
root.resizable(False,False)
root.title('Interfaz v1.0')

current_path = ""
tipo_img = 1

#Functions
lista_nombres_archivos = get_nombres()

def button_event():
    global current_path
    opc = Combo_option.get()
    if opc == 'Agregar texto a analizar':
        formulario()
        root.mainloop()
    elif opc == 'Estadísticas generales':
        textbox.insert(index = "0.0", text = estadisticas(Combo_archives.get()), tags=None)
    elif opc == 'Barra de tendencia del discurso':
        barra_path = barra_tendencias(Combo_archives.get())
        current_path = barra_path
        change_image(barra_path, label_img)
    elif opc == 'Gráfica serie-tiempo':
        print(opc)
    elif opc == 'Gráfica dispersión léxica':
        print(opc)
        dirty = textbox.get("0.0", "end")
        dispersion_path = dispersion_lexica(Combo_archives.get(), dirty)
        current_path = dispersion_path
        change_image(dispersion_path, label_img,2)
        tipo_img = 2
    elif opc == 'Nube de palabras':
        wordcloud_path = hacer_wordcloud(Combo_archives.get())
        current_path = wordcloud_path
        change_image(wordcloud_path, label_img)
    elif opc == 'Actualizar archivos':
        lista_nombres_archivos = get_nombres()
        Combo_archives.configure(values = lista_nombres_archivos)
    else:
        print('ERROR')

#Change image
def change_image(new_image_path, label_img, tipo=1):
    global tipo_img
    # Cargar la nueva imagen
    new_photo = PhotoImage(file=new_image_path)
    if tipo == 1:
        proc_photo = new_photo.zoom(30)
        proc_photo = proc_photo.subsample(38)
        tipo_img = 1
    else:
        proc_photo = new_photo.zoom(10)
        proc_photo = proc_photo.subsample(33)
        tipo_img = 2
    label_img.configure(image=proc_photo)
    label_img.image = proc_photo

def show_img():
    print(tipo_img)
    viewer_img(root,current_path,tipo_img)
    root.mainloop()

#Graphic
graphic = PhotoImage(file = 'kiwi.png')
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

label_img = CTkLabel(graphic_frame, image=graph_img, text="")
label_img.grid(columnspan=1, row=0)

btn_zoom = CTkButton(graphic_frame, text="Mostrar en otra ventana", corner_radius=8, border_width=2, command=show_img)
btn_zoom.grid(columnspan=1, row=1,sticky='se', pady=35, padx=10)

#More Configs
root.columnconfigure(0,weight=1)
root.rowconfigure(0, weight=1)
root.call('wm', 'iconphoto', root._w, graphic)
root.mainloop()
