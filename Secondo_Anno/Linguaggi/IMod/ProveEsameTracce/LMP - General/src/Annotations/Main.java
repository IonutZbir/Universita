package Annotations;
import Enums.Stadi;

public class Main {

    public static void main(String[] args) {

        //stampo gli stadi
        for (Stadi stadio : Stadi.values()) {
            stadio.getStadio();
        }
    }
}
