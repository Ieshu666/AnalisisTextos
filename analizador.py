# Importar módulos y paquetes necesarios
import re
from contexto.lectura import *
from contexto.escritura import *
from contexto.limpieza import *
from contexto.exploracion import *

# Rutas de los archivos de los cuales se va a extraer texto
stopwords_ruta = 'C:/Users/Usuario/Documents/uni/4tosem/Ing_software/PROYECTOFINAL/stopwords.txt'
lista_ruta_datos = 'C:/Users/Usuario/Documents/uni/4tosem/Ing_software/PROYECTOFINAL/archivo.txt'

#opciones Constantes no mover
lista_funciones = ['Estadísticas generales', 'Nube de palabras', 'Agregar texto a analizar', 'Barra de tendencia del discurso','Gráfica dispersión léxica', 'Gráfica serie-tiempo', 'Actualizar archivos']
stopwords = leer_texto(stopwords_ruta).split('\n')

#ListasIm
lista_nombres_archivos = []
lista_rutas_archivos = []
archivos_seleccionados = []


def guardar_archivo_nuevo(lista_ruta_datos = lista_ruta_datos, archivo_ruta = 'texto.txt', nombre = 'texto_ejemplo', fecha = '21/03/06', autor = 'Juan Perez'):
    with open(lista_ruta_datos, 'a') as archivo:
        archivo.writelines(nombre + "\n")
        archivo.writelines(archivo_ruta + "\n")
        archivo.writelines(fecha + "\n")
        archivo.writelines(autor + "\n")

def get_nombres():
    cont  = 1
    lista_aux = []
    with open(lista_ruta_datos, 'r') as archivo:
        for linea in archivo:
            if cont % 4 == 1:
                lista_aux.append(linea.strip())
            cont += 1
    return lista_aux

def hacer_wordcloud(archivos = archivos_seleccionados):
    texto = ''
    for a in archivos:
        texto_archivo = leer_texto(a)
        texto += limpieza_texto(texto_archivo,  n_min=4, lista_palabras=stopwords)
    nube_palabras(texto, n_grama=1, ubicacion_archivo='salida/nube_uni.jpg', semilla=130, dim_figura=(5,5))
    
def estadisticas(nombre):
    texto = ''
    i = 0
    with open(lista_ruta_datos, 'r') as archivo:
            for linea in archivo:
                if(i == 3):
                    texto += " por " + linea.strip()
                    i = 0
                if(i == 2):
                    texto += "Fue escrito en " + linea.strip()
                    i = 3
                if(i == 1):
                    texto_ruta = str(str(linea).strip())
                    texto_archivo = leer_texto(texto_ruta)
                    palabras = len(texto_archivo.split(' '))
                    texto +=  "El texto " + nombre + " tiene " +  str(palabras) + ' palabras\n'
                    i = 2
                if(nombre == linea.strip()):
                    i = 1
                
    return texto