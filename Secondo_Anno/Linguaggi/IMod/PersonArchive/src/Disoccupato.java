import java.util.Date;

public class Disoccupato extends Person{

    private String registroDis;

    public Disoccupato(String nome, String cognome, String codiceFiscale, Date dataDiNascita, String registroDis) {
        super(nome, cognome, codiceFiscale, dataDiNascita);
        this.registroDis = registroDis;
    }

    public String getRegistroDis() {
        return registroDis;
    }

    public void setRegistroDis(String registroDis) {
        this.registroDis = registroDis;
    }

    @Override
    public String toString() {
        return "Disoccupato{" +
                "registroDis='" + registroDis + '\'' +
                '}';
    }
}

