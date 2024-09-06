import java.io.IOException;
import java.util.*;

public class Azienda {

    private int numeroIscrizione;

    public Azienda() {
        this.numeroIscrizione = 0;
    }

    //Lista dei dipendenti
    ArrayList<Dipendente> listaDipendenti = new ArrayList<Dipendente>(0);

    public void generateDipendente() {

        try {

            while (true) {

                String nome;
                String cognome;
                Date dataDiNascita;
                Date dataDiAssunzione;
                String numeroMatricola;
                Dipartimento dipartimento;
                int livello;

                //Inserimento dei dati del dipendente

                Scanner scanner = new Scanner(System.in);

                while (true) {
                    System.out.println("Inserisci il nome del dipendente: ");
                    nome = scanner.nextLine();
                    nome = capitalize(nome);
                    if (nome.length() > 0) {
                        break;
                    } else {
                        System.out.println("Il nome non può essere vuoto");
                    }
                }

                while (true) {
                    System.out.println("Inserisci il cognome del dipendente: ");
                    cognome = scanner.nextLine();
                    cognome = capitalize(cognome);
                    if (cognome.length() > 0) {
                        break;
                    } else {
                        System.out.println("Il cognome non può essere vuoto");
                    }
                }

                while (true) {

                    try {

                        System.out.println("Inserisci la data di nascita del dipendente (gg/mm/aaaa): ");
                        String data = scanner.nextLine();
                        String dataArr[] = data.split("/");

                        int giorno = Integer.parseInt(dataArr[0]);
                        int mese = Integer.parseInt(dataArr[1]);
                        int anno = Integer.parseInt(dataArr[2]);

                        dataDiNascita = new Date(anno, mese, giorno);
                        break;
                    } catch (Exception e) {
                        System.out.println("Data non valida, perfavore inserisci la data nel formato gg/mm/aaaa");
                    }
                }

                while (true) {

                    try {

                        System.out.println("Inserisci la data di assunzione del dipendente (gg/mm/aaaa): ");
                        String data = scanner.nextLine();
                        String dataArr[] = data.split("/");

                        int giorno = Integer.parseInt(dataArr[0]);
                        int mese = Integer.parseInt(dataArr[1]);
                        int anno = Integer.parseInt(dataArr[2]);

                        dataDiAssunzione = new Date(anno, mese, giorno);
                        break;
                    } catch (Exception e) {
                        System.out.println("Data non valida, perfavore inserisci la data nel formato gg/mm/aaaa");
                    }
                }

                //calcolo del numero di matricola
                numeroIscrizione++; //aumento il contatore generale
                numeroMatricola = "CLT_" + numeroIscrizione;

                while (true) {
                    System.out.println("Inserisci il dipartimento del dipendente (MARKETING,RISORSE_UMANE,SVILUPPO): ");
                    String dip = scanner.nextLine().toLowerCase();

                    if (dip.equals("marketing")) {
                        dipartimento = Dipartimento.MARKETING;
                        break;
                    } else if (dip.equals("risorse_umane")) {
                        dipartimento = Dipartimento.RISORSE_UMANE;
                        break;
                    } else if (dip.equals("sviluppo")) {
                        dipartimento = Dipartimento.SVILUPPO;
                        break;
                    } else {
                        System.out.println("Dipartimento non valido, riprova");
                    }
                }

                while (true) {
                    System.out.println("Inserisci il livello del dipendente (da 1 a 8): ");
                    livello = scanner.nextInt();
                    if (livello < 1 || livello > 8) {
                        System.out.println("Livello non valido, riprova");
                    } else {
                        break;
                    }
                }

                //creazione del dipendente
                Dipendente dipendente = new Dipendente(nome, cognome, dataDiNascita, dataDiAssunzione, numeroMatricola, dipartimento, livello);

                //aggiungo il dip appena creato alla lista
                listaDipendenti.add(dipendente);

                System.out.println("Dipendente creato con successo, matricola: " + numeroMatricola);
                System.out.println("---------------------------------------------");
                System.out.println("Vuoi creare un altro dipendente? (s/n)");
                String risposta = scanner.next().toLowerCase();
                if (risposta.equals("n") || risposta.equals("no")) {
                    break;
                } else if (risposta.equals("s") || risposta.equals("si")) {
                    continue;
                } else {
                    System.out.println("Risposta non valida, esco dalla generazione");
                    break;
                }
            }

        } catch (Exception e) {
            System.out.println("Errore generale nella creazione del dipendente, errore: " + e.getMessage());
        }
    }

    public String capitalize(String string) {
        return string.substring(0, 1).toUpperCase() + string.substring(1);
    }

    public boolean checkDipendente(String matricola) {

        for (int i = 0; i < listaDipendenti.size(); i++) {
            if (listaDipendenti.get(i).getNumeroMatricola().equals(matricola)) {
                return true;
            }
        }

        //utente non trovato
        return false;
    }

