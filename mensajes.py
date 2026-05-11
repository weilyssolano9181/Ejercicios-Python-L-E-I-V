from abc import ABC, abstractmethod

class Notificacion(ABC):
    """Clase abstracta base para todas las notificaciones."""
    
    def __init__(self, destinatario: str):
        self.destinatario = destinatario
    
    @abstractmethod
    def enviar(self) -> str:
        """Método abstracto que cada subclase debe implementar."""
        pass
    
    def __str__(self):
        return f"Notificacion para: {self.destinatario}"


class EmailNotificacion(Notificacion):
    """Notificación por correo electrónico con asunto y cuerpo."""
    
    def __init__(self, destinatario: str, asunto: str, cuerpo: str):
        super().__init__(destinatario)
        self.asunto = asunto
        self.cuerpo = cuerpo
    
    def enviar(self) -> str:
        mensaje = (
            f"📧 Enviando EMAIL\n"
            f"   Para:    {self.destinatario}\n"
            f"   Asunto:  {self.asunto}\n"
            f"   Cuerpo:  {self.cuerpo}\n"
            f"   ✅ Email enviado exitosamente."
        )
        print(mensaje)
        return mensaje


class SMSNotificacion(Notificacion):
    """Notificación por SMS con límite de caracteres."""
    
    LIMITE_CARACTERES = 160
    
    def __init__(self, destinatario: str, mensaje: str):
        super().__init__(destinatario)
        if len(mensaje) > self.LIMITE_CARACTERES:
            raise ValueError(
                f"El mensaje excede el límite de {self.LIMITE_CARACTERES} caracteres. "
                f"Caracteres actuales: {len(mensaje)}"
            )
        self.mensaje = mensaje
    
    def enviar(self) -> str:
        resultado = (
            f"📱 Enviando SMS\n"
            f"   Para:      {self.destinatario}\n"
            f"   Mensaje:   {self.mensaje}\n"
            f"   Caracteres: {len(self.mensaje)}/{self.LIMITE_CARACTERES}\n"
            f"   ✅ SMS enviado exitosamente."
        )
        print(resultado)
        return resultado


# ── Demostración ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Email
    email = EmailNotificacion(
        destinatario="usuario@ejemplo.com",
        asunto="Bienvenido al sistema",
        cuerpo="Hola, tu cuenta ha sido creada exitosamente."
    )
    email.enviar()

    print()

    # SMS
    sms = SMSNotificacion(
        destinatario="+57 300 123 4567",
        mensaje="Tu código de verificación es: 482910"
    )
    sms.enviar()

    print()

    # SMS con mensaje demasiado largo (manejo de error)
    try:
        sms_largo = SMSNotificacion(
            destinatario="+57 300 987 6543",
            mensaje="A" * 161
        )
    except ValueError as e:
        print(f"⚠️  Error: {e}")