package src.programacion.Tema1.ActividadesU1Java.Estatico.Ejercicio2;

import java.time.LocalDate;

public class Canario extends Mascotas implements IAves{
    private String color;
    private boolean canta;

    public Canario(String nombre, int edad, LocalDate fechaNacimiento) {
        super(nombre, edad, fechaNacimiento);
    }

    @Override
    public boolean volar() {
        return false;
    }

    @Override
    public boolean habla() {
        return false;
    }

    public void muestra(){};
}