    public void cambiaInformazioni() {

        try {

            Scanner scanner = new Scanner(System.in);
            String matricola;

            while (true) {
                System.out.println("Inserisci la matricola del dipendente di cui vuoi modificare le informazioni: ");

                matricola = scanner.nextLine().toUpperCase();

                if (!checkDipendente(matricola)) {
                    System.out.println("Dipendente non trovato");

                } else {
                    System.out.println("Dipendente trovato!");
                    break;
                }
            }

            String scelta;
            while (true) {
                System.out.println("Cosa vuoi modificare?");
                System.out.println("1) Nome");
                System.out.println("2) Cognome");
                System.out.println("3) Data di nascita");
                System.out.println("4) Data di assunzione");
                System.out.println("5) Dipartimento");
                System.out.println("6) Livello");
                scelta = scanner.nextLine();
                if (!scelta.equals("1") && !scelta.equals("2") && !scelta.equals("3") && !scelta.equals("4") && !scelta.equals("5") && !scelta.equals("6")) {
                    System.out.println("Scelta non valida, riprova");
                } else {
                    break;
                }
            }

            if (scelta.equals("1")) {
                System.out.println("Inserisci il nuovo nome: ");
                String nome = scanner.nextLine();
                nome = capitalize(nome);

                for (int i = 0; i < listaDipendenti.size(); i++) {
                    if (listaDipendenti.get(i).getNumeroMatricola().equals(matricola)) {
                        listaDipendenti.get(i).setNome(nome);
                        System.out.println("Nome modificato con successo");
                    }
                }
            } else if (scelta.equals("2")) {
                System.out.println("Inserisci il nuovo cognome: ");
                String cognome = scanner.nextLine();
                cognome = capitalize(cognome);

                for (int i = 0; i < listaDipendenti.size(); i++) {
                    if (listaDipendenti.get(i).getNumeroMatricola().equals(matricola)) {
                        listaDipendenti.get(i).setCognome(cognome);
                        System.out.println("Cognome modificato con successo");
                    }
                }
            } else if (scelta.equals("3")) {

                //handling uguale a quello della creazione del dipendente
                while (true) {

                    try {

                        System.out.println("Inserisci la nuova data di nascita del dipendente (gg/mm/aaaa): ");
                        String data = scanner.nextLine();
                        String dataArr[] = data.split("/");

                        int giorno = Integer.parseInt(dataArr[0]);
                        int mese = Integer.parseInt(dataArr[1]);
                        int anno = Integer.parseInt(dataArr[2]);

                        Date dataDiNascita = new Date(anno, mese, giorno);

                        for (int i = 0; i < listaDipendenti.size(); i++) {
                            if (listaDipendenti.get(i).getNumeroMatricola().equals(matricola)) {
                                listaDipendenti.get(i).setDataDiNascita(dataDiNascita);
                                System.out.println("Data di nascita modificata con successo");
                            }
                        }
                        break;
                    } catch (Exception e) {
                        System.out.println("Data non valida, perfavore inserisci la data nel formato gg/mm/aaaa");
                    }
                }
            } else if (scelta.equals("4")) {

                //handling uguale a quello della creazione del dipendente
                while (true) {

                    try {

                        System.out.println("Inserisci la nuova data di assunzione del dipendente (gg/mm/aaaa): ");
                        String data = scanner.nextLine();
                        String dataArr[] = data.split("/");

                        int giorno = Integer.parseInt(dataArr[0]);
                        int mese = Integer.parseInt(dataArr[1]);
                        int anno = Integer.parseInt(dataArr[2]);

                        Date dataDiAssunzione = new Date(anno, mese, giorno);

                        for (int i = 0; i < listaDipendenti.size(); i++) {
                            if (listaDipendenti.get(i).getNumeroMatricola().equals(matricola)) {
                                listaDipendenti.get(i).setDataDiAssunzione(dataDiAssunzione);
                                System.out.println("Data di assunzione modificata con successo");
                            }
                        }
                        break;
                    } catch (Exception e) {
                        System.out.println("Data non valida, perfavore inserisci la data nel formato gg/mm/aaaa");
                    }
                }
            } else if (scelta.equals("5")) {
                while (true) {
                    System.out.println("Inserisci il nuovo dipartimento del dipendente (MARKETING,RISORSE_UMANE,SVILUPPO): ");
                    String dip = scanner.nextLine().toLowerCase();

                    Dipartimento dipartimento = null;
                    if (dip.equals("marketing")) {
                        dipartimento = Dipartimento.MARKETING;
                    } else if (dip.equals("risorse_umane")) {
                        dipartimento = Dipartimento.RISORSE_UMANE;
                    } else if (dip.equals("sviluppo")) {
                        dipartimento = Dipartimento.SVILUPPO;
                    } else {
                        System.out.println("Dipartimento non valido, riprova");
                    }

                    for (int i = 0; i < listaDipendenti.size(); i++) {
                        if (listaDipendenti.get(i).getNumeroMatricola().equals(matricola)) {
                            listaDipendenti.get(i).setDipartimento(dipartimento);
                            System.out.println("Dipartimento modificato con successo");
                        }
                    }
                    break;
                }
            } else if (scelta.equals("6")) {
                while (true) {
                    System.out.println("Inserisci il nuovo livello del dipendente (da 1 a 8): ");
                    int livello = scanner.nextInt();
                    if (livello < 1 || livello > 8) {
                        System.out.println("Livello non valido, riprova");
                    } else {
                        for (int i = 0; i < listaDipendenti.size(); i++) {
                            if (listaDipendenti.get(i).getNumeroMatricola().equals(matricola)) {
                                listaDipendenti.get(i).setLivello(livello);
                                System.out.println("Livello modificato con successo");
                            }
                        }
                        break;
                    }
                }
            }

        } catch (Exception e) {
            System.out.println("Errore generale nella modifica delle informazioni, errore: " + e.getMessage());
        }
    }

