import java.util.*;

public class Prodotto {
    /*
     * Ogni componente per l’auto (da ora in poi prodotto) è descritto tramite un
     * identificativo, un’etichetta di
     * riferimento, un costo di produzione, un prezzo agli acquirenti e la lista dei
     * suoi componenti (intesi come
     * subcomponenti del componente per l’auto, ossia del prodotto) e da dove questi
     * provengono.
     */

    private int id;
    private String label;
    private double productionCost;
    private double clientCost;
    private double assemblyCost;
    private double profit;
    public ArrayList<Componente> componenti;

    public Prodotto(int id, String label, double productionCost, double clientCost, double assemblyCost,
            ArrayList<Componente> componenti) {
        this.id = id;
        this.label = label;
        this.productionCost = productionCost;
        this.clientCost = clientCost;
        this.assemblyCost = assemblyCost;
        this.componenti = componenti;
    }

    public double getAssemblyCost() {
        return assemblyCost;
    }

    public void setAssemblyCost(double assemblyCost) {
        this.assemblyCost = assemblyCost;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public double getProductionCost() {
        return productionCost;
    }

    public void setProductionCost(double productionCost) {
        this.productionCost = productionCost;
    }

    public double getClientCost() {
        return clientCost;
    }

    public void setClientCost(double clientCost) {
        this.clientCost = clientCost;
    }

    public int numOfComponents() {
        return componenti.size();
    }

    public double getProfit() {
        return profit;
    }

    public void setProfit(double profit) {
        this.profit = profit;
    }

    public int estimateOrdTime() {
        int max = 0;
        for (Componente c : this.componenti) {
            max = Math.max(c.getOrdTime(), max);
        }
        return max;
    }

    public double totalBuildTime(double dayCostFactory) {
        return this.assemblyCost * dayCostFactory;
    }

    public double totalCost() {
        double sum = 0;
        for (Componente c : this.componenti) {
            sum += c.getCost();
        }
        return sum;
    }

    public double totalProductionCost() {
        return this.totalCost() + this.productionCost;
    }

}
