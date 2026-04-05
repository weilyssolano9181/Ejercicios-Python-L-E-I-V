class Rectangulo:
    def __init__(self, largo, ancho):
        
        if largo > 0 and ancho > 0:
            self.__largo = largo
            self.__ancho = ancho
        else:
            raise ValueError("El largo y el ancho deben ser mayores a cero.")

    
    def cambiar_dimensiones(self, nuevo_largo, nuevo_ancho):
        if nuevo_largo > 0 and nuevo_ancho > 0:
            self.__largo = nuevo_largo
            self.__ancho = nuevo_ancho
            print(f"Dimensiones actualizadas: {self.__largo}x{self.__ancho}")
        else:
            print("Error: Las dimensiones deben ser números positivos.")

    
    def calcular_area(self):
        # Área = largo * ancho
        return self.__largo * self.__ancho

    def calcular_perimetro(self):
        # Perímetro = 2 * (largo + ancho)
        return 2 * (self.__largo + self.__ancho)


    def consultar_dimensiones(self):
        return {"largo": self.__largo, "ancho": self.__ancho}

rect = Rectangulo(10, 5)
print(f"Dimensiones actuales: {rect.consultar_dimensiones()}")
print(f"El área es: {rect.calcular_area()}")
print(f"El perímetro es: {rect.calcular_perimetro()}")

rect.cambiar_dimensiones(-2, 10)