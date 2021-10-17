try:
    archivo = open("archivo1","r")
    for linea in archivo:
        print(linea)
    archivo.close()
except IOError:
    print("Error al abrir el archivo")