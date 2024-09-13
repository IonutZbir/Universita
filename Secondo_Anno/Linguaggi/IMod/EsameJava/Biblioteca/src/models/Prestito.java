package models;

import java.time.LocalDate;

public class Prestito {
    private LocalDate dataInizio;
    private LocalDate dataPrevistaConsegna;
    private LocalDate dataConsegna;
    String nome;
    String cognome;
    private double costoAffitto;
    private static final double PENA = 10; 
    public Prestito(LocalDate dataInizio, LocalDate dataPrevistaConsegna, LocalDate dataConsegna, String nome,
            String cognome, double costoAffitto) {
        setDate(dataInizio, dataPrevistaConsegna, dataConsegna);
        this.costoAffitto = costoAffitto;
        this.nome = nome;
        this.cognome = cognome;
        checkConsegna();
    }

    private void checkConsegna(){
        if(dataConsegna != null && dataPrevistaConsegna != null && dataConsegna.isAfter(dataPrevistaConsegna) ){
            this.costoAffitto += PENA;
            System.out.println("Hai consegnato in ritardo.\nNuovo costo: " + this.costoAffitto);
        }
    }

    public void setDate(LocalDate dataInizio, LocalDate dataPrevistaConsegna, LocalDate dataConsegna) {
        if(dataInizio.isAfter(dataConsegna) || dataInizio.isAfter(dataPrevistaConsegna)){
            System.out.println("La data di inizio è invalida: " + dataInizio);
            return;
        }
        this.dataInizio = dataInizio;
        this.dataPrevistaConsegna = dataPrevistaConsegna;
        this.dataConsegna = dataConsegna;
    }

    public void setDataPrevistaConsegna(int giorni) {
        if(this.dataPrevistaConsegna == null){
            System.out.println("Non è stato possibile modificare la data prevista di consegna per il seguente prestito:\n " + toString() + "\n");
            return;
        }
        this.dataPrevistaConsegna = this.dataPrevistaConsegna.plusDays(giorni);
    }
    
    public void setNome(String nome) {
        this.nome = nome;
    }
    public void setCognome(String cognome) {
        this.cognome = cognome;
    }
    public void setCostoAffitto(double costoAffitto) {
        this.costoAffitto = costoAffitto;
    }
    public LocalDate getDataInizio() {
        return dataInizio;
    }
    public LocalDate getDataPrevistaConsegna() {
        return dataPrevistaConsegna;
    }
    public LocalDate getDataConsegna() {
        return dataConsegna;
    }
    public String getNome() {
        return nome;
    }
    public String getCognome() {
        return cognome;
    }
    public double getCostoAffitto() {
        return costoAffitto;
    }
    @Override
    public String toString() {
        return "Prestito [dataInizio=" + dataInizio + ", dataPrevistaConsegna=" + dataPrevistaConsegna
                + ", dataConsegna=" + dataConsegna + ", nome=" + nome + ", cognome=" + cognome + ", costoAffitto="
                + costoAffitto + "]";
    }
}