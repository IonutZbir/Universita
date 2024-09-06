import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Azienda azienda = new Azienda();
        azienda.addDipendente();
        azienda.addDipendente();
        azienda.addDipendente();
        azienda.addDipendente();

        Scanner scanner = new Scanner(System.in);

        while (true){
            System.out.println("Inserisci la matricola del dipendente di cui vuoi conoscere la catena di comando: ");
            String matricola = scanner.nextLine();
            azienda.findChainOfCommand(matricola);
        }




    }
}