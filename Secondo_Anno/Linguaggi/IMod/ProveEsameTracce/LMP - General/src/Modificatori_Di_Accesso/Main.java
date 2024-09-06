package Modificatori_Di_Accesso;
import java.util.*;

/**
 * Lezione sui modificatori di accesso PUBLIC, PROTECTED, PRIVATE
 *
 * | PUBLIC |
 * Class YES
 * Package YES
 * Subclass YES
 * World YES
 *
 *
 * | PROTECTED |
 * Class YES
 * Package YES
 * Subclass YES
 * World NO
 *
 *
 * | NO MODIFIER |
 * Class YES
 * Package YES
 * Subclass NO
 * World NO
 *
 *
 * | PRIVATE | *
 * Class YES
 * Package NO
 * Subclass NO
 * World NO
 */

public class Main {

    public static void main(String[] args) {

        //Istanzio le classi
        PublicClass pub = new PublicClass();
        ProtectedClass prot = new ProtectedClass();
        PrivateClass priv = new PrivateClass();

        //PUBLIC OUTPUT: 5
        System.out.println(pub.number);

        //PROTECTED OUTPUT: 3
        System.out.println(prot.number);

        //PRIVATE OUTPUT: ERROR
        //System.out.println(priv.number());

        //PRIVATE OUTPUT: 2
        System.out.println(priv.getNumber());

    }

}
