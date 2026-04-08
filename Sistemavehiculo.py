#sistema de vehiculos#
class vehiculo():
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año
    def infovehiculo (self):
        return f"este vehiculo es de la marca {self.marca} y es del año {self.año} "
 
class coche(vehiculo):
    def __init__(self, marca, año, modelo):
        super().__init__(marca, año)          
        self.modelo = modelo
    def infocoche (self):
        return f"el modelo {self.modelo}"
    
coche1 = coche("Onix", 2026, "Turbo") 
print(coche1.infocoche())
   