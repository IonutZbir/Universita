package Error_Handling;

/**
 * Lezione Try Catch (error handling)
 * Try prova ad eseguire un operazione
 * Catch cattura l'errore e lo gestisce (si possono specificare i tipi di errori da catturare)
 * Finally viene eseguito sempre, sia che ci sia stato un errore o meno
 */

public class Main {

    public static void main(String[] args) {

        int array[] = {1, 2, 3, 4, 5};

        try {
            System.out.println(array[10]);

        } catch(IndexOutOfBoundsException e) {
            System.out.println("E' stato catturato un errore IndexOutOfBoundsException: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("E' stato catturato un errore generale: " + e.getMessage());
        } finally {
            System.out.println("Blocco finale");
        }
    }
}
