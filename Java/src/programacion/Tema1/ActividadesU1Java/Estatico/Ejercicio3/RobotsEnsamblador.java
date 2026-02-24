package src.programacion.Tema1.ActividadesU1Java.Estatico.Ejercicio3;

public class RobotsEnsamblador extends Robots{
    public RobotsEnsamblador(String modelo, double bateria, Estado estado, double combustible, String descripcion) {
        super(modelo, bateria, estado, combustible, descripcion);
    }

    @Override
    void ejecutarTarea() {
        System.out.println("Ensamblar piezas");
    }

    @Override
    boolean recargar() {
        if(estado.equals("APAGADO") && suficienteBateria()){
            System.out.println("Recargando por gasolina");
            return true;
        }
        else{
            System.out.println("Estoy encendido y no puedo recargar");
            return false;
        }
    }
}
