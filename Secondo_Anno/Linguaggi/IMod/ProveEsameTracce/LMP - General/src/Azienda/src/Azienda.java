import java.util.ArrayList;
import java.util.List;

public class Azienda {

    List<Dipendente> dipendenti;

    public static int numeroIscrizione;

    public Azienda(){
        numeroIscrizione = 0;
        dipendenti = new ArrayList<Dipendente>();
    }

    public void addDipendente(){

        numeroIscrizione++;
        Dipendente dipendente = new Dipendente(numeroIscrizione);
        dipendenti.add(dipendente);

        for(Dipendente d : dipendenti){
            d.printInfo();
        }
    }

    public void addDipendente(Dipendente dipendente){
        dipendenti.add(dipendente);
    }

    public void findChainOfCommand(String matricola){

        for(Dipendente d : dipendenti){
            if(d.matricola.equals(matricola)){
                if(d.mansione.equals(Mansione.DIRETTORE)){
                    System.out.println("Sei il direttore, non hai nessuno sopra di te");
                    return;
                }
            }
        }

        //ordino la lista dei dipendenti per livello utilizzando il bubble sort
        for(int i = 0; i < dipendenti.size(); i++){
            for(int j = 0; j < dipendenti.size() - 1; j++){
                if(dipendenti.get(j).livello > dipendenti.get(j + 1).livello){
                    Dipendente temp = dipendenti.get(j);
                    dipendenti.set(j, dipendenti.get(j + 1));
                    dipendenti.set(j + 1, temp);
                }
            }
        }

        boolean found = false;
        for(int i = 0; i < dipendenti.size(); i++){
            if(dipendenti.get(i).matricola.equals(matricola)){
                found = true;
            }else if(found){
                System.out.println("-----------------");
                System.out.println(dipendenti.get(i).nome);
                System.out.println(dipendenti.get(i).cognome);
                System.out.println(dipendenti.get(i).mansione);
                System.out.println(dipendenti.get(i).livello);
            }
        }
    }
}