    public ArrayList<Dipendente> calcolaRegaliDiCompleanno() {
        Scanner scanner = new Scanner(System.in);
        String mesediNascita;
        String livello;

        System.out.println("Inserisci il mese di nascita dei dipentendi da trovare espresso in numeri (da 1 a 12): ");
        mesediNascita = scanner.nextLine();
        System.out.println("Inserisci il livello dei dipendenti da trovare: ");
        livello = scanner.nextLine();

        ArrayList<Dipendente> dipendentiDaRegalareRegalo = new ArrayList<Dipendente>(0);

        for (int i = 0; i < listaDipendenti.size(); i++) {

            //lo devo incrementtare di uno perche restituisce n-1
            int meseTrovato = listaDipendenti.get(i).getDataDiNascita().getMonth();
            int livelloTrovato = listaDipendenti.get(i).getLivello();

            //converto i dati in stringhe per fare la comprarazone
            String meseTrovatoString = Integer.toString(meseTrovato);
            String livelloTrovatoString = Integer.toString(livelloTrovato);


            //cerco se il dipendente ha i le info uguali a quelle inserire
            if (mesediNascita.equals(meseTrovatoString) && livello.equals(livelloTrovatoString)) {
                dipendentiDaRegalareRegalo.add(listaDipendenti.get(i));
            }
        }

        if (dipendentiDaRegalareRegalo.size() == 0) {
            System.out.println("Nessun dipendente trovato");
        }
        return dipendentiDaRegalareRegalo;
    }

    //questa funzione ritorna una mappa, la chiave è formata dal mese, dall'anno e dal dipartimento, il contenuto di ogni chive è una lista di dipendenti
    public HashMap<String, ArrayList<Dipendente>> calcolaDipendentiDipartimentoMeseAnnoComune() {

        try {

            HashMap<String, ArrayList<Dipendente>> dipendentiInComune = new HashMap<>(); //la inzializzo vuota

            //scorro i dipendenti
            for (int i = 0; i < listaDipendenti.size(); i++) {

                //prendo il mese sotto forma di stringa
                String mese = Integer.toString(listaDipendenti.get(i).getDataDiNascita().getMonth());

                //anno
                String anno = Integer.toString(listaDipendenti.get(i).getDataDiNascita().getYear());

                //dipartimento
                String dipartimento = listaDipendenti.get(i).getDipartimento().toString(); //lo devo conerrtire in stringa perche e un enum

                //creo la chiave
                String chiave = mese + anno + dipartimento;

                //controllo se la chiae esiste gia
                if (dipendentiInComune.get(chiave) == null) {

                    //se non esiste la creo
                    ArrayList<Dipendente> dipendenti = new ArrayList<Dipendente>(0);
                    dipendenti.add(listaDipendenti.get(i));
                    dipendentiInComune.put(chiave, dipendenti);
                } else {
                    //se esiste aggiungo il dipendente
                    dipendentiInComune.get(chiave).add(listaDipendenti.get(i));
                }
            }

            //IMPORTANTE adesso vado a togliere gli elementi in cui la lista è solamente formata da 1 dipendente perche
            // e stato chiesto 2 dipendentio o piu
            for (String key : dipendentiInComune.keySet()) {
                if (dipendentiInComune.get(key).size() == 1) {
                    dipendentiInComune.remove(key);
                }
            }

            return dipendentiInComune;

        } catch (Exception e) {
            System.out.println("Errore generale nel calcolo dei regali di natale, errore: " + e.getMessage());
            return null;
        }

    }
}
