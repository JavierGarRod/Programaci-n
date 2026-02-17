package programacion.Tema1.ActividadesU1Java.Simulacro.Incidencias;

public class Incidente {
    private int idNum;
    private String nombre;
    private String descripcion;
    private String fechaInicio;
    private String fechaFin;
    Estado estado;
    Criticidad criticidad;
    Equipo equipo;

    public Incidente(int idNum, String nombre, String fechaInicio, String fechaFin, Estado estado, Criticidad criticidad, Equipo equipo) {
        this.idNum = idNum;
        this.nombre = nombre;
        this.fechaInicio = fechaInicio;
        setFechaFin(fechaFin);
        this.estado = estado;
        this.criticidad = criticidad;
        this.equipo = equipo;
    }

    public int getIdNum() {
        return idNum;
    }

    public void setIdNum(int idNum) {
        this.idNum = idNum;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public String getFechaInicio() {
        return fechaInicio;
    }

    public void setFechaInicio(String fechaInicio) {
        this.fechaInicio = fechaInicio;
    }

    public String getFechaFin() {
        return fechaFin;
    }

    public void setFechaFin(String fechaFin) {
        if(estado.equals("CERRADA")){
            this.fechaFin=fechaFin;
        }
        else{
            this.fechaFin=null;
        }
    }

    public Estado getEstado() {
        return estado;
    }

    public void setEstado(Estado estado) {
        this.estado = estado;
    }

    public Criticidad getCriticidad() {
        return criticidad;
    }

    public void setCriticidad(Criticidad criticidad) {
        this.criticidad = criticidad;
    }

    public Equipo getEquipo() {
        return equipo;
    }

    public void setEquipo(Equipo equipo) {
        this.equipo = equipo;
    }

    @Override
    public String toString() {
        return "Incidente{" + getNombre() +
                " - " + getEstado() +
                ": " + getCriticidad() +
                " - " + getFechaInicio()+
                " - " + getEquipo() +
                '}';
    }

    boolean esUrgente(Estado estado, int tiempoTranscurrido){
        if(estado.equals("CRITICA") || estado.equals("GRAVE") || estado.equals("MEDIA")){
            return true;
        }
        else{
            return false;
        }
    }
}
