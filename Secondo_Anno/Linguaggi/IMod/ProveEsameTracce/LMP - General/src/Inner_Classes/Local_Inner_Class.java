package Inner_Classes;

/**
 * 3) Local inner class
 * Una classe interna locale è una classe definita all'interno di un blocco di codice, come un metodo.
 * Ha accesso ai membri della classe esterna e ai finali o effettivamente finali della classe locale in cui è dichiarata.
 */

public class Local_Inner_Class {

    public void stampaNumero(){

        //creo una classe che genera un numero random
        class GeneraNumero{
            public int getNumber(){
                return (int) (Math.random() * 100);
            }
        }

        //creo un oggetto della classe GeneraNumero
        GeneraNumero generator = new GeneraNumero();
        System.out.println(generator.getNumber());
    }
}
