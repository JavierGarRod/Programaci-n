package Programacion.src.programacion.Tema1.Resumen;

public class ResumenJava {
    static void main() {
        // =====================
        // CADENAS (String)
        // =====================

        String texto = "Hola Java";

        System.out.println(texto.length());
        System.out.println(texto.toUpperCase());
        System.out.println(texto.equals("Hola Java"));
        System.out.println(texto.charAt(0));
        System.out.println(texto.substring(0, 4));

        // =====================
        // IF - ELSE
        // =====================

        int edad = 18;

        if (edad >= 18) {
            System.out.println("Mayor de edad");
        } else {
            System.out.println("Menor de edad");
        }

        // =====================
        // SWITCH
        // =====================

        int dia = 2;

        switch (dia) {
            case 1:
                System.out.println("Lunes");
                break;
            case 2:
                System.out.println("Martes");
                break;
            case 3:
                System.out.println("Miércoles");
                break;
            default:
                System.out.println("Día no válido");
        }

        // =====================
        // FUNCIÓN
        // =====================

        int resultado = sumar(5, 3);
        System.out.println(resultado);

        // =====================
        // BUCLE WHILE
        // =====================

        int i = 0;
        while (i < 3) {
            System.out.println("While: " + i);
            i++;
        }

        // =====================
        // BUCLE DO WHILE
        // =====================

        int j = 0;
        do {
            System.out.println("Do While: " + j);
            j++;
        } while (j < 3);

        // =====================
        // BUCLE FOR
        // =====================

        for (int k = 0; k < 3; k++) {
            System.out.println("For: " + k);
        }

        // =====================
        // TABLAS (ARRAY)
        // =====================

        int[] numeros = {1, 2, 3, 4};

        for (int n = 0; n < numeros.length; n++) {
            System.out.println(numeros[n]);
        }

        // =====================
        // MATRICES
        // =====================

        int[][] matriz = {
                {1, 2, 3},
                {4, 5, 6}
        };

        for (int fila = 0; fila < matriz.length; fila++) {
            for (int col = 0; col < matriz[fila].length; col++) {
                System.out.print(matriz[fila][col] + " ");
            }
            System.out.println();
        }

        // =====================
        // EXPRESIONES REGULARES
        // =====================

        String email = "correo@gmail.com";
        if (email.matches("^[A-Za-z0-9+_.-]+@(.+)$")) {
            System.out.println("Email válido");} else {
            System.out.println("Email no válido");}
    }
}

// FUNCIÓN (metodo)

public static int sumar(int a, int b) {          //Se declara fuera del main y se llama dentro del main
    return a + b;                                //
}