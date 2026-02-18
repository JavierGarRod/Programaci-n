package programacion.Tema1.ActividadesU1Java.Simulacro.TerraNova;

import java.time.LocalDate;

public class MisionExplo extends Misiones{
    private String dsetino;
    private int tripulacion;

    public MisionExplo(int codNum, String nombre, LocalDate fechaLanzamiento, Nave nave, Estado estado, String dsetino, int tripulacion) {
        super(codNum, nombre, fechaLanzamiento, nave, estado);
        this.dsetino = dsetino;
        this.tripulacion = tripulacion;
    }

    public String getDsetino() {
        return dsetino;
    }

    public void setDsetino(String dsetino) {
        this.dsetino = dsetino;
    }

    public int getTripulacion() {
        return tripulacion;
    }

    public void setTripulacion(int tripulacion) {
        this.tripulacion = tripulacion;
    }

    @Override
    public String toString() {
        return "MisionExplo{" +
                "dsetino='" + getDsetino() + '\'' +
                ", tripulacion=" + getTripulacion() +
                ", codNum=" + getCodNum() +
                ", nombre='" + getNombre() + '\'' +
                ", fechaLanzamiento=" + getFechaLanzamiento() +
                ", nave=" + getNave() +
                ", estado=" + getEstado() +
                '}';
    }
}
