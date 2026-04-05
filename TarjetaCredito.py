class TarjetaCredito:
    def __init__(self, numero, titular, limite_credito):
        self.__numero = numero          
        self.__titular = titular        
        self.__limite_credito = limite_credito 
        self.__saldo_utilizado = 0      

    def realizar_compra(self, monto):
        
        if self.__saldo_utilizado + monto <= self.__limite_credito:
            self.__saldo_utilizado += monto
            print(f"Compra autorizada por ${monto}. Saldo utilizado: ${self.__saldo_utilizado}")
        else:
            cupo_disponible = self.__limite_credito - self.__saldo_utilizado
            print(f"Compra RECHAZADA. Solo tienes ${cupo_disponible} de cupo disponible.")

    def pagar_tarjeta(self, monto):
        if monto > 0 and monto <= self.__saldo_utilizado:
            self.__saldo_utilizado -= monto
            print(f"Pago de ${monto} recibido. Cupo liberado.")
        else:
            print("Error: El monto del pago es inválido o excede la deuda actual.")

    def consultar_estado(self):
        return {
            "Titular": self.__titular,
            "Límite Total": self.__limite_credito,
            "Deuda Actual": self.__saldo_utilizado,
            "Disponible": self.__limite_credito - self.__saldo_utilizado
        }

if __name__ == "__main__":
    print("--- SISTEMA DE CRÉDITO ---")
    
    
    mi_tarjeta = TarjetaCredito("1234-5678", "Weylis Acosta", 1000000)
    
    
    mi_tarjeta.realizar_compra(800000)
    
    mi_tarjeta.realizar_compra(300000)
    
    mi_tarjeta.pagar_tarjeta(200000)
    
    mi_tarjeta.realizar_compra(300000) 
    
    print("\nEstado final:", mi_tarjeta.consultar_estado())
    print("--------------------------")