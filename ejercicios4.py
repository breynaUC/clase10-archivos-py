try:
    archivo = open("archivo1.txt","r")    
    contador = 0
    while True:
        caracter = archivo.read(1)
        if caracter.isspace():
            contador +=1
        if not caracter:
            break
    archivo.close()
    print("Número espacios en blanco: %d"%contador)
except IOError:
    print("Error al leer el archivo...!");