import java.io.IOError;
import java.io.IOException;
import java.util.Date;
import java.util.Scanner;

public class Dipendente {

    public String nome;
    public String cognome;
    public Date dataNascita;
    public String matricola;
    public Dipartimento dipartimento;
    public Mansione mansione;
    public int livello;
    public String matricolaCapoDiretto;

    public Dipendente(int numeroIscrizione) {

        Scanner scanner = new Scanner(System.in);

        try {

            System.out.println("Inserisci il nome del dipendente");
            String nome = scanner.nextLine();
            this.nome = nome;

            System.out.println("Inserisci il cognome del dipendente");
            String cognome = scanner.nextLine();
            this.cognome = cognome;

            System.out.println("Inserisci la data di nascita del dipendente nel formato gg/mm/aaaa");
            String leggiData = scanner.nextLine();
            Date data = new Date(leggiData);
            this.dataNascita = data;

            while (true) {
                System.out.println("Inserisci il dipartimento del dipendente tra MARKETING, RISORSE_UMANE, SVILUPPO");
                String dipartimento = scanner.nextLine().toLowerCase().trim();

                if (dipartimento.equals("marketing")) {
                    this.dipartimento = Dipartimento.MARKETING;
                    break;
                } else if (dipartimento.equals("risorse_umane")) {
                    this.dipartimento = Dipartimento.RISORSE_UMANE;
                    break;
                } else if (dipartimento.equals("sviluppo")) {
                    this.dipartimento = Dipartimento.SVILUPPO;
                    break;
                } else {
                    System.out.println("Dipartimento non valido, riprova");
                }
            }

            while (true) {
                System.out.println("Inserisci la mansione del dipendente tra DIRETTORE, RESPONSABILE, IMPIEGATO, STAGISTA");
                String mansione = scanner.nextLine().toLowerCase().trim();

                if (mansione.equals("direttore")) {
                    this.mansione = Mansione.DIRETTORE;
                    break;
                } else if (mansione.equals("responsabile")) {
                    this.mansione = Mansione.RESPONSABILE;
                    break;
                } else if (mansione.equals("impiegato")) {
                    this.mansione = Mansione.IMPIEGATO;
                    break;
                } else if (mansione.equals("stagista")) {
                    this.mansione = Mansione.STAGISTA;
                    break;
                } else {
                    System.out.println("Mansione non valida, riprova");
                }
            }

            if(this.mansione == Mansione.DIRETTORE){
                this.livello = 8;
            }else {
                while (true) {
                    System.out.println("Inserisci il livello del dipendente: ");
                    int livello = scanner.nextInt();

                    if (livello > 0 && livello < 9) {
                        this.livello = livello;
                        break;
                    } else {
                        System.out.println("Il livello deve essere compreso tra 1 e 8, riprova");
                    }
                }
            }

            //handling livello

            if(livello < 8) {
                while (true) {

                    System.out.println("Inserisci la matricola del capo diretto del dipendente");
                    String matricolaCapoDiretto = scanner.nextLine();
                    if (!matricolaCapoDiretto.startsWith("CLT_")) {
                        System.out.println("Matricola non valida");
                        continue;
                    } else {
                        this.matricolaCapoDiretto = matricolaCapoDiretto;
                        break;
                    }
                }
            }else{
                this.matricolaCapoDiretto = null;
            }

            this.matricola = "CLT_" + numeroIscrizione;
        } catch (Exception e) {
            System.out.println("Si è verificato un errore durante l'inserimento dei dati del dipendente");
            e.printStackTrace();
        }
    }

    public void changeInfo() {

        while (true) {

            System.out.println("Quale informazione vuoi cambiare?");
            System.out.println("1. Nome");
            System.out.println("2. Cognome");
            System.out.println("3. Data di nascita");
            System.out.println("4. Dipartimento");
            System.out.println("5. Mansione");
            System.out.println("6. Livello");
            System.out.println("7. Matricola capo diretto");

            Scanner scanner = new Scanner(System.in);

            int scelta = scanner.nextInt();
            if (scelta < 1 || scelta > 7) {
                System.out.println("Scelta non valida, riprova");
                continue;
            } else {

                switch (scelta) {
                    case 1:
                        System.out.println("Inserisci il nuovo nome del dipendente");
                        String nome = scanner.nextLine();
                        this.nome = nome;
                        break;
                    case 2:
                        System.out.println("Inserisci il nuovo cognome del dipendente");
                        String cognome = scanner.nextLine();
                        this.cognome = cognome;
                        break;
                    case 3:
                        System.out.println("Inserisci la nuova data di nascita del dipendente nel formato gg/mm/aaaa");
                        String leggiData = scanner.nextLine();
                        Date data = new Date(leggiData);
                        this.dataNascita = data;
                        break;
                    case 4:
                        while (true) {
                            System.out.println("Inserisci il nuovo dipartimento del dipendente tra MARKETING, RISORSE_UMANE, SVILUPPO");
                            String dipartimento = scanner.nextLine().toLowerCase().trim();

                            if (dipartimento.equals("marketing")) {
                                this.dipartimento = Dipartimento.MARKETING;
                                break;
                            } else if (dipartimento.equals("risorse_umane")) {
                                this.dipartimento = Dipartimento.RISORSE_UMANE;
                                break;
                            } else if (dipartimento.equals("sviluppo")) {
                                this.dipartimento = Dipartimento.SVILUPPO;
                                break;
                            } else {
                                System.out.println("Dipartimento non valido, riprova");
                            }
                        }
                        break;
                    case 5:
                        while (true) {
                            System.out.println("Inserisci la nuova mansione del dipendente tra DIRETTORE, RESPONSABILE, IMPIEGATO, STAGISTA");
                            String mansione = scanner.nextLine().toLowerCase().trim();

                            if (mansione.equals("direttore")) {
                                this.mansione = Mansione.DIRETTORE;
                                break;
                            } else if (mansione.equals("responsabile")) {
                                this.mansione = Mansione.RESPONSABILE;
                                break;
                            } else if (mansione.equals("impiegato")) {
                                this.mansione = Mansione.IMPIEGATO;
                                break;
                            } else if (mansione.equals("stagista")) {
                                this.mansione = Mansione.STAGISTA;
                                break;
                            }


                        }
                }
            }
        }
    }

    //costruttore per test, passare i parametri in ordine: nome, cognome, dataNascita, dipartimento, mansione, livello, matricolaCapoDiretto
    public Dipendente(String nome, String cognome, Date dataNascita, Dipartimento dipartimento, Mansione mansione, int livello, String matricolaCapoDiretto){
        this.nome = nome;
        this.cognome = cognome;
        this.dataNascita = dataNascita;
        this.dipartimento = dipartimento;
        this.mansione = mansione;
        this.livello = livello;
        this.matricolaCapoDiretto = matricolaCapoDiretto;
    }

    public void printInfo() {
        System.out.println("-----------------");
        System.out.println("Nome: " + this.nome);
        System.out.println("Cognome: " + this.cognome);
        System.out.println("Data di nascita: " + this.dataNascita);
        System.out.println("Matricola: " + this.matricola);
        System.out.println("Dipartimento: " + this.dipartimento);
        System.out.println("Mansione: " + this.mansione);
        System.out.println("Livello: " + this.livello);
        System.out.println("Matricola capo diretto: " + this.matricolaCapoDiretto);
    }
}
