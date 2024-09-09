import java.time.LocalDate;
import java.time.Month;

import models.TipologiaSportivo;
import services.GestioneSportivi;

public class Main {
    public static void main(String[] args) {
        GestioneSportivi gs = new GestioneSportivi();

        gs.addSportivo("Ionut","Zbirciog", LocalDate.of(2023, 6, 24), TipologiaSportivo.GIOCATORE, 4);
        
        gs.addSportivo("Adriano","Porzia", LocalDate.of(2022, 7, 14), TipologiaSportivo.GIOCATORE, 4);
        
        gs.addSportivo("Giacomo","Pace", LocalDate.of(2024, 9, 12), TipologiaSportivo.PREPARATORE_ATTLETICO, 2);
        
        gs.getSportivo("TEAM_1").addReti(Month.APRIL, 12);
        gs.getSportivo("TEAM_1").addReti(Month.MARCH, 9);
        gs.getSportivo("TEAM_1").addReti(Month.JULY, 14);
        gs.getSportivo("TEAM_2").addReti(Month.SEPTEMBER, 10);
        gs.getSportivo("TEAM_3").addReti(Month.OCTOBER, 2);

        gs.setNumeroRetiPreviste(10);

        System.out.println(gs.spotiviPremiati());

    }
}
