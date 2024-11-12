from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class Producto:
    def __init__(self, codigo, nombre, precio_compra, ganancia, existencias):
        self.codigo = codigo
        self.nombre = nombre
        self.precio_compra = precio_compra
        self.ganancia = ganancia
        self.existencias = existencias

    def calcular_precio_venta(self):
        return round(self.precio_compra * (1 + self.ganancia), 2)

    def reducir_existencias(self, cantidad):
        if cantidad > self.existencias:
            raise ValueError(f"No hay suficientes existencias para {self.nombre}.")
        self.existencias -= cantidad

class Venta:
    def __init__(self, producto, cantidad, total_venta):
        self.producto = producto
        self.cantidad = cantidad
        self.total_venta = total_venta

class SistemaVentas:
    def __init__(self):
        self.productos = [
            Producto("983C", "Cheetos", 23, 0.25, 100),
            Producto("765D", "Cereal", 12, 0.10, 34),
            Producto("125A", "Leche", 30, 0.15, 89),
            Producto("045I", "Oreos", 15, 0.20, 10),
            Producto("402P", "Chocotorro", 8, 0.06, 1000)
        ]
        self.ventas = []

    def mostrar_productos(self):
        return self.productos

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def registrar_venta(self, producto, cantidad):
        try:
            producto.reducir_existencias(cantidad)
            total_venta = cantidad * producto.calcular_precio_venta()
            self.ventas.append(Venta(producto, cantidad, total_venta))
            return {
                'nombre': producto.nombre,
                'cantidad': cantidad,
                'total_venta': total_venta,
                'existencias_restantes': producto.existencias
            }
        except ValueError as e:
            return {'error': str(e)}

    def mostrar_ventas(self):
        return [{'producto': venta.producto.nombre, 'cantidad': venta.cantidad, 'total_venta': venta.total_venta} for venta in self.ventas]

sistema = SistemaVentas()

@app.route('/')
def index():
    productos = sistema.mostrar_productos()
    return render_template('indexTres.html', productos=productos)

@app.route('/vender', methods=['POST'])
def vender():
    try:
        codigo = request.form['codigo']
        cantidad = int(request.form['cantidad'])
        
        producto = sistema.buscar_producto(codigo)
        
        if producto:
            resultado_venta = sistema.registrar_venta(producto, cantidad)
            if 'error' not in resultado_venta:
                return jsonify(resultado_venta)
            else:
                return jsonify(resultado_venta), 400
        else:
            return jsonify({'error': 'Producto no encontrado'}), 404
    except (ValueError, KeyError) as e:
        return jsonify({'error': 'Datos de entrada no válidos'}), 400

@app.route('/ventas')
def ventas():
    ventas = sistema.mostrar_ventas()
    return jsonify(ventas)

if __name__ == '__main__':
    app.run(debug=True)

