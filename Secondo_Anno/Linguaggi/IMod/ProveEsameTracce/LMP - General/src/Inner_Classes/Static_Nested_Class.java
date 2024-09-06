package Inner_Classes;

/**
 * 4) Static nested class
 * Una classe annidata statica è una classe definita all'interno di un'altra classe come membro statico.
 * Non può accedere ai membri NON statici della classe esterna,
 * ma può essere istanziata senza creare un'istanza della classe esterna.
 *
 * Nell'esempio la sottoclasse statica non può accedere alla variabile y della classe esterna
 *
 */
public class Static_Nested_Class {

    public static int x = 10;
    public int y = 5;

    public static class childClass{

        public void getNumber(){
            System.out.println("x: " + x);

            //ERRORE PERCHE' NON PUO' ACCEDERE A VARIABILI NON STATICHE
            //System.out.println("y: " + y);
        }
    }
}

class Main{
    public static void main(String args []){

        //Utilizzo la sottoclasse istanziando la classe esterna
        Static_Nested_Class.childClass sottoClasse = new Static_Nested_Class.childClass();
        sottoClasse.getNumber();
    }
}
