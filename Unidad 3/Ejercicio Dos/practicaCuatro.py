from flask import Flask, render_template, request

app = Flask(__name__)

class Menu:
    def __init__(self):
        self.opciones = {
            1: "Opción 1",
            2: "Opción 2",
            3: "Opción 3",
            4: "Opción 4",
            5: "Salir"
        }

    def obtener_opciones(self):
        return self.opciones

menu = Menu()

@app.route('/', methods=['GET', 'POST'])
def index():
    opciones = menu.obtener_opciones()
    seleccion = None
    if request.method == 'POST':
        opcion = int(request.form['opcion'])
        if 1 <= opcion <= 4:
            seleccion = f"Has seleccionado {opciones[opcion]}"
        elif opcion == 5:
            seleccion = "Saliendo..."
        else:
            seleccion = "Opción no válida. Intenta de nuevo."
    return render_template('indexCuatro.html', opciones=opciones, seleccion=seleccion)

if __name__ == '__main__':
    app.run(debug=True)
