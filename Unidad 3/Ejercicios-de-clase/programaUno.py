class Producto:
    def __init__(self, codigo, nombre, precio_compra, ganancia, existencias):
        self.codigo = codigo
        self.nombre = nombre
        self.precio_compra = precio_compra
        self.ganancia = ganancia
        self.existencias = existencias

    def calcular_precio_venta(self):
        return self.precio_compra * (1 + self.ganancia)
    
    def reducir_existencias(self, cantidad):
        if cantidad > self.existencias:
            raise ValueError(f"No hay suficientes existencias para {self.nombre}.")
        self.existencias -= cantidad

class Venta:
    def __init__(self, cantidad, total_venta):
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
        print("\nProductos disponibles:")
        for producto in self.productos:
            print(f"{producto.codigo} - {producto.nombre} (${producto.precio_compra}) - Existencias: {producto.existencias}")

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def registrar_venta(self, producto, cantidad):
        try:
            producto.reducir_existencias(cantidad)
            total_venta = cantidad * producto.calcular_precio_venta()
            self.ventas.append(Venta(cantidad, total_venta))
            print(f"\nVenta realizada: {cantidad} unidades de {producto.nombre} por un total de ${total_venta:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

    def mostrar_ventas(self):
        print("\nMatriz de Ventas:")
        print("Cantidad vendida   Total$ Vendido")
        for venta in self.ventas:
            print(f"{venta.cantidad}                 ${venta.total_venta:.2f}")


from os import system

sistema = SistemaVentas()

while True:
    system("cls")
    sistema.mostrar_productos()
    codigo = input("\nIntroduce el código del producto que deseas comprar (o '*' para terminar): ").upper()

    if codigo == "*":
        break
    producto = sistema.buscar_producto(codigo)

    if producto:
        try:
            cantidad = int(input(f"¿Cuántas unidades de {producto.nombre} deseas comprar? "))
            sistema.registrar_venta(producto, cantidad)
        except ValueError:
            print("Cantidad no válida. Intenta nuevamente.")
    else:
        print("Código de producto no válido. Intenta nuevamente.")
    input()


if __name__ == "__main__":
    sistema.mostrar_ventas()
    print("\nFin del programa.")
