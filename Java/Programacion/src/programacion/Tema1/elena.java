package programacion.Tema1;

import java.util.Scanner;

public class elena {
    static void main() {
        Scanner sc = new Scanner(System.in);
        int num1=0;
        int num2=0;
        int suma=0;
        do{
            System.out.println("Introduce un num: ");
            num1 = sc.nextInt();
            System.out.println("Introduce otro num: ");
            num2 = sc.nextInt();
            suma=num1+num2;
            System.out.println(suma);
        } while(num1!=0 && num2!=0);
    }
}