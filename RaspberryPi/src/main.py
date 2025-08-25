import json
from device_controllers.relay_controller import RelayController, GPIO
from bluetooth_service.bt_server import BluetoothServer


# Mapeia o 'type' do JSON para a classe Python correspondente
CONTROLLER_MAP = {
    "relay": RelayController
}

class DeviceManager:
    def __init__(self, config_path):
        self.devices = {}
        self._load_devices(config_path)

    def _load_devices(self, config_path):
        print("Carregando dispositivos do arquivo de configuração...")
        GPIO.setmode(GPIO.BCM)
        with open(config_path, 'r') as f:
            config = json.load(f)
            for device_info in config['devices']:
                device_id = device_info['id']
                controller_class = CONTROLLER_MAP.get(device_info['type'])
                if controller_class:
                    self.devices[device_id] = controller_class(
                        device_id=device_id,
                        name=device_info['name'],
                        pin=device_info['pin']
                    )
                    print(f"- Dispositivo '{device_id}' carregado com sucesso.")
                else:
                    print(f"[AVISO] Tipo de dispositivo desconhecido: {device_info['type']}")

    def handle_command(self, command_json):
        """Processa um comando JSON e retorna uma resposta JSON."""
        try:
            command_data = json.loads(command_json)
            command = command_data.get("command")

            if command == "get_devices":
                all_statuses = [dev.get_status() for dev in self.devices.values()]
                return json.dumps({"status": "success", "data": all_statuses})

            elif command == "set_state":
                device_id = command_data.get("device_id")
                new_state = command_data.get("state")
                device = self.devices.get(device_id)
                if device:
                    updated_status = device.set_state(new_state)
                    return json.dumps({"status": "success", "data": updated_status})
                else:
                    return json.dumps({"status": "error", "message": "Dispositivo não encontrado."})
            else:
                return json.dumps({"status": "error", "message": "Comando desconhecido."})

        except Exception as e:
            return json.dumps({"status": "error", "message": str(e)})

    def cleanup(self):
        GPIO.cleanup()

def main():
    """Função principal para iniciar o servidor."""
    config_file = '../config/devices.json' # Ajuste o caminho para ser relativo ao main.py
    manager = DeviceManager(config_file)
    bt_server = BluetoothServer(device_manager=manager)
    
    try:
        bt_server.start()
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        manager.cleanup()
        bt_server.stop()

if __name__ == "__main__":
    main()