package com.example.allanos.data.datasource

import com.example.allanos.model.Device
import kotlinx.coroutines.delay

// Fonte de dados que SIMULA a comunicação Bluetooth.
class BluetoothDataSource {

    // MOCK: Lista de dispositivos que seriam recebidos do Pi
    private val mockDevices = mutableListOf(
        Device("luz_sala", "Luz da Sala", "relay", "OFF"),
        Device("luz_quarto", "Luz do Quarto", "relay", "ON"),
        Device("ventilador", "Ventilador", "relay", "OFF")
    )

    // Simula o envio do comando "get_devices"
    suspend fun getDevices(): List<Device> {
        // TODO: Implementar a lógica real de envio/recebimento Bluetooth aqui
        println("DataSource: Simulando busca de dispositivos...")
        delay(1500) // Simula a latência da rede
        println("DataSource: Dispositivos recebidos.")
        return mockDevices
    }

    // Simula o envio do comando "set_state"
    suspend fun setDeviceState(deviceId: String, newState: String): Boolean {
        // TODO: Implementar a lógica real de envio/recebimento Bluetooth aqui
        println("DataSource: Enviando comando para $deviceId -> $newState")
        delay(500) // Simula a latência da rede

        // Atualiza nossa lista local para refletir a mudança
        mockDevices.find { it.id == deviceId }?.state = newState

        println("DataSource: Comando executado com sucesso.")
        return true // Simula uma resposta de sucesso
    }
}