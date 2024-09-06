package Static_And_Final;

/**
 * Classe FINAL
 * Questa classe non può essere estesa da nessuna altra classe
 * Potrebbe essere utile per creare una classe che non può essere modificata da nessuno
 *
 */

public final class FinalClass {

    public String name;
    public String surname;

    public String getName() {

        return "Name: " + name + " (parent class)";
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getSurname(){
        return "Surname: " + surname + " (parent class)";
    }
    public void setSurname(String surname){
        this.surname = surname;
    }
}
