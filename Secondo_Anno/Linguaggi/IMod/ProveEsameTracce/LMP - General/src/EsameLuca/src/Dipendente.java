import java.util.Date;
import java.util.Scanner;

public class Dipendente {

    private String nome;
    private String cognome;
    private Date dataDiNascita;
    private Date dataDiAssunzione;
    private String numeroMatricola;
    private Dipartimento dipartimento;
    private int livello;

    public Dipendente(String nome, String cognome, Date dataDiNascita, Date dataDiAssunzione, String numeroMatricola, Dipartimento dipartimento, int livello) {
        this.nome = nome;
        this.cognome = cognome;
        this.dataDiNascita = dataDiNascita;
        this.dataDiAssunzione = dataDiAssunzione;
        this.numeroMatricola = numeroMatricola;
        this.dipartimento = dipartimento;
        this.livello = livello;
    }

    public String getNumeroMatricola() {
        return numeroMatricola;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCognome() {
        return cognome;
    }

    public void setCognome(String cognome) {
        this.cognome = cognome;
    }

    public Date getDataDiNascita() {
        return dataDiNascita;
    }

    public void setDataDiNascita(Date dataDiNascita) {
        this.dataDiNascita = dataDiNascita;
    }

    public Date getDataDiAssunzione() {
        return dataDiAssunzione;
    }

    public void setDataDiAssunzione(Date dataDiAssunzione) {
        this.dataDiAssunzione = dataDiAssunzione;
    }

    public void setNumeroMatricola(String numeroMatricola) {
        this.numeroMatricola = numeroMatricola;
    }

    public Dipartimento getDipartimento() {
        return dipartimento;
    }

    public void setDipartimento(Dipartimento dipartimento) {
        this.dipartimento = dipartimento;
    }

    public int getLivello() {
        return livello;
    }

    public void setLivello(int livello) {
        this.livello = livello;
    }
}
