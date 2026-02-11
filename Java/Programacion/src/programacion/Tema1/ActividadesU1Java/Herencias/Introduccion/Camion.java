package programacion.Tema1.ActividadesU1Java.Herencias.Ej2;

public class Camion extends Vehiculo {

    private int mma;        // Masa Máxima Autorizada
    private int pasajeros;
    private String tipoCarnet;

    public Camion(String matricula, String tipoEtiqueta, String ciudad, int mma, int pasajeros) {
        super(matricula, tipoEtiqueta, ciudad);
        this.mma = mma;
        this.pasajeros = pasajeros;
        this.tipoCarnet = asignarCarnet();
    }

    private String asignarCarnet() {
        if (mma > 3500 && mma <= 7500) {
            return "C1";
        } else if (mma > 7500) {
            return "C";
        } else {
            return "B"; // Vehículos ligeros
        }
    }

    @Override
    public String toString() {
        return super.toString() + " Camion [MMA=" + mma + ", pasajeros=" + pasajeros + ", carnet=" + tipoCarnet + "]";
    }
}