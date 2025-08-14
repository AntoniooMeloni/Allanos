# --- MOCK GPIO ---
# Para testar em um PC. No Raspberry Pi, comente esta seção.
class GPIO:
    BCM = "BCM"
    OUT = "OUT"
    def setup(self, pin, mode): print(f"GPIO: Pin {pin} set as {mode}")
    def output(self, pin, value): print(f"GPIO: Pin {pin} set to {value}")
    def setmode(self, mode): print(f"GPIO: Mode set to {mode}")
    def cleanup(): print("GPIO: Cleanup called")
# --- FIM DO MOCK ---

# No Raspberry Pi, descomente a linha abaixo e comente a classe mock acima
# import RPi.GPIO as GPIO

from .base_controller import BaseController

class RelayController(BaseController):
    """Controla um dispositivo conectado a um relé."""

    def _setup_pin(self):
        GPIO.setup(self.pin, GPIO.OUT)
        # Garante que o relé comece desligado
        GPIO.output(self.pin, 1) # Relés costumam ser LOW-ACTIVE (0 liga, 1 desliga)
        self.state = "OFF"

    def set_state(self, new_state):
        if new_state.upper() == "ON":
            GPIO.output(self.pin, 0) # Liga o relé
            self.state = "ON"
            print(f"Dispositivo '{self.name}' (pino {self.pin}) LIGADO.")
        elif new_state.upper() == "OFF":
            GPIO.output(self.pin, 1) # Desliga o relé
            self.state = "OFF"
            print(f"Dispositivo '{self.name}' (pino {self.pin}) DESLIGADO.")
        else:
            raise ValueError(f"Estado desconhecido: {new_state}")
        
        return self.get_status()