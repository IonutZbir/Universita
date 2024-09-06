package Lambda_Functions;

public class Person {

    public String name;
    public int age;

    public Person(){

        //sceglie un nome random dalla lista
        this.name = generateRandomName();
        this.age = generateRandomAge();
    }

    public String generateRandomName(){

        //lista di nomi possibili
        //Useremo questa lista per generare un nome random
        String[] names = {"Mario", "Luigi", "Giovanni", "Paolo", "Marco", "Giacomo"};

        //scelgo un nome random dalla lista
        int randomIndex = (int) (Math.random() * names.length);
        return names[randomIndex];
    }

    public int generateRandomAge(){

        //genero un numero random tra 0 e 100
        return (int) (Math.random() * 80);
    }
}
