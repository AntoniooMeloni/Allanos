# Protocolo de Comunicação All-anos (Bluetooth)

A comunicação é feita através de strings JSON.

## App -> Raspberry Pi

### 1. Pedir a lista de dispositivos
Envia:
```json
{ "command": "get_devices" }