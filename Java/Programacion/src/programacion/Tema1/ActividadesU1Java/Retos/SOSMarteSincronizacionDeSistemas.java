package programacion.Tema1.ActividadesU1Java.Retos;

import java.util.Arrays;
import java.util.Scanner;

public class SOSMarteSincronizaciónDeSistemas {
    static void main() {
        String[] tabla={"Recurso","Cantidad","Nivel Crítico"};
        String [] recursos= new String[3];
        int[] cantidades= new int[3];
        int[] limites_alerta= new int [3];
        Scanner sc = new Scanner(System.in);
        System.out.println("Introduce la cantidad de recursos que deseas introducir: ");
        int rep = sc.nextInt();
        for (int i=0;i<rep;i++){
            System.out.println("Introduce el nombre del recurso: ");
            recursos[i] = sc.next();
            System.out.println("Introduce la cantidad: ");
            cantidades[i] = sc.nextInt();
            System.out.println("Introduce el nivel crítico: ");
            limites_alerta[i] = sc.nextInt();
        }
        System.out.println(Arrays.toString(tabla));
        for (int a=0;a<rep;a++){
            System.out.println(recursos[a]+" , "+cantidades[a]+" , "+limites_alerta[a]);
        }
    }
}
