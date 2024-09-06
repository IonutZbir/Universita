package Enums;

/**
 * Lezione sugli ENUMS
 *
 */

public class Main {
    public static void main(String[] args) {

        System.out.println("Il pomodoro è di colore: " + colors.ROSSO);
        System.out.println("Il limone è di colore: " + colors.GIALLO);
        System.out.println("Il cielo è di colore: " + colors.BLU);

        System.out.println("----------------------------------");

        System.out.println("Informatica ha il codice corso: " + Corsi.INFORMATICA.getDescrizione());
        System.out.println("Matematica ha il codice corso: " + Corsi.MATEMATICA.getDescrizione());
        System.out.println("Fisica ha il codice corso: " + Corsi.FISICA.getDescrizione());


    }
}
