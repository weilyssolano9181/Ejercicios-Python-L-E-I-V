from abc import ABC, abstractmethod
from datetime import date
import re


# ── Excepciones personalizadas ────────────────────────────────────────────────

class PagoFallidoError(Exception):
    """Se lanza cuando un pago no puede procesarse."""
    pass

class SaldoInsuficienteError(PagoFallidoError):
    """Saldo de PayPal insuficiente para cubrir el monto."""
    pass

class TarjetaInvalidaError(PagoFallidoError):
    """Datos de tarjeta de crédito inválidos o expirados."""
    pass


# ── Clase abstracta ───────────────────────────────────────────────────────────

class MetodoPago(ABC):
    """Interfaz abstracta para todos los métodos de pago."""

    @abstractmethod
    def procesar_pago(self, monto: float) -> str:
        """Procesa un pago por el monto indicado (en USD)."""
        pass

    def _validar_monto(self, monto: float) -> None:
        if monto <= 0:
            raise ValueError(f"El monto debe ser positivo. Recibido: {monto}")


# ── Subclases ─────────────────────────────────────────────────────────────────

class TarjetaCredito(MetodoPago):
    """Pago mediante tarjeta de crédito con validación de datos."""

    def __init__(
        self,
        numero_tarjeta: str,
        fecha_expiracion: str,   # formato "MM/YY"
        codigo_seguridad: str,
        titular: str,
    ):
        self.titular = titular
        self.numero_tarjeta = self._validar_numero(numero_tarjeta)
        self.fecha_expiracion = self._validar_expiracion(fecha_expiracion)
        self.codigo_seguridad = self._validar_cvv(codigo_seguridad)

    # -- validaciones de atributos --

    def _validar_numero(self, numero: str) -> str:
        limpio = numero.replace(" ", "").replace("-", "")
        if not limpio.isdigit() or len(limpio) not in (13, 15, 16):
            raise TarjetaInvalidaError(
                f"Número de tarjeta inválido: '{numero}'. "
                "Debe tener 13, 15 o 16 dígitos."
            )
        return limpio

    def _validar_expiracion(self, fecha: str) -> str:
        if not re.fullmatch(r"\d{2}/\d{2}", fecha):
            raise TarjetaInvalidaError(
                f"Formato de fecha inválido: '{fecha}'. Use MM/YY."
            )
        mes, anio = int(fecha[:2]), int(fecha[3:]) + 2000
        if mes < 1 or mes > 12:
            raise TarjetaInvalidaError(f"Mes inválido: {mes}.")
        hoy = date.today()
        if (anio, mes) < (hoy.year, hoy.month):
            raise TarjetaInvalidaError(
                f"Tarjeta expirada: {fecha}."
            )
        return fecha

    def _validar_cvv(self, cvv: str) -> str:
        if not cvv.isdigit() or len(cvv) not in (3, 4):
            raise TarjetaInvalidaError(
                f"Código de seguridad inválido: '{cvv}'. Debe tener 3 o 4 dígitos."
            )
        return cvv

    # -- método principal --

    def procesar_pago(self, monto: float) -> str:
        self._validar_monto(monto)

        # Simulación de validación con el banco
        ultimos = self.numero_tarjeta[-4:]
        print(f"   🔍 Validando tarjeta **** **** **** {ultimos}...")
        print(f"   🔍 Verificando CVV y fecha de expiración...")
        print(f"   🔍 Consultando límite de crédito disponible...")

        # Simular rechazo si el monto es excesivamente alto
        if monto > 10_000:
            raise PagoFallidoError(
                f"Pago rechazado por el banco: monto ${monto:,.2f} supera el límite diario."
            )

        return (
            f"✅ Pago con tarjeta aprobado\n"
            f"   Titular:  {self.titular}\n"
            f"   Tarjeta:  **** **** **** {ultimos}\n"
            f"   Monto:    ${monto:,.2f}"
        )


class Paypal(MetodoPago):
    """Pago mediante cuenta PayPal con verificación de saldo."""

    def __init__(self, correo_electronico: str, saldo: float):
        self.correo_electronico = self._validar_correo(correo_electronico)
        self.saldo = self._validar_saldo(saldo)

    # -- validaciones de atributos --

    def _validar_correo(self, correo: str) -> str:
        patron = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
        if not re.fullmatch(patron, correo):
            raise ValueError(f"Correo electrónico inválido: '{correo}'.")
        return correo

    def _validar_saldo(self, saldo: float) -> float:
        if saldo < 0:
            raise ValueError("El saldo no puede ser negativo.")
        return saldo

    # -- método principal --

    def procesar_pago(self, monto: float) -> str:
        self._validar_monto(monto)

        print(f"   🔍 Autenticando cuenta {self.correo_electronico}...")
        print(f"   🔍 Saldo disponible: ${self.saldo:,.2f}")

        if self.saldo < monto:
            raise SaldoInsuficienteError(
                f"Saldo insuficiente: disponible ${self.saldo:,.2f}, "
                f"requerido ${monto:,.2f}."
            )

        self.saldo -= monto
        return (
            f"✅ Pago con PayPal aprobado\n"
            f"   Cuenta:   {self.correo_electronico}\n"
            f"   Monto:    ${monto:,.2f}\n"
            f"   Saldo restante: ${self.saldo:,.2f}"
        )


# ── Utilidad de prueba ────────────────────────────────────────────────────────

def ejecutar_pago(metodo: MetodoPago, monto: float) -> None:
    """Ejecuta un pago y muestra el resultado o el error."""
    tipo = type(metodo).__name__
    print(f"\n{'─'*50}")
    print(f"💳 Procesando pago de ${monto:,.2f} con {tipo}")
    print(f"{'─'*50}")
    try:
        resultado = metodo.procesar_pago(monto)
        print(resultado)
    except (PagoFallidoError, ValueError) as e:
        print(f"❌ Error: {e}")


# ── Demostración ──────────────────────────────────────────────────────────────

if __name__ == "__main__":

    # -- Tarjeta de crédito válida --
    tarjeta = TarjetaCredito(
        numero_tarjeta="4111 1111 1111 1111",
        fecha_expiracion="12/26",
        codigo_seguridad="123",
        titular="Weilys Solano",
    )
    ejecutar_pago(tarjeta, 250.00)     # ✅ aprobado
    ejecutar_pago(tarjeta, 15_000.00)  # ❌ supera límite diario

    # -- PayPal con saldo suficiente --
    paypal = Paypal(correo_electronico="Weilys@ejemplo.com", saldo=500.00)
    ejecutar_pago(paypal, 120.00)  # ✅ aprobado
    ejecutar_pago(paypal, 400.00)  # ❌ saldo insuficiente (quedan 380)

    # -- Monto inválido --
    ejecutar_pago(paypal, -50.00)  # ❌ monto negativo

    # -- Construcción con datos inválidos --
    print(f"\n{'─'*50}")
    print("🧪 Pruebas de validación en construcción")
    print(f"{'─'*50}")

    casos = [
        ("Tarjeta expirada",    lambda: TarjetaCredito("4111111111111111", "01/20", "123", "Juan")),
        ("CVV inválido",        lambda: TarjetaCredito("4111111111111111", "12/26", "99X", "Juan")),
        ("Correo inválido",     lambda: Paypal("no-es-un-correo", 100)),
        ("Saldo negativo",      lambda: Paypal("x@x.com", -10)),
    ]

    for descripcion, constructor in casos:
        try:
            constructor()
        except (TarjetaInvalidaError, ValueError) as e:
            print(f"   ❌ {descripcion}: {e}")