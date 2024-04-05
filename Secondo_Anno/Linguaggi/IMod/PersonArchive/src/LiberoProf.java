import java.util.Date;

public class LiberoProf extends Person{

    private String professione;
    private String iva;

    public LiberoProf(String nome, String cognome, String codiceFiscale, Date dataDiNascita, String professione, String iva) {
        super(nome, cognome, codiceFiscale, dataDiNascita);
        this.iva = iva;
        this.professione = professione;
    }

    public String getProfessione() {
        return professione;
    }

    public void setProfessione(String professione) {
        this.professione = professione;
    }

    public String getIva() {
        return iva;
    }

    public void setIva(String iva) {
        this.iva = iva;
    }
}
