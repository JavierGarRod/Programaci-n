package org.example.Tema1.ActividadesU1Java.Funciones;

public class Ejercicio0001 {
    static void main() {
        int x = 144;
        int y = 999;
        Ejercicio0001 referencia = new Ejercicio0001();
        int sum = referencia.suma(x, y);
        int res = referencia.resta(x, y);
        float divi = referencia.division(x, y);
        int multi = referencia.multiplicacion(x, y);
    }

    int suma(int x, int y) {
        int sumas = x + y;
        System.out.println(sumas);

        return sumas;
    }
    int resta(int x, int y){
        int restas = x - y;
        System.out.println(restas);

        return restas;
    }

    float division (int x, int y){
        float div= ((float)x / y);
        System.out.println(div);

        return div;
    }

    int multiplicacion (int x, int y){
        int mult=x * y;
        System.out.println(mult);

        return mult;
    }

}
