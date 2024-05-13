from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel, CTkTextbox, CTkComboBox, CTkImage, CTkToplevel
from tkinter import PhotoImage

black = '#E2E8ED'
white = '#FFFFFF'

def viewer_img(root,path, tipo = 1):
    new_window = CTkToplevel(root)
    new_window.title("Visualizador")

    # Cargar la imagen
    image_path = path
    new_image = PhotoImage(file=image_path)
    if tipo == 1:
	    proc_photo = new_image.zoom(10)
	    proc_photo = proc_photo.subsample(6)
	    print("uno")
    else:
	    proc_photo = new_image.zoom(10)
	    proc_photo = proc_photo.subsample(20)
	    print("dos")

    # Mostrar la imagen en un label en la nueva ventana
    new_label = CTkLabel(new_window, image=proc_photo, text="")
    new_label.image = proc_photo  # Mantener referencia a la imagen
    new_label.pack()