class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self._titular = titular  # Protegido para que la hija lo use
        self._saldo = saldo_inicial

    def consultar_saldo(self):
        return self._saldo

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Depósito de ${monto} exitoso.")
        else:
            print("El monto a depositar debe ser positivo.")

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, interes_anual):
        # super() hereda el constructor del padre
        super().__init__(titular, saldo_inicial)
        self.__interes_anual = interes_anual # Privado de esta clase

    def aplicar_interes(self):
        # Calculamos el interés sobre el saldo actual
        interes_ganado = self._saldo * (self.__interes_anual / 100)
        self._saldo += interes_ganado
        print(f"Interés del {self.__interes_anual}% aplicado: +${interes_ganado}")

    def consultar_interes(self):
        return self.__interes_anual


# === BLOQUE DE PRUEBA (Esto es lo que verás en la terminal) ===

if __name__ == "__main__":
    print("--- SIMULACIÓN BANCARIA ---")
    
    # 1. Creamos la cuenta
    mi_cuenta = CuentaAhorro("Weylis Acosta", 1000, 5) # Saldo 1000, Interés 5%
    
    print(f"Titular: {mi_cuenta._titular}")
    print(f"Saldo inicial: ${mi_cuenta.consultar_saldo()}")
    
    # 2. Aplicamos interés
    mi_cuenta.aplicar_interes()
    print(f"Saldo tras interés: ${mi_cuenta.consultar_saldo()}")
    
    # 3. Hacemos un depósito
    mi_cuenta.depositar(500)
    print(f"Saldo final: ${mi_cuenta.consultar_saldo()}")
    
    print("---------------------------")