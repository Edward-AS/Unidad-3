from flask import Flask, render_template, request

app = Flask(__name__)

class Moneda:
    def __init__(self, billete):
        self.billete = billete
        self.uno = 0
        self.cinco = 0
        self.diez = 0

    def conversion(self):
        while self.billete > 0:
            if self.billete >= 10:
                self.billete -= 10
                self.diez += 1
            elif self.billete >= 5:
                self.billete -= 5
                self.cinco += 1
            else:
                self.billete -= 1
                self.uno += 1

    def obtener_resultado(self):
        return {
            "diez": self.diez,
            "cinco": self.cinco,
            "uno": self.uno
        }

@app.route('/')
def index():
    return render_template('indexDos.html')

@app.route('/cambiar', methods=['POST'])
def cambiar():
    cantidad = int(request.form['cantidad'])
    cambio = Moneda(cantidad)
    cambio.conversion()
    resultado = cambio.obtener_resultado()
    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)

