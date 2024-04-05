import java.util.Date;

public class Dipendente {
    private String nome;
    private String cognome;
    private Data dataAssunzione;
    private static nMatricola;
    private String matricola;

    private String dipartimento;
    private String mansione;

    private int livello;
    private int capo;

    public Dipendente(String nome, String cognome, String dataAssunzione) {
    	this.nome = nome;
        this.cognome = cognome;
        SimpleDateFormatter sdf = new SimpleDateFormatter("dd/MM/yyyy");
        Date dataAssunzioneFormatted = new Date();
        try {
        	dataAssunzioneFormatted = sdf.parse(dataAssunzione);
        } catch (ParseException e) {
        	System.out.println("ERROR: Format errato");
        }
        this.dataAssunzione = dataAssunzioneFormatted;
    }

}
