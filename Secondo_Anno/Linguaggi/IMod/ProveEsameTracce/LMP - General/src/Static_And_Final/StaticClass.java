package Static_And_Final;

/**
 * Classe STATIC
 * Le variabili con il modificatore STATIC sono condivise uniche in memoria e quindi condivise tra le istanze
 * Modificando il valore di una variabile static in una istanza, il valore cambierà per tutte le istanze
 */

public class StaticClass {

    public static int x = 10;
    public int y = 5;

    public void getNumber(){
        System.out.println("x: " + x);
        System.out.println("y: " + y);
    }
}
