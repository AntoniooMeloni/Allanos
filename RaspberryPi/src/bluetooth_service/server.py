import bluetooth

class BluetoothServer:
    def __init__(self, device_manager, port=1):
        self.manager = device_manager
        self.server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.port = port
        self.server_sock.bind(("", self.port))
        self.server_sock.listen(1)
        self.uuid = "00001101-0000-1000-8000-00805F9B34FB" # UUID Padrão para Serial Port Profile (SPP)

    def start(self):
        """Inicia o servidor Bluetooth e aguarda por conexões."""
        print(f"--- Servidor Bluetooth All-anos iniciado no canal {self.port} ---")
        bluetooth.advertise_service(self.server_sock, "AllanosServer",
                                  service_id=self.uuid,
                                  service_classes=[self.uuid, bluetooth.SERIAL_PORT_CLASS],
                                  profiles=[bluetooth.SERIAL_PORT_PROFILE])

        try:
            while True:
                print("Aguardando conexão de um cliente...")
                client_sock, client_info = self.server_sock.accept()
                print(f"Cliente conectado: {client_info}")
                self.handle_client(client_sock)
        except KeyboardInterrupt:
            print("\nServidor encerrado pelo usuário.")
        finally:
            self.stop()

    def handle_client(self, client_sock):
        """Lida com a comunicação de um cliente conectado."""
        try:
            while True:
                data = client_sock.recv(1024)
                if not data:
                    break
                
                command_json = data.decode('utf-8')
                print(f"Comando recebido: {command_json}")
                
                response = self.manager.handle_command(command_json)
                client_sock.send(response.encode('utf-8'))
                print(f"Resposta enviada: {response}")

        except bluetooth.btcommon.BluetoothError as e:
            print(f"Erro de conexão Bluetooth: {e}")
        finally:
            print("Cliente desconectado.")
            client_sock.close()

    def stop(self):
        """Encerra o socket do servidor."""
        print("Encerrando o servidor Bluetooth.")
        if self.server_sock:
            self.server_sock.close()