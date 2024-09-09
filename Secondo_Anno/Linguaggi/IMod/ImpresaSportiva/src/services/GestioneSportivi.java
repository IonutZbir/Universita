package services;

import java.time.LocalDate;
import java.util.HashMap;
import java.util.NoSuchElementException;

import models.Sportivo;
import models.TipologiaSportivo;

public class GestioneSportivi {
    private static HashMap<String, Sportivo> archivioSportivi = new HashMap<>();
    private int numeroRetiPreviste;

    public void addSportivo(String nome, String cognome, LocalDate dataAssunzione,
            TipologiaSportivo tipologia, int livello){
        
        Sportivo s = new Sportivo(nome, cognome, dataAssunzione, tipologia, livello);
        archivioSportivi.put(s.getNrIscrizione(), s);
    }

    public Sportivo getSportivo(String nrIscrizione) {
        Sportivo s = archivioSportivi.getOrDefault(nrIscrizione, null);
        if (s == null) {
            throw new NoSuchElementException("Lo sportivo non esiste");
        }
        return s;
    }

    public HashMap<Integer, Sportivo> spotiviPremiati() {
        HashMap<Integer, Sportivo> premiati = new HashMap<>();
        int counter;
        for (Sportivo sp : archivioSportivi.values()) {
            if (sp.getLivello() >= 3) {
                counter = 0;
                for (int value : sp.getReti().values()) {
                    if (value >= numeroRetiPreviste) {
                        counter++;
                    }
                }
                if (counter > 0) {
                    premiati.put(counter, sp);
                }
            }
        }
        return premiati;
    }

    public void setNumeroRetiPreviste(int numeroRetiPreviste) {
        if (numeroRetiPreviste < 0) {
            throw new IllegalArgumentException("Il numero di reti non può essere negativo");
        }
        this.numeroRetiPreviste = numeroRetiPreviste;
    }

    public int getNumeroRetiPreviste() {
        return numeroRetiPreviste;
    }

}
