package Inner_Classes;

/**
 * 2) Anonymous inner class
 * Una classe interna anonima è una classe senza nome definita al volo durante la creazione di un'istanza
 * di un'interfaccia o di una classe astratta. Solitamente viene utilizzata quando è necessario implementare
 * un'interfaccia o una classe astratta senza dover dichiarare una classe separata.
 *
 * In questo esempio viene implementata l'interfaccia Salutare.
 * Viene creata una classe anonima che utilizza l'interfaccia Salutare e specifica il comportamento del metodo saluta()
 * NOTA che la differenza sta che il comportamento del metodo saluta viene specificato senza dover creare una classe
 * ed implementare l'interfaccia (implements...), viene quindi creato un oggetto di tipo Salutare e viene specificato
 * il comportamento del metodo saluta() all'interno delle parentesi graffe.
 */

interface Salutare{
    public void saluta();
}

public class Anonymous_Inner_Class {

    public static void main(String args []){
        Salutare s = new Salutare(){
            public void saluta(){
                System.out.println("Ciao!");
            }
        };
        s.saluta();
    }
}
