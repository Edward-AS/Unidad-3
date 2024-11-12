 #* NameError: se produce cuando una variable no se encuentra en el ámbito
"""
try:
    saludo = "Hola mundo"
    print(saludos)
except NameError as error:
    print(error)
"""

#* ValueError: se produce cuando la operación o función recibe un argumento con el tipo correcto pero el valor incorrecto.
"""
try:
    saludo = "Hola mundo"
    print(float(saludo))
except ValueError as error:
    print(error)
"""

#* ZeroDivisionError: se produce al dividir un valor o variable por cero.
"""
try:
    numero = 3
    print(numero / 0)
except ZeroDivisionError as error:
    print(f"No se puede dividir entre cero\n>> ERROR: {error}")
"""

#* SyntaxError: provocado por el analizador sintáctico cuando la sintaxis de Python es incorrecta.
"""
try:
    print(Hola mundo)
except SyntaxError as error:
    print(error)
"""

#* IndentationError: se produce cuando hay una sangría incorrecta.
"""
try:
    print("Hola mundo")
     print()
except IndentationError as error:
    print(error)
"""
#* AssertionError: se produce cuando falla la sentencia assert.
"""
try:
    assert 1 + 1 == 3
except AssertionError:
    print(False)
"""

#* SystemError: aparece cuando el intérprete detecta un error interno.
"""
import ctypes

try:
    ctypes.string_at(0) 
except SystemError as error:
    print("Se ha producido un SystemError:", error)
"""

#* MemoryError: se produce cuando los programas se quedan sin memoria.
"""
try:
    big_list = [1] * (10**10)
    print("Lista creada exitosamente.")
except MemoryError:
    print("Error: No hay suficiente memoria para crear la lista.")
"""

#* RuntimeError: se produce cuando un error no entra en ninguna categoría.
"""
def recursion_infinita():
    return recursion_infinita()

try:
    recursion_infinita()
except RuntimeError as e:
    print(f"Ocurrió un RuntimeError: {e}")
"""

#* KeyboardInterrupt: se activa cuando el usuario introduce teclas de interrupción (Ctrl + C o Supr).
"""
import time

try:
    count = 1
    while True:
        print(count)
        time.sleep(1)
        count += 1
except KeyboardInterrupt:
    print("\nPrograma interrumpido. Saliendo...")
"""

#* IndexError: se produce cuando el índice de una secuencia está fuera de rango
"""
lista = [1, 2, 3, 4, 5]
try:
    print(lista[6])
except IndexError as error:
    print(f"El índice está fuera de la lista: {error}")
"""

#* ImportError: se produce cuando falla la importación del módulo.
"""
try:
    import o

    os.system("cls")
except ImportError as error:
    print(error)
"""

#* TabError: se produce cuando las sangrías consisten en tabulaciones o espacios incoherentes.
"""
def calcular_area(base, altura):
    return base * altura / 2

try:
    print("Calculando el área del triángulo...")
    
    if True:
         base = 10
        altura = 5
        
         area = calcular_area(base, altura)  
       print("El área es:", area)

     print("Cálculo completado.")

except TabError as error:
    print(f"Ocurrió un error: {error}")
"""

#* AttributeError: se produce cuando falla la asignación o referencia de un atributo.
"""
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

persona = Persona("Paco")

try:
    print(persona.edad)
except AttributeError as error:
    print(f"El atributo no existe: {error}")
"""

#* EOFError: se produce cuando la función input() cumple la condición de fin de archivo.
"""
try:
    with open('ejemplo.txt', 'r') as archivo:
        while True:
            linea = archivo.readline()
            
            if not linea:
                raise EOFError("Se ha alcanzado el final del archivo")
            print(linea.strip())
except EOFError as error:
    print(error)
"""
