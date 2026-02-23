package src.programacion.Tema1.ActividadesU1Java.Estatico.Ejercicio2;

import java.time.LocalDate;

public class Loro extends Mascotas implements IAves{
    private String origen;
    private boolean habla;

    public Loro(String nombre, int edad, int fechaNacimiento, String origen, boolean habla) {
        super(nombre, edad, LocalDate.ofEpochDay(fechaNacimiento));
        this.origen = origen;
        this.habla = habla;
    }

    @Override
    public boolean volar() {
        return true;
    }

    @Override
    public boolean habla() {
        return true;
    }

    public void muestra() {
    }
}
