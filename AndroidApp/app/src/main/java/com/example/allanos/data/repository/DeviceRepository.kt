package com.example.allanos.data.repository

import com.example.allanos.data.datasource.BluetoothDataSource
import com.example.allanos.model.Device

// Repositório: abstrai a origem dos dados (Bluetooth, API, Banco de Dados, etc.)
class DeviceRepository(private val dataSource: BluetoothDataSource) {

    suspend fun getDevices(): List<Device> {
        return dataSource.getDevices()
    }

    suspend fun updateDeviceState(deviceId: String, newState: String): Boolean {
        return dataSource.setDeviceState(deviceId, newState)
    }
}