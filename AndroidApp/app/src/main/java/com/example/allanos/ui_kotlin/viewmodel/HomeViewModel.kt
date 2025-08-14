package com.example.allanos.ui_kotlin.viewmodel

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.allanos.data.datasource.BluetoothDataSource
import com.example.allanos.data.repository.DeviceRepository
import com.example.allanos.model.Device
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

class HomeViewModel : ViewModel() {
    // Instanciação direta para simplificar. O ideal é usar Injeção de Dependência (Hilt/Koin).
    private val repository = DeviceRepository(BluetoothDataSource())

    private val _devices = MutableStateFlow<List<Device>>(emptyList())
    val devices: StateFlow<List<Device>> = _devices

    private val _isLoading = MutableStateFlow(false)
    val isLoading: StateFlow<Boolean> = _isLoading

    init {
        fetchDevices()
    }

    fun fetchDevices() {
        viewModelScope.launch {
            _isLoading.value = true
            _devices.value = repository.getDevices()
            _isLoading.value = false
        }
    }

    fun onDeviceToggled(device: Device, isChecked: Boolean) {
        val newState = if (isChecked) "ON" else "OFF"

        // Atualiza a UI imediatamente para uma experiência fluida
        val currentList = _devices.value.toMutableList()
        val deviceIndex = currentList.indexOfFirst { it.id == device.id }
        if (deviceIndex != -1) {
            currentList[deviceIndex].state = newState
            _devices.value = currentList.toList() // Dispara a recomposição
        }

        // Envia o comando para o Raspberry Pi em background
        viewModelScope.launch {
            val success = repository.updateDeviceState(device.id, newState)
            if (!success) {
                // Se falhar, reverte a mudança na UI e mostra um erro (não implementado)
                fetchDevices()
            }
        }
    }
}