import java.io.File;
import java.util.Scanner;

public class Negozio {

    public String partitaIva;
    public String sede;
    public String merceVenduta;
    public int inAttivitaDal;

    public Negozio(String path) {

        try {
            // Crea uno Scanner per il tuo file di testo
            Scanner scanner = new Scanner(new File(path));

            int counter = 0;
            // Leggi ogni riga del file e stampala
            while (scanner.hasNextLine()) {
                if(counter > 0) {
                   String line = scanner.nextLine().toLowerCase().trim();
                   String attributo = line.split(":")[0];
                   String valore = line.split(":")[1];

                     if(attributo.equals("partita_iva")) {
                          this.partitaIva = valore;
                     } else if(attributo.equals("sede")) {
                          this.sede = valore;
                     } else if(attributo.equals("merce_venduta")) {
                          this.merceVenduta = valore;
                     } else if(attributo.equals("in_attivita_dal")) {

                         int attivitaDal = Integer.parseInt(valore);
                         if(attivitaDal <= 2014 && attivitaDal >= 1800) {
                             this.inAttivitaDal = Integer.parseInt(valore);
                         } else {
                             System.out.println("Errore: l'anno di attività deve essere compreso tra il 1800 e il 2014");
                             return;
                         }

                     }else{
                          System.out.println("Attributo non riconosciuto: " + attributo);
                          return;
                     }
                }else{
                    scanner.nextLine();
                }
                counter++;
            }

            // Chiudi lo Scanner
            scanner.close();

            if(this.partitaIva == null || this.sede == null || this.merceVenduta == null || this.inAttivitaDal == 0) {
                System.out.println("Errore: uno o più attributi non sono stati inizializzati");
                return;
            }
        } catch (Exception e) {
            System.out.println("Errore: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
