package Static_And_Final;

/**
 * Lezione su STATIC e FINAL
 */

public class Main {

    public static void main(String args []){

        //Valori iniziali della classe x:10 e y:5

        StaticClass t1 = new StaticClass();
        t1.x = 20; //modifico il valore di x (variabile static)
        t1.y = 10; //modifico il valore di y

        System.out.println("t1");
        t1.getNumber();

        StaticClass t2 = new StaticClass();
        t2.y = 30; //modifico il valore di t

        System.out.println("\nt2");
        t2.getNumber();

        //Il valore della variabile static x è condiviso tra tutte le istanze quindi sarà lo stesso per t1 e t2
        //Il valore della variabile y è diverso per ogni istanza quindi sarà diverso per t1 e t2



    }
}
