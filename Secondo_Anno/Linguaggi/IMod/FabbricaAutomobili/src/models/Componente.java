package models;

import java.util.ArrayList;

public class Componente extends Prodotto{
    private String nome;
    private String paese;
    private int tempoOrdinazione; // giorni
    private double costoProduzione; 

    public Componente(String identificativo, String etichetta, double costoProduzione, double prezzoAcquisto,
            ArrayList<Componente> componenti, String nome, String paese, int tempoOrdinazione) {
        super(identificativo, etichetta, costoProduzione, prezzoAcquisto, componenti);
        this.nome = nome;
        this.paese = paese;
        this.tempoOrdinazione = tempoOrdinazione;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getPaese() {
        return paese;
    }

    public void setPaese(String paese) {
        this.paese = paese;
    }

    public int getTempoOrdinazione() {
        return tempoOrdinazione;
    }

    public void setTempoOrdinazione(int tempoOrdinazione) {
        this.tempoOrdinazione = tempoOrdinazione;
    }

    public double getCostoProduzione() {
        return costoProduzione;
    }

    public void setCostoProduzione(double costoProduzione) {
        this.costoProduzione = costoProduzione;
    }
   
    

    
}
