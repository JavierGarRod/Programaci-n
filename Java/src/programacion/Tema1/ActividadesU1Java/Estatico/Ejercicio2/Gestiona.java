package src.programacion.Tema1.ActividadesU1Java.Estatico.Ejercicio2;

public class Gestiona {
    public static void main(String[] args) {

        GestionaTiendaDeAnimales tienda = new GestionaTiendaDeAnimales();

        tienda.addMascota(new Perro("Bobby", 3,1/02/2026 , "Pequinés", true));
        tienda.addMascota(new Loro("Paco", 2, 10/02/2026,"Marruecos", true));

        tienda.mostrarLista();
    }
}