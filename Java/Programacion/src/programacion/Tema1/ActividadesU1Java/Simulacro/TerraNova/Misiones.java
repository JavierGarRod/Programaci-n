package programacion.Tema1.ActividadesU1Java.Simulacro.TerraNova;

import java.time.LocalDate;

public class Misiones {
    private int codNum;
    private String nombre;
    private LocalDate fechaLanzamiento;
    private Nave nave;
    private Estado estado;

    public Misiones(int codNum, String nombre, LocalDate fechaLanzamiento, Nave nave, Estado estado) {
        this.codNum = codNum;
        this.nombre = nombre;
        setFechaLanzamiento(fechaLanzamiento);
        this.nave = nave;
        setEstado(estado);
    }

    public int getCodNum() {
        return codNum;
    }

    public void setCodNum(int codNum) {
        this.codNum = codNum;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public LocalDate getFechaLanzamiento() {
        return fechaLanzamiento;
    }

    public void setFechaLanzamiento(LocalDate fechaLanzamiento) {
        if(fechaLanzamiento.isBefore(LocalDate.now())){
            this.fechaLanzamiento=null;
        }
    }

    public Nave getNave() {
        return nave;
    }

    public void setNave(Nave nave) {
        this.nave = nave;
    }

    public Estado getEstado() {
        return estado;
    }

    public void setEstado(Estado estado) {
        this.estado = Estado.PLANIFICADA;
    }

    @Override
    public String toString() {
        return "Misiones{" +
                "codNum=" + getCodNum() +
                ", nombre='" + getNombre() + '\'' +
                ", fechaLanzamiento=" + getFechaLanzamiento() +
                ", nave=" + getNave() +
                ", estado=" + getEstado() +
                '}';
    }
}
