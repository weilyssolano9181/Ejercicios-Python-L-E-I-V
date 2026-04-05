class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre  # Atributo privado
        
        if precio > 0:
            self.__precio = precio
        else:
            self.__precio = 0
            print("Advertencia: El precio inicial no puede ser menor a 0. Se asignó 0.")

    
    def obtener_nombre(self):
        return self.__nombre

    def obtener_precio(self):
        return self.__precio

    
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            print(f"Precio actualizado a: {self.__precio}")
        else:
            print("Error: El precio debe ser mayor que cero. No se realizaron cambios.")

    def aplicar_descuento(self, porcentaje):
        
        if 0 <= porcentaje <= 100:
            descuento = self.__precio * (porcentaje / 100)
            self.__precio -= descuento
            print(f"Descuento del {porcentaje}% aplicado con éxito.")
        else:
            print("Error: Porcentaje de descuento inválido.")
            
joya = Producto("Anillo Wigsé", 25000)
print(f"Producto: {joya.obtener_nombre()}")
print(f"Precio: {joya.obtener_precio()}")

joya.aplicar_descuento(20) # Aplicamos 20%
print(f"Precio con descuento: {joya.obtener_precio()}")