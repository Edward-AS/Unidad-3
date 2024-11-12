#Crea un archivo y lo establece en modo "escribir"
f = open("myfile.txt", "w")

#Escribe en el archivo
f.write("Hello There\n")


f.writelines(["Hello World \n", "You are welcome to Fcc\n"])


f.close()


