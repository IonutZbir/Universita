import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Menu {

    public List<Pietanza> pietanze;

    public Menu(){
        pietanze = new ArrayList<>();
    }

    public void addPietanza(Pietanza pietanza){
        pietanze.add(pietanza);
    }

    public void getMenu(){

        System.out.println("\nAntipasti");
        for (Pietanza pietanza : pietanze) {
            if(pietanza.portata == Portate.ANTIPASTI){
                //print delle informazioni e degli ingredienti
                pietanza.pietanzaToString();
            }
        }

        System.out.println("\nPrimi");
        for (Pietanza pietanza : pietanze) {
            if(pietanza.portata == Portate.PRIMI){
                //print delle informazioni e degli ingredienti
                pietanza.pietanzaToString();
            }
        }

        System.out.println("\nSecondi");
        for (Pietanza pietanza : pietanze) {
            if(pietanza.portata == Portate.SECONDI){
                //print delle informazioni e degli ingredienti
                pietanza.pietanzaToString();
            }
        }
    }

    public void addPietanzaManualmente(){

        try {

            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

            System.out.println("--------------------Starting inserimento della pietanza--------------------");
            System.out.println("Inserisci il nome della pietanza: ");
            String nome = reader.readLine();
            System.out.println("Inserisci il tempo di preparazione: ");
            int tempoPreparazione = Integer.parseInt(reader.readLine());

            Portate portataEnum = null;
            while(true){
                System.out.println("Inserisci la portata: ");
                System.out.println("1) Antipasti");
                System.out.println("2) Primi");
                System.out.println("3) Secondi");
                int portata = Integer.parseInt(reader.readLine());
                if(portata == 1){
                    portataEnum = Portate.ANTIPASTI;
                    break;
                }else if(portata == 2){
                    portataEnum = Portate.PRIMI;
                    break;
                }else if(portata == 3) {
                    portataEnum = Portate.SECONDI;
                    break;
                }else{
                    System.out.println("Portata non valida");
                }
            }
            System.out.println("Inserimento degli ingredienti...");
            List<Ingrediente> ingredienti = new ArrayList<>();
            while(true){
                System.out.println("Inserisci il nome dell'ingrediente: ");
                String nomeIngrediente = reader.readLine();
                System.out.println("Inserisci il costo per ettogrammo: ");
                double costoEttogrammo = Double.parseDouble(reader.readLine());
                System.out.println("Inserisci la quantita: ");
                int quantita = Integer.parseInt(reader.readLine());
                System.out.println("L'ingrediente è pubblico? (true/false)");
                boolean pubblico = Boolean.parseBoolean(reader.readLine());
                System.out.println("Vuoi inserire un altro ingrediente? (true/false)");
                boolean continua = Boolean.parseBoolean(reader.readLine());
                ingredienti.add(new Ingrediente(nomeIngrediente, costoEttogrammo, pubblico, quantita));
                if(!continua){
                    break;
                }
            }
            System.out.println("Ingredienti inseriti correttamente");
            pietanze.add(new Pietanza(nome, ingredienti, tempoPreparazione, portataEnum));
            System.out.println("Pietanza inserita correttamente");

        } catch (Exception e) {
            System.out.println("Errore nell'inserimento della pietanza");
        }
    }

    public void getRanking(){

        //creo una map per il ranking
        Map<String, Double> ranking = new HashMap<>();

        for(int i = 0; i < pietanze.size(); i++){

            int tempoDiPreparazione = pietanze.get(i).tempoPreparazione;
            double prezzo = pietanze.get(i).prezzo;
            double rapporto = prezzo/tempoDiPreparazione;

            ranking.put(pietanze.get(i).nome, rapporto);
        }

        //stampo il ranking
        System.out.println("Ranking delle pietanze");
        for (Map.Entry<String, Double> entry : ranking.entrySet()) {
            System.out.println("Pietanza: " + entry.getKey() + " Rapporto: " + entry.getValue());
        }
    }
}
