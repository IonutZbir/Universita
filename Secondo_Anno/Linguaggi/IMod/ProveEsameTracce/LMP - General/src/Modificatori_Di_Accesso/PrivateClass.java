package Modificatori_Di_Accesso;

public class PrivateClass {

    private int number;

    public PrivateClass() {
        this.number = 2;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
}
