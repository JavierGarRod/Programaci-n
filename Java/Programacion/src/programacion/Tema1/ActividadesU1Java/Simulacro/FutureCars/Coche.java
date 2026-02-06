package programacion.Tema1.ActividadesU1Java.Simulacro.AutosInteligentes;

public class Coche {
    private String marca;
    private String modelo;
    private String matricula;
    private Conductor duenio;
    private Sensor sensor;
    private Estado estado;

    public Coche(String marca, String modelo, String matricula,
                 Conductor duenio, Sensor sensor) {
        this.marca = marca;
        this.modelo = modelo;
        this.matricula = matricula;
        this.duenio = duenio;
        this.sensor = sensor;
        this.estado = Estado.APAGADO;
    }

    public void arrancar(Conductor conductor) {
        if (!conductor.equals(duenio)) {
            System.out.println("Solo el dueño puede arrancar el coche");
            return;
        }
        estado = Estado.ARRANCADO;
        System.out.println("Coche arrancado");
        conductor.conducir();
    }

    public void verificarParada() {
        while (estado == Estado.ARRANCADO) {
            if (sensor.hayObstaculoCercano()) {
                System.out.println("Obstáculo cercano detectado. El coche se apaga.");
                estado = Estado.APAGADO;
            }
            // en un sistema real habría espera / actualización de sensores
            break;
        }
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Coche)) return false;
        Coche coche = (Coche) o;
        return matricula.equals(coche.matricula);
    }

    @Override
    public int hashCode() {
        return Objects.hash(matricula);
    }
}
