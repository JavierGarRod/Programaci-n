package programacion.Tema1.ActividadesU1Java.Simulacro.TerraNova;

import java.time.LocalDate;

public class MisionLogi extends Misiones{
    private double carga;

    public MisionLogi(int codNum, String nombre, LocalDate fechaLanzamiento, Nave nave, Estado estado, double carga) {
        super(codNum, nombre, fechaLanzamiento, nave, estado);
        this.carga = carga;
    }

    public double getCarga() {
        return carga;
    }

    public void setCarga(double carga) {
        this.carga = carga;
    }

    @Override
    public String toString() {
        return "MisionLogi{" +
                "carga=" + getCarga() +
                ", codNum=" + getCodNum() +
                ", nombre='" + getNombre() + '\'' +
                ", fechaLanzamiento=" + getFechaLanzamiento() +
                ", nave=" + getNave() +
                ", estado=" + getEstado() +
                '}';
    }
}
