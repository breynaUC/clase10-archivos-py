import os
import errno
from shutil import rmtree
from os import rmdir
def crearFile(file):
    archivo = open(file, "w")
    archivo.close()
def add(file, texto):
    archivo = open(file, "w")
    archivo.write(texto)
    archivo.close()
def adds(file, texto):
    archivo = open(file, "a")
    archivo.write("\n"+ texto)
    archivo.close()
def delete(file):
    os.remove(file)
def deleteCarpeta(carpeta):
    rmtree(carpeta)
def leer(file):
    archivo = open(file, "r")
    lineas = archivo.readlines()
    archivo.close()
    return lineas
def crearCarpeta(carpeta):
    try:
        os.mkdir(carpeta)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
def crearDirectorio(carpetas):
    os.makedirs(carpetas, exist_ok=True)
def delDirectorioFile(carpeta):
    rmtree(carpeta)
def delDirectorioVacio(carpeta_vacia):
    rmdir(carpeta_vacia)
def renombrarArchivo(fileNombreAntiguo,fileNombreNuevo):
    print(fileNombreAntiguo)
    print(fileNombreNuevo)
    os.rename(fileNombreAntiguo, fileNombreNuevo)
def fileAddList(lista):
    archivo = open('datos1.txt','w')
    archivo.writelines(lista)
    archivo.close()












