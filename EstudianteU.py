class Estudiante:

    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def verificar_aprobacion(self):
        if self.calificacion >= 3.0:
            print(self.nombre, "aprobó la materia.")
        else:
            print(self.nombre, "reprobó la materia.")

est1 = Estudiante("Liam", 21, 4.7)
est1.verificar_aprobacion()
est2 = Estudiante("Luciana", 19, 4.4)
est2.verificar_aprobacion()
est3 = Estudiante("Rodney", 22, 2.5)
est3.verificar_aprobacion()