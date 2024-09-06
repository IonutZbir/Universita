import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Factory {

    public Object readCard(String cardPath){

        try{

            Scanner scanner = new Scanner(new File(cardPath));

            int counter = 0;
            while(scanner.hasNextLine()){
                if(counter == 0){

                    String line = scanner.nextLine().toLowerCase().trim();
                    if(!line.split(":")[0].equals("filetype")){
                        System.out.println("Errore: il primo attributo deve essere 'filetype', formato non valido");
                        return null;
                    }else{
                        String fileType = line.split(":")[1];
                        if(fileType.equals("negozio")){
                            Negozio negozio = new Negozio(cardPath);
                            return negozio;
                        }else if(fileType.equals("ristorante")){
                            Ristorante ristorante = new Ristorante(cardPath);
                            return ristorante;
                        }else if(fileType.equals("associazione")){
                            Associazione associazione = new Associazione(cardPath);
                            return associazione;
                        }else{
                            System.out.println("Errore: fileType non riconosciuto");
                            return null;
                        }
                    }
                }
            }

        }catch(FileNotFoundException e){
            System.out.println("Errore: file non trovato");
            return null;
        }catch(Exception e) {
            System.out.println("Errore generale: " + e.getMessage());
            e.printStackTrace();
            return null;
        }
        return null;
    }
}
