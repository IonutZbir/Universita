import java.awt.*;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {

        Menu menu = new Menu();

        List<Ingrediente> ingredientiAntipasto = new ArrayList<>();
        ingredientiAntipasto.add(new Ingrediente("Salame", 0.5, true, 1));
        ingredientiAntipasto.add(new Ingrediente("Formaggio", 1.5, true, 2));
        ingredientiAntipasto.add(new Ingrediente("Olive", 0.5, true, 5));
        Pietanza tagliere = new Pietanza("Tagliere misto", ingredientiAntipasto, 5, Portate.ANTIPASTI);

        List<Ingrediente> ingredientiFocaccia = new ArrayList<>();
        ingredientiFocaccia.add(new Ingrediente("Farina", 0.5, false, 100));
        ingredientiFocaccia.add(new Ingrediente("Acqua", 1.5, false, 100));
        ingredientiFocaccia.add(new Ingrediente("Olio", 0.5, false, 100));
        Pietanza focaccia = new Pietanza("Focaccia", ingredientiFocaccia, 10, Portate.ANTIPASTI);

        List<Ingrediente> ingredientiPizza = new ArrayList<>();
        ingredientiPizza.add(new Ingrediente("Pomodoro", 0.5, true, 100));
        ingredientiPizza.add(new Ingrediente("Mozzarella", 1.5, true, 100));
        ingredientiPizza.add(new Ingrediente("Basilico", 0.5, false, 100));
        ingredientiPizza.add(new Ingrediente("Olio", 0.5, false, 100));
        Pietanza pizza = new Pietanza("Margherita", ingredientiPizza, 10, Portate.PRIMI);

        List<Ingrediente> ingredientiPasta = new ArrayList<>();
        ingredientiPasta.add(new Ingrediente("Pasta", 0.5, true, 100));
        ingredientiPasta.add(new Ingrediente("Pomodoro", 1.5, true, 100));
        ingredientiPasta.add(new Ingrediente("Basilico", 0.5, false, 100));
        ingredientiPasta.add(new Ingrediente("Olio", 0.5, false, 100));
        Pietanza pasta = new Pietanza("Pasta al pomodoro", ingredientiPasta, 10, Portate.PRIMI);

        List<Ingrediente> ingredientiCarne = new ArrayList<>();
        ingredientiCarne.add(new Ingrediente("Carne", 2.5, true, 1));
        ingredientiCarne.add(new Ingrediente("Patate", 1.5, true, 10));
        ingredientiCarne.add(new Ingrediente("Olio", 0.5, false, 1));
        Pietanza carne = new Pietanza("Secondo", ingredientiCarne, 15, Portate.SECONDI);

        List<Ingrediente> ingredientiPesce = new ArrayList<>();
        ingredientiPesce.add(new Ingrediente("Pesce", 2.5, true, 1));
        ingredientiPesce.add(new Ingrediente("Patate", 1.5, true, 10));
        ingredientiPesce.add(new Ingrediente("Olio", 0.5, false, 1));
        Pietanza pesce = new Pietanza("Pesce", ingredientiPesce, 15, Portate.SECONDI);



        menu.addPietanza(tagliere);
        menu.addPietanza(focaccia);
        menu.addPietanza(pizza);
        menu.addPietanza(pasta);
        menu.addPietanza(carne);
        menu.addPietanza(pesce);

        //menu.addPietanzaManualmente();

        menu.getRanking();

    }
}
