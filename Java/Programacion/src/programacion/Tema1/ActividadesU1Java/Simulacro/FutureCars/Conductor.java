package programacion.Tema1.ActividadesU1Java.Simulacro.FutureCars;

public class Conductores {
    private String nombre;
    private int añosExperiencia;

    public Conductores(String nombre, int aniosExperiencia) {
        this.nombre = nombre;
        this.añosExperiencia = aniosExperiencia;
    }

    public String getNombre() {
        return nombre;
    }

    public void conducir() {
        System.out.println(nombre + " conduciendo");
    }
}
