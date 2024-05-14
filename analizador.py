# Importar módulos y paquetes necesarios
import re
from contexto.lectura import *
from contexto.escritura import *
from contexto.limpieza import *
from contexto.exploracion import *
from hashlib import sha1 # for the temp name's file
import time # for get the unixtime

# Rutas de los archivos de los cuales se va a extraer texto
stopwords_ruta = 'stopwords.txt'
lista_ruta_datos = 'archivo.txt'

#opciones Constantes no mover
lista_funciones = [ 'Agregar texto a analizar', 'Estadísticas generales', 'Barra de tendencia del discurso',  'Gráfica serie-tiempo', 'Nube de palabras','Gráfica dispersión léxica', 'Actualizar archivos']
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

def generate_temp():
    temp_name = str(round(time.time() * 1000))
    temp_path = sha1(temp_name.encode('utf-8')).hexdigest()
    return 'temp/'+temp_path+'.png'

def get_nombres():
    cont  = 1
    lista_aux = []
    with open(lista_ruta_datos, 'r') as archivo:
        for linea in archivo:
            if cont % 4 == 1:
                lista_aux.append(linea.strip())
            cont += 1
    return lista_aux

def get_rutas():
    cont  = 0
    lista_aux = []
    with open(lista_ruta_datos, 'r') as archivo:
        for linea in archivo:
            if cont % 4 == 1:
                lista_aux.append(linea.strip())
            cont += 1
    return lista_aux

def get_anios():
    i = 0
    anios = []
    with open(lista_ruta_datos, 'r') as archivo:
        for linea in archivo:
            if(i % 4 == 2):
                anios.append(int(linea.strip().split('/')[2]))
            i += 1
    anios = list(set(anios))
    anios.sort()
    return anios

def buscar_ruta(nombre):
    i = 0
    with open(lista_ruta_datos, 'r') as archivo:
        for linea in archivo:
            if(i == 1):
                return linea.strip()
            if(nombre == linea.strip()):
                i = 1

def serie_tiempo(palabras = []):
    ruta = ''
    palabra_en_un_anio = []
    palabras_en_anios = []
    veces_palabra = 0
    txt_aux = ''
    for palabra in palabras:
        for a in get_anios():
            with open(lista_ruta_datos, 'r') as archivo:
                for linea in archivo:
                    try:
                        if(int(linea.strip().split('/')[2]) == a):
                            txt_aux = leer_texto(ruta)
                            txt_aux = limpieza_texto(txt_aux,  n_min=4, lista_palabras=stopwords)
                            veces_palabra += txt_aux.split(' ').count(palabra)
                        ruta = linea.strip()
                    except IndexError:
                        ruta = linea.strip()
                    except ValueError:
                        ruta = linea.strip()
            palabra_en_un_anio.append(veces_palabra)
            veces_palabra = 0
        palabras_en_anios.append(palabra_en_un_anio)     
        palabra_en_un_anio = []   
    return palabras_en_anios

def hacer_serie_tiempo(dirty):
    cleanArray = dirty.split("\n")
    cleanArray.pop(-1)
    anios = get_anios()
    for a,b in zip(cleanArray, serie_tiempo(cleanArray)):
        plt.plot(anios, b , label=a)
    plt.title('Gráfica de Línea')
    plt.xlabel('Año')
    plt.ylabel('Veces dicha')
    plt.legend()
    serie_tmp_path = generate_temp()
    plt.savefig(serie_tmp_path)
    return serie_tmp_path

def hacer_wordcloud(nombre):
    texto = ''
    texto_archivo = leer_texto(buscar_ruta(nombre))
    texto += limpieza_texto(texto_archivo,  n_min=4, lista_palabras=stopwords)
    path_name = generate_temp()
    nube_palabras(texto, n_grama=1, ubicacion_archivo=path_name, semilla=130, dim_figura=(5,5), graficar=False)
    return path_name

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

def barra_tendencias(nombre):
    texto = ''
    path = buscar_ruta(nombre)
    temp_path = generate_temp()
    texto_archivo = leer_texto(path)
    texto += limpieza_texto(texto_archivo,  n_min=4, lista_palabras=stopwords)
    grafica_barchart_frecuencias(texto, ubicacion_archivo=temp_path,titulo='Frecuencias de palabras', dim_figura=(7,4),graficar=False)
    return temp_path

def dispersion_lexica(nombre, dirty_tokens):
    texto = ''
    path = buscar_ruta(nombre)
    tokens = dirty_tokens.split('\n')
    print(dirty_tokens)
    temp_path = generate_temp()
    texto_archivo = leer_texto(path)
    texto += limpieza_texto(texto_archivo, n_min=4, lista_palabras=stopwords)
    graficar_dispersion(texto, tokens,ubicacion_archivo=temp_path,auto_etiquetas = True, dim_figura=(6,3), graficar=False)
    return temp_path