package Lezione_9_ott;
interface Bicycle {

	// solo metodi, senza variabili/attributi/stati
	
    void changeCadence(int newValue);

    void changeGear(int newValue);

    void speedUp(int increment);

    void applyBrakes(int decrement);
    
    void printStates();
}
