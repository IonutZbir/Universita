import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {


        Azienda azienda = new Azienda();

        //creazione dei dipententi
        azienda.generateDipendente();

        //cambio informazioni (bisogna specificare il numero di matricola)
        azienda.cambiaInformazioni();


        //calcolo dei regali
        ArrayList<Dipendente> regali = azienda.calcolaRegaliDiCompleanno();

        //calcolo dei dipendenti che hanno in comune dipartimneto mese e anno
        HashMap<String, ArrayList<Dipendente>> dipendentiInComune = azienda.calcolaDipendentiDipartimentoMeseAnnoComune();

    }
}