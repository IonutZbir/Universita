package it.uniroma2.info.lmp;

public class ProfessoreImpl extends PersonImpl implements Professore {

	public ProfessoreImpl(String nome, String cognome, String cattedra) {
		super(nome, cognome);
		this.cattedra = cattedra;
	}

	private String cattedra;
		
	@Override
	public String getCattedra() {
		return cattedra;
	}

}
