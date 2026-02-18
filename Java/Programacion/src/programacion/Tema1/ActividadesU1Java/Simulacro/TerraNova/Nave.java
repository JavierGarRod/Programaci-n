package programacion.Tema1.ActividadesU1Java.Simulacro.TerraNova;

public class Nave {
    private String codId;
    private String modelo;
    private double hVuelo;
    private String igualdad;

    public Nave(String codId, String modelo, double hVuelo, String igualdad) {
        this.codId = codId;
        this.modelo = modelo;
        this.hVuelo = hVuelo;
        this.igualdad = igualdad;
    }

    public String getCodId() {
        return codId;
    }

    public void setCodId(String codId) {
        this.codId = codId;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public double gethVuelo() {
        return hVuelo;
    }

    public void sethVuelo(double hVuelo) {
        this.hVuelo = hVuelo;
    }

    public String getIgualdad() {
        return igualdad;
    }

    public void setIgualdad(String igualdad) {
        this.igualdad = igualdad;
    }

    @Override
    public String toString() {
        return "Nave{" +
                "codId='" + getCodId() + '\'' +
                ", modelo='" + getModelo() + '\'' +
                ", hVuelo=" + gethVuelo() +
                ", igualdad='" + getIgualdad() + '\'' +
                '}';
    }
}
