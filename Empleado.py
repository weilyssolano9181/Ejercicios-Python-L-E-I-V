class Empleado:
    
    total_empleados = 0

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        
        Empleado.total_empleados += 1

    @classmethod
    def cantidad_empleados(cls):
        return f"Total de empleados en la empresa: {cls.total_empleados}"


if __name__ == "__main__":
    print("--- REGISTRO DE NÓMINA ---")
    
    
    emp1 = Empleado("Weylis Acosta", 3000)
    emp2 = Empleado("Dayerlys Solano", 3500)
    emp3 = Empleado("Andrés Pérez", 2800)
    
    print(emp1.nombre, "- Registrado")
    print(emp2.nombre, "- Registrado")
    print(emp3.nombre, "- Registrado")
    
    print("\n" + Empleado.cantidad_empleados())
    print("--------------------------")