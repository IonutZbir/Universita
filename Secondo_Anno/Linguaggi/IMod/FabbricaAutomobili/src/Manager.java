import java.util.ArrayList;

public class Manager {
    private ArrayList<Prodotto> prodotti = new ArrayList<>();

    public void addProdotto(int id, String label, double productionCost, double clientCost, double assemblyCost,
            ArrayList<Componente> componenti) {

        Prodotto p = new Prodotto(id, label, productionCost, clientCost, assemblyCost, componenti);
        prodotti.add(p);

    }

}
