package programacion.Tema1.ActividadesU1Java.Herencias.Ej2;

public class Vehiculo {
    protected String matricula;
    protected String tipoEtiqueta; // A, B, C, ECO
    protected String ciudad;

    public Vehiculo(String matricula, String tipoEtiqueta, String ciudad) {this.matricula = matricula;
        this.tipoEtiqueta = tipoEtiqueta;
        this.ciudad = ciudad;
    }

    public boolean tieneLimitacionParaCircular() {
        if ((ciudad.equalsIgnoreCase("Madrid") || ciudad.equalsIgnoreCase("Barcelona"))
                && (tipoEtiqueta.equals("B") || tipoEtiqueta.equals("C"))) {
            return true;
        }

        if ((ciudad.equalsIgnoreCase("Valencia") || ciudad.equalsIgnoreCase("Sevilla"))
                && tipoEtiqueta.equals("C")) {
            return true;
        }

        return false;
    }

    @Override
    public String toString() {
        return "Vehiculo [matricula=" + matricula + ", etiqueta=" + tipoEtiqueta + ", ciudad=" + ciudad + "]";
    }
}