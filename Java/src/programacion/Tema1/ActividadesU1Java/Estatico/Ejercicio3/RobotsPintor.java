package src.programacion.Tema1.ActividadesU1Java.Estatico.Ejercicio3;

public class RobotsPintor extends Robots{
    public RobotsPintor(String modelo, double bateria, Estado estado, double combustible, String descripcion) {
        super(modelo, bateria, estado, combustible, descripcion);
    }

    @Override
    void ejecutarTarea() {
        System.out.println("Aplica pintura a los vehículos de manera uniforme");
    }

    @Override
    boolean recargar() {
        System.out.println("Recargando por electricidad");
        return true;
    }

    @Override
    public String toString() {
        return "RobotsPintor{" +
                ", estado=" + getEstado() +
                ", id=" + getId() +
                ", modelo='" + getModelo() + '\'' +
                ", bateria=" + getBateria() +
                ", estado=" + getEstado() +
                ", combustible=" + getCombustible() +
                ", descripcion='" + getDescripcion() + '\'' +
                '}';
    }
}
