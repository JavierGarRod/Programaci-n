package java.org.example.Tema1.ActividadesU1Java.Funciones;

import java.util.Scanner;

public class Ejercicio0002 {
    static void main() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Introduce un número: ");
        int num1=sc.nextInt();
        System.out.println("Introduce otro número: ");
        int num2=sc.nextInt();
        Ejercicio0002 referencia = new Ejercicio0002();
        int multi=referencia.multiplicacion(num1, num2);
        System.out.println(multi);
    }

    int multiplicacion (int num1, int num2){
        int mult = num1* num2;

        return mult;
    }
}
