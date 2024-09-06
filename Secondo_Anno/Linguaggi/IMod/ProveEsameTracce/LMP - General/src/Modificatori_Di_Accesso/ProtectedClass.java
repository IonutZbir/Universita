package Modificatori_Di_Accesso;

public class ProtectedClass {

    protected int number;

    public ProtectedClass(){

        this.number = 3;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
}
