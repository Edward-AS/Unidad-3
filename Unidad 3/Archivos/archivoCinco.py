# Programa para mostrar varias formas de leer y 
# escribir datos en un archivo de texto. 
file = open("myfile.txt","w") 
L = ["This is Lagos \n","This is Python \n","This is Fcc \n"] 

# Asignar ["This is Lagos \n","This is Python \n","This is Fcc \n"] 
# a la variable L 
#El \n se coloca para indicar fin de línea 
file.write("Hello There \n") 
file.writelines(L) 
file.close() 

# Usar close() para cambiar los modos de acceso a archivos 
file = open("myfile.txt","r+")  
print("Output of the Read function is ") 
print(file.read()) 
print() 

# La función seek(n) Mueve el puntero hacia el byte indicado, 
# el byte desde el principio. 
file.seek(0)  
print( "The output of the Readline function is ") 
print(file.readline())  
print() 
file.seek(0) 

# Mostrar la diferencia entre lectura y línea de lectura 
print("Output of Read(12) function is ")  
print(file.read(12)) 
print() 
file.seek(0) 
print("Output of Readline(8) function is ")  
print(file.readline(8)) 
file.seek(0) 

# Función de lectura de líneas 
print("Output of Readlines function is ")  
print(file.readlines())  
print() 
file.close()