from abc import ABC, abstractmethod

class SensorTemperatura(ABC):
    """Clase abstracta base para sensores de temperatura."""

    def __init__(self, temperatura: float):
        self._temperatura = temperatura

    @abstractmethod
    def obtener_temperatura(self) -> float:
        """Retorna la temperatura en la unidad nativa del sensor."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class SensorCelsius(SensorTemperatura):
    """Sensor que trabaja en grados Celsius."""

    def obtener_temperatura(self) -> float:
        return self._temperatura

    def a_fahrenheit(self) -> float:
        """Convierte la temperatura interna a Fahrenheit."""
        return self._temperatura * 9 / 5 + 32

    def __str__(self) -> str:
        return (
            f"🌡️  SensorCelsius\n"
            f"   Celsius:    {self.obtener_temperatura():.2f} °C\n"
            f"   Fahrenheit: {self.a_fahrenheit():.2f} °F"
        )


class SensorFahrenheit(SensorTemperatura):
    """Sensor que trabaja en grados Fahrenheit."""

    def obtener_temperatura(self) -> float:
        return self._temperatura

    def a_celsius(self) -> float:
        """Convierte la temperatura interna a Celsius."""
        return (self._temperatura - 32) * 5 / 9

    def __str__(self) -> str:
        return (
            f"🌡️  SensorFahrenheit\n"
            f"   Fahrenheit: {self.obtener_temperatura():.2f} °F\n"
            f"   Celsius:    {self.a_celsius():.2f} °C"
        )


# ── Demostración ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sensor_c = SensorCelsius(100.0)
    print(sensor_c)

    print()

    sensor_f = SensorFahrenheit(98.6)
    print(sensor_f)

    print()

    # Verificación cruzada: 0 °C debe ser 32 °F
    freezing = SensorCelsius(0)
    print(f"Punto de congelación: {freezing.obtener_temperatura()} °C → {freezing.a_fahrenheit()} °F")

    # Verificación cruzada: 212 °F debe ser 100 °C
    boiling = SensorFahrenheit(212)
    print(f"Punto de ebullición:  {boiling.obtener_temperatura()} °F → {boiling.a_celsius()} °C")

    print()

    # Polimorfismo: lista mixta de sensores
    sensores: list[SensorTemperatura] = [
        SensorCelsius(37.0),     # temperatura corporal normal
        SensorFahrenheit(32.0),  # punto de congelación
        SensorCelsius(-40.0),    # donde °C y °F coinciden
    ]

    print("── Lecturas polimórficas ──")
    for s in sensores:
        print(f"   {type(s).__name__}: {s.obtener_temperatura():.1f}")