class Estudiante:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__notas = []  

    
    def agregar_nota(self, nota):
        if 0 <= nota <= 100:
            self.__notas.append(nota)
            print(f"Nota {nota} agregada a {self.__nombre}.")
        else:
            
            raise ValueError("La nota debe estar entre 0 y 100.")

    
    def calcular_promedio(self):
        if not self.__notas:
            return 0
        return sum(self.__notas) / len(self.__notas)


    def consultar_nombre(self):
        return self.__nombre

    def consultar_edad(self):
        return self.__edad

est = Estudiante("Weylis", 26)
est.agregar_nota(90)
est.agregar_nota(100)
est.agregar_nota(80)

print(f"Estudiante: {est.consultar_nombre()}")
print(f"Promedio final: {est.calcular_promedio()}")

est = Estudiante("Daniel", 20)
est.agregar_nota(80)
est.agregar_nota(90)
est.agregar_nota(100)

print(f"Estudiante: {est.consultar_nombre()}")
print(f"Promedio final: {est.calcular_promedio()}")