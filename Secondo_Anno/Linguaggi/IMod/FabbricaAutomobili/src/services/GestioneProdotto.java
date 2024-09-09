package services;

import models.Componente;
import models.Prodotto;

public class GestioneProdotto {
    public double getCostoProdottoComplessivo(Prodotto p){
        return getCostoComplessivo(p) + getCostoComplessivoProduzione(p) + 
    }
    
    private double getCostoComplessivo(Prodotto p){
        double totPrezzo = 0;
        for (Componente comp : p.getComponenti()) {
            totPrezzo += comp.getCostoProduzione();
        }

        return totPrezzo;
    }

    private double getCostoComplessivoProduzione(Prodotto p){
        return getCostoComplessivo(p) * p.getCostoDiProduzione();
    }
}
