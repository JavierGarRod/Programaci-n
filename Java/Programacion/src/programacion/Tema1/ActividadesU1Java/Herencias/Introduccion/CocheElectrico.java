package programacion.Tema1.ActividadesU1Java.Herencias.Ej2;

public class CocheElectrico extends Automovil {

    private String tipoBateria; // LFP o NCM

    public CocheElectrico(String matricula, String tipoEtiqueta, String ciudad, int numPuertas, String tipoBateria) {
        super(matricula, tipoEtiqueta, ciudad, numPuertas);

        if (!tipoBateria.equals("LFP") && !tipoBateria.equals("NCM")) {
            throw new IllegalArgumentException("Tipo de batería no válido");
        }

        this.tipoBateria = tipoBateria;
    }

    @Override
    public String toString() {
        return super.toString() + " CocheElectrico [batería=" + tipoBateria + "]";
    }
}