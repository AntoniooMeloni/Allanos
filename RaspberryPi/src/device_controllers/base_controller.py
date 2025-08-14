from abc import ABC, abstractmethod

class BaseController(ABC):
    """Classe base abstrata para todos os controladores de dispositivo."""
    def __init__(self, device_id, name, pin):
        self.id = device_id
        self.name = name
        self.pin = pin
        self.state = "OFF"  # Estado inicial padrão
        self._setup_pin()

    @abstractmethod
    def _setup_pin(self):
        """Configura o pino GPIO."""
        pass

    @abstractmethod
    def set_state(self, new_state):
        """Define um novo estado para o dispositivo (ex: 'ON' ou 'OFF')."""
        pass

    def get_status(self):
        """Retorna um dicionário com o status atual do dispositivo."""
        return {"id": self.id, "name": self.name, "type": "relay", "state": self.state}