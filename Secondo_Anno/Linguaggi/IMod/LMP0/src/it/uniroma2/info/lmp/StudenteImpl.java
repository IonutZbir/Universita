package it.uniroma2.info.lmp;

public class StudenteImpl extends PersonImpl implements Studente{

	private String matricola;
	
	public StudenteImpl(String nome, String cognome, String matricola) {
		super(nome, cognome);
		this.matricola = matricola;
	}
	
	@Override
	public String getMatricola() {
		return matricola;
	}
	
	public String toString() {
		return super.toString() + " " + matricola;
	}
	
}
