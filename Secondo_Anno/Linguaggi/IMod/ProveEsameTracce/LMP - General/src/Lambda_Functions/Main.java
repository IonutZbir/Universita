package Lambda_Functions;

import java.util.ArrayList;
import java.util.List;

/**
 * Lezione sulle Lambda Functions
 *
 * SINTASSI:
 * parameter -> expression
 * (parameter1, parameter2) -> expression
 * (parameter1, parameter2) -> { code block }
 *
 * A:
 * funzione lambda che non prende nessun parametro in ingresso
 *
 * B:
 * funzione lambda che prende un aram in ingresso e lo restituisce per printare una stringa
 *
 * C:
 * funzione lambda che prende due parametri in ingresso e li restituisce per printare due stringhe
 *
 * D:
 * funzione lambda che prende due parametri in ingresso e li restituisce per printare la somma, il prodotto e la differenza
 */

public class Main {

    public interface A{
        void print();
    }

    public interface B{
        void print(String x);
    }

    public interface C{
        void print(String x, String y);
    }

    public interface D{
        void print(int x, int y);
    }

    public static void main(String args[]){

        A obj = () -> System.out.println("Funzione lambda di tipo A");
        obj.print();

        B obj2 = (x) -> System.out.println("Funzione lambda di tipo B, la stringa passata è: " + x);
        obj2.print("Ciao sono Luca");

        C obj3 = (x, y) -> System.out.println("Funzione lambda di tipo C, le stringhe passate sono: " + x + " e " + y);
        obj3.print("Ciao sono Luca", " e sono all'università");

        D obj4 = (x, y) -> {
        	System.out.println("Funzione lambda di tipo D, la somma dei due numeri passati è: " + (x+y));
            System.out.println("Il prodotto dei due numeri passati è: " + (x*y));
            System.out.println("La differenza dei due numeri passati è: " + (x-y));
        };
        obj4.print(10, 5);
        

    }



}
