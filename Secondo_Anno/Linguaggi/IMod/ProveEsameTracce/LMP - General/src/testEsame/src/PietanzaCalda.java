import java.util.List;

public class PietanzaCalda extends Pietanza{

    public int tempoCottura;

    public PietanzaCalda(String nome, List<Ingrediente> ingredienti, int tempoPreparazione, Portate portata, int tempoCottura) {
        super(nome, ingredienti, tempoPreparazione, portata);
        this.tempoCottura = tempoCottura;
    }

    public double getCostoCostoCottura(){
        return Costi.GAS.costo * tempoCottura;
    }

}
