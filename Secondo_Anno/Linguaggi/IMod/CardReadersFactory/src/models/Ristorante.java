package models;

public class Ristorante {
    private String partitaIva;
    private String sede;
    private Categoria categoria;
    private int inAttivitàDal;

    public Ristorante(String partitaIva, String sede, Categoria categoria, int inAttivitàDal) {
        this.partitaIva = partitaIva;
        this.sede = sede;
        this.categoria = categoria;
        this.inAttivitàDal = inAttivitàDal;
    }
}
