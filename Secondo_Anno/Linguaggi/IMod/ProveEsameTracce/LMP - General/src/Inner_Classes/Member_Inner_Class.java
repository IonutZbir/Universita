package Inner_Classes;

/**
 * 1) Member inner class
 *  Una classe interna di membro è una classe definita all'interno di un'altra classe (classe esterna)
 *  e ha accesso ai membri della classe esterna, compresi quelli privati. Può essere istanziata solo attraverso
 *  un'istanza della classe esterna.
 */

public class Member_Inner_Class {

    public int numberOfParentClass = 5;

    class InnerClass{
        public int numberOfInnerClass = 10;
        public void getNumber(){
            System.out.println("Number of parent class: " + numberOfParentClass);
            System.out.println("Number of inner class: " + numberOfInnerClass);
        }
    }
}
