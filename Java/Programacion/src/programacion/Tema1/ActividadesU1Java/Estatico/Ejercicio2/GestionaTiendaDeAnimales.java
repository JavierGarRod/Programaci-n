package Programacion.src.programacion.Tema1.ActividadesU1Java.Estatico.Ejercicio2;

import java.util.ArrayList;

public class GestionaTiendaDeAnimales {
    private ArrayList<Mascotas> mascotas = new ArrayList<>();

    public void addMascota(Mascotas m) {
        mascotas.add(m);
    }

    // 1. Mostrar lista de animales
    public void mostrarLista() {
        mascotas.forEach(System.out::println);
    }

    // 2. Dado un animal concreto, devolver su información
    public String infoMascota(Mascotas m) {
        return m.toString();
    }

    // 3. Mostrar todos los datos de todos los animales
    public void mostrarTodo() {
        mostrarLista();
    }

    // 4. Eliminar animales
    public boolean eliminar(Mascotas m) {
        return mascotas.remove(m);
    }

}