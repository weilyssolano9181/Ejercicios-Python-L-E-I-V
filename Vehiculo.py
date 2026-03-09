class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        nueva_velocidad = self.velocidad_actual + incremento
        
        if nueva_velocidad > self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima
            print("Has alcanzado la velocidad máxima del vehículo.")
        else:
            self.velocidad_actual = nueva_velocidad
        
        print("Velocidad actual: " + str(self.velocidad_actual) + " km/h")

    def frenar(self, decremento):
        nueva_velocidad = self.velocidad_actual - decremento
        
        if nueva_velocidad < 0:
            self.velocidad_actual = 0
            print("El vehículo se ha detenido completamente.")
        else:
            self.velocidad_actual = nueva_velocidad
            
        print("Velocidad actual: " + str(self.velocidad_actual) + " km/h")

    def verificar_limite(self, velocidad_limite):
        if self.velocidad_actual > velocidad_limite:
            print("Estás excediendo el límite de velocidad de " + str(velocidad_limite) + " km/h.")
        else:
            print("Vas a una velocidad dentro del límite de " + str(velocidad_limite) + " km/h.")


mi_auto = Vehiculo("Chevrolet", "Onix Turbo LT", 187)

print("- Bienvenido al simulador de conducción -")
print("Vehículo: " + mi_auto.marca + " " + mi_auto.modelo)

continuar = True

while continuar:
    print("\nSeleccione una opción:")
    print("1. Acelerar")
    print("2. Frenar")
    print("3. Verificar límite de velocidad")
    print("4. Salir")
    
    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        cantidad = int(input("¿Cuánto desea acelerar? "))
        mi_auto.acelerar(cantidad)
    elif opcion == "2":
        cantidad = int(input("¿Cuánto desea frenar? "))
        mi_auto.frenar(cantidad)
    elif opcion == "3":
        limite = int(input("Ingrese el límite de velocidad de la vía: "))
        mi_auto.verificar_limite(limite)
    elif opcion == "4":
        print("Saliendo del simulador...")
        continuar = False
    else:
        print("Opción no válida, por favor intente de nuevo.")