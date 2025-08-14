package com.example.allanos.model;

// Modelo de dados em Java. Simples e estável.
public class Device {
    private String id;
    private String name;
    private String type;
    private String state;

    public Device(String id, String name, String type, String state) {
        this.id = id;
        this.name = name;
        this.type = type;
        this.state = state;
    }

    public String getId() { return id; }
    public String getName() { return name; }
    public String getType() { return type; }
    public String getState() { return state; }

    public void setState(String state) {
        this.state = state;
    }
}