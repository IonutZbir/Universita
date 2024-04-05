import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

public class PersonArchive{

    private Map <String, Person> personArchive;
    public PersonArchive() {
        this.personArchive = new HashMap<>();
    }

    public String readInput(Scanner input){
        String output = "";
        try {
            output = input.nextLine();
        }catch (Exception e) {
            System.out.println("Error: Input!!!!!");
        }
        return output;
    }

    public void createPerson(int numPerson){
        System.out.println("[Generazione di persone in corso]");
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < numPerson; i++) {

            System.out.println("Inserire:");
            System.out.println("Nome:");
            String nome = this.readInput(sc);

            System.out.println("Cognome:");
            String cognome = this.readInput(sc);

            System.out.println("Codice Fiscale:");
            String codice = this.readInput(sc);

            System.out.println("Data di nascita, gg/mm/aaaa:");
            String rawDate = this.readInput(sc);
            Date formattedDate = new Date();
            SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

            try {
                formattedDate = sdf.parse(rawDate);
                System.out.println(rawDate);
            } catch (ParseException e) {
                System.out.println("Invalid date format. Please use dd/MM/yyyy.");
            }

            System.out.println("""
                    Inserire:\s
                    [Impiegato]: 1\s
                    [Libero Professionista]:2\s
                    [Disocuppato]: 3""");

            int tipo = Integer.parseInt(this.readInput(sc));

            System.out.println("Inserire:");
            switch (tipo){
                case 1:
                    System.out.println("Matricola:");
                    String matricola = this.readInput(sc);

                    System.out.println("Livello:");
                    String livello = this.readInput(sc);

                    System.out.println("Mansione:");
                    String mansione = this.readInput(sc);

                    Impiegato p = new Impiegato(nome, cognome, codice, formattedDate, matricola, livello, mansione);
                    this.personArchive.put(codice, p);
                    break;
                case 2:
                    System.out.println("Professione:");
                    String professione = this.readInput(sc);

                    System.out.println("Partita IVA:");
                    String iva = this.readInput(sc);

                    LiberoProf l = new LiberoProf(nome, cognome, codice, formattedDate, professione, iva);
                    this.personArchive.put(codice, l);
                    break;
                case 3:
                    System.out.println("Iscrizione registro di dissocupazione:");
                    String registro = this.readInput(sc);

                    Disoccupato d = new Disoccupato(nome, cognome, codice, formattedDate, registro);
                    this.personArchive.put(codice, d);
                    break;
                default:
                    System.out.println("Input Sbagliato!!!");
                    break;
            }
        }
        sc.close();
    }

    @Override
    public String toString() {
        return this.personArchive.toString();
    }
}
