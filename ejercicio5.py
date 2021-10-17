archivo = open("archivo2.txt", "a")
text = input("Ingresar: ")
archivo.writelines(text)
archivo.close()