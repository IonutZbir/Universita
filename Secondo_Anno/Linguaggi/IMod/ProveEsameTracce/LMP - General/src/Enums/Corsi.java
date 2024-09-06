package Enums;

//Corsi universitari
public enum Corsi {

    INFORMATICA("CS"),
    MATEMATICA("MT"),
    FISICA("PH"),
    INGEGNERIA("EN");

    private final String codice;

    Corsi(String codice){
        this.codice = codice;
    }

    public String getDescrizione(){
        return codice;
    }


}
