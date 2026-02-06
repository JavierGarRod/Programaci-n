package programacion.Tema1.ActividadesU1Java.Simulacro.AutosInteligentes;

public class Sensor {
    private double distanciaObstaculo; // en cm
    private double velocidad; // km/h

    public Sensor(double distanciaObstaculo, double velocidad) {
        this.distanciaObstaculo = distanciaObstaculo;
        this.velocidad = velocidad;
    }

    public boolean hayObstaculoCercano() {
        return distanciaObstaculo < 50;
    }

    public boolean excesoVelocidad() {
        return velocidad > 120;
    }

    public double getDistanciaObstaculo() {
        return distanciaObstaculo;
    }

    public double getVelocidad() {
        return velocidad;
    }
}
