package programacion.Tema1.ActividadesU1Java.Herencias.Ej2;

public class Automovil extends Vehiculo{
    private int numPuertas;

    public Automovil(String matricula, String tipoEtiqueta, String ciudad, int numPuertas) {
        super(matricula, tipoEtiqueta, ciudad);
        this.numPuertas = numPuertas;
    }
}
