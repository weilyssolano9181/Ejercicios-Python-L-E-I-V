class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self, cantidad):
        if self.stock >= cantidad:
            print("Disponibilidad de " + str(cantidad) + " unidades de " + self.nombre)
            return True
        else:
            print("No hay suficiente stock. Disponible " + str(self.stock) + " unidades.")
            return False

    def vender(self, cantidad):
        if self.stock >= cantidad:
            self.stock = self.stock - cantidad
            print("Venta exitosa. Se vendieron " + str(cantidad) + " unidades.")
            print("Stock restante: " + str(self.stock))
        else:
            print("Error: No se puede vender " + str(cantidad) + " unidades. Stock insuficiente.")

    def reabastecer(self, cantidad):
        self.stock = self.stock + cantidad
        print("Se han añadido " + str(cantidad) + " unidades al inventario.")
        print("Nuevo stock total: " + str(self.stock))


mi_producto = Producto("Atenea polvo suelto", 2300, 20)

mi_producto.verificar_disponibilidad(20)

mi_producto.vender(14)

mi_producto.verificar_disponibilidad(6)

mi_producto.vender(7)

mi_producto.reabastecer(20)

mi_producto.verificar_disponibilidad(7)

mi_producto.vender(7)