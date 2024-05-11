# Importar módulos y paquetes necesarios
import re
from contexto.lectura import *
from contexto.escritura import *
from contexto.limpieza import *
from contexto.exploracion import *

# Rutas de los archivos de los cuales se va a extraer texto
stopwords_ruta = 'C:/Users/Usuario/Documents/uni/4tosem/Ing software/PROYECTOFINAL/stopwords.txt'
lista_ruta_datos = 'C:/Users/Usuario/Documents/uni/4tosem/Ing software/PROYECTOFINAL/archivo.txt'

#opciones Constantes no mover
lista_funciones = ['Estadísticas generales', 'Nube de palabras', 'Agregar texto a analizar', 'Barra de tendencia del discurso','Gráfica dispersión léxica', 'Gráfica serie-tiempo']
stopwords = leer_texto(stopwords_ruta).split('\n')

#ListasIm
lista_nombres_archivos = []
lista_rutas_archivos = []
archivos_seleccionados = []


def guardar_archivo_nuevo(lista_ruta_datos = lista_ruta_datos, archivo_ruta = 'texto.txt', nombre = 'texto_ejemplo', fecha = '21/03/06', autor = 'Juan Perez'):
    get_nombres()
    with open(lista_ruta_datos, 'a') as archivo:
        archivo.writelines(nombre + "\n")
        archivo.writelines(archivo_ruta + "\n")
        archivo.writelines(fecha + "\n")
        archivo.writelines(autor + "\n")

def get_nombres():
    cont  = 1
    with open(lista_ruta_datos, 'r') as archivo:
        for linea in archivo:
            if cont % 4 == 2:
                lista_nombres_archivos.append(linea.strip())
            cont += 1
    return lista_nombres_archivos

def hacer_wordcloud(archivos = archivos_seleccionados):
    texto = ''
    for a in archivos:
        texto_archivo = leer_texto(a)
        texto += limpieza_texto(texto_archivo,  n_min=4, lista_palabras=stopwords)
    nube_palabras(texto, n_grama=1, ubicacion_archivo='salida/nube_uni.jpg', semilla=130, dim_figura=(5,5))
    
def estadisticas(archivos):
    texto = ''
    i = 0
    with open(lista_ruta_datos, 'r') as archivo:
        for a in archivos:
            for linea in archivo:
                if(a == linea.strip()):
                    texto_archivo = leer_texto(a)
                    palabras = len(texto_archivo.split(' '))
                    texto += palabras + '\n'
                    i = 4
                if(i > 0):
                    texto += linea.strip() + '\n'
                    i-=1
    return texto