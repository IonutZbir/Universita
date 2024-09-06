package Enums;

public enum Stadi {

    sansiro("Inter", "80.000"),
    olimpico("Lazio", "70.000"),
    marassi("Sampdoria", "40.000"),
    maradona("Napoli", "60.000");


   private final String squadra;
    private final String capienza;

    Stadi(String squadra, String capienza){
        this.squadra = squadra;
        this.capienza = capienza;
    }

    public void getStadio(){
        System.out.println("Stadio: " + this.squadra + " con capienza: " + this.capienza);
    }

}
