package models;

public class Negozio {
    private String partitaIva;
    private String sede;
    private String merceVenduta;
    private int inAttivitaDal;

    public Negozio(String partitaIva, String sede, String merceVenduta, int inAttivitaDal) {
        this.partitaIva = partitaIva;
        this.sede = sede;
        this.merceVenduta = merceVenduta;
        this.inAttivitaDal = inAttivitaDal;
    }
}
