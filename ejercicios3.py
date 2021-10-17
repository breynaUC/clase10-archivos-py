try:
    archivo = open("archivo1.txt","r")
    caracter = archivo.read(1)
    contador = 0
    while caracter != "":
        contador +=1
        caracter = archivo.read(1)
    archivo.close()
    print("Número de caracteres: %d"%contador)
except IOError:
    print("Error al leer el archivo...!");
