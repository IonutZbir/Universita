package models;

import java.sql.Time;
import java.util.ArrayList;

public class Prodotto {
    private String identificativo;
    private String etichetta;
    private double costoProduzione;
    private double prezzoAcquisto;
    private ArrayList<Componente> componenti;
    private static double costoGiornaliero;

    public Prodotto(String identificativo, String etichetta, double costoProduzione, double prezzoAcquisto,
            ArrayList<Componente> componenti) {
        this.identificativo = identificativo;
        this.etichetta = etichetta;
        this.costoProduzione = costoProduzione;
        this.prezzoAcquisto = prezzoAcquisto;
        this.componenti = componenti;
    }

    public int getNumeroComponenti(){
        return componenti.size();
    }

    public int getStimaOrdinazione(){
        int maxTime = 0;
        for (Componente comp : componenti) {
            maxTime = Math.max(maxTime, comp.getTempoOrdinazione());
        }
        return maxTime;
    }

    public int getTempoTotAssemblaggio(){
        int totTime = 0;

        for (Componente comp : componenti) {
            totTime += comp.getTempoOrdinazione();
        }

        return totTime;
    }

    public double getCostoDiProduzione(){
        return getTempoTotAssemblaggio() * costoGiornaliero;
    }

    public void setCostoGiornaliero(double costo){
        this.costoGiornaliero = costo;
    }

    public ArrayList<Componente> getComponenti() {
        return componenti;
    }

    public void setComponenti(ArrayList<Componente> componenti) {
        this.componenti = componenti;
    } 
}
