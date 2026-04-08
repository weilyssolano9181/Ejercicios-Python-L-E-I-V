#sistema escolar
class persona ():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
    
    def infopersona (self):
        return f"soy {self.nombre}, mi edad es {self.edad}"
    
class estudiante (persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def curso (self):
        return f"mi nombre es {self.nombre}, mi edad es {self.edad}, y estoy en el grado {self.grado} "
 
estudiante1 = estudiante("Liam", 8, 3)

print(estudiante1.curso())