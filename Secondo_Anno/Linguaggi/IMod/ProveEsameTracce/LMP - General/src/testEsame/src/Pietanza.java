import java.util.List;

public class Pietanza {

    public String nome;
    public double prezzo;
    List<Ingrediente> ingredienti;

    public int tempoPreparazione;

    public Portate portata;

    public Pietanza(String nome, List<Ingrediente> ingredienti,int tempoPreparazione, Portate portata) {
        this.nome = nome;
        this.ingredienti = ingredienti;
        this.tempoPreparazione = tempoPreparazione;
        this.portata = portata;
        this.prezzo = calcolaPrezzoPubblico();
    }

    public double getCostoIngredienti(){

        if(ingredienti.size() == 0){
            return 0;
        }

        double costo = 0;
        for (Ingrediente ingrediente : ingredienti) {
            costo += (ingrediente.costoEttogrammo * ingrediente.quantita);
        }
        return costo;
    }

    public double getCostoPreparazione(){
        return Costi.MANODOPERA.costo * tempoPreparazione;
    }

    public double calcolaPrezzoPubblico(){
        return getCostoIngredienti() + getCostoPreparazione() + Costi.PROFITTO.costo;
    }

    public void pietanzaToString(){

        System.out.println("-----------------------Pietanza-----------------------");
        System.out.println("Nome: " + nome);
        System.out.println("Prezzo: " + prezzo);
        System.out.println("Tempo di preparazione: " + tempoPreparazione);
        System.out.println("Portata: " + portata);
        System.out.println("Ingredienti: ");
        for(int i = 0; i < ingredienti.size(); i++){
            if(ingredienti.get(i).pubblico){
                System.out.println(ingredienti.get(i).nome + " " + ingredienti.get(i).quantita + "g");
            }
        }

        System.out.println("Ingredienti nascosti: ");
        //Ingredienti nascosti
        for(int i = 0; i < ingredienti.size(); i++){
            if(!ingredienti.get(i).pubblico){
                System.out.println(ingredienti.get(i).nome + " " + ingredienti.get(i).quantita + "g");
            }
        }
        System.out.println("----------------------------------------------------");
    }

}
