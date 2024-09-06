package models;

public class Associazione {
    private String sede;
    private Scopo scopo;
    private int inAttivitaDal;

    public Associazione(String sede, Scopo scopo, int inAttivitaDal) {
        this.sede = sede;
        this.scopo = scopo;
        this.inAttivitaDal = inAttivitaDal;
    }
}
