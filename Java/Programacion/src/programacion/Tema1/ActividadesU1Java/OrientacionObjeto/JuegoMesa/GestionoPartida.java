package programacion.Tema1.ActividadesU1Java.OrientacionObjeto.JuegoMesa;

public class GestionPartida {
    static void main() {
        Participante pepe=new Participante("","Pepe",0,1234);
        Participante jose=new Participante("","Jose",0,1334);
        Participante elena=new Participante("","Elena",0,2234);
        Participante javi=new Participante("","Javi",0,5234);

        String[] participante=new String[4];
        participante[0] = pepe.getNombre();
        participante[1] = jose.getNombre();
        participante[2] = elena.getNombre();
        participante[3] = javi.getNombre();


    }
}
