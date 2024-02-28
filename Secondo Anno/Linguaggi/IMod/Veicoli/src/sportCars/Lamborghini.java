package sportCars;

public class Lamborghini extends SportCar{
	public int nrGears;
	
	public Lamborghini(float motorizzazione, String carburante, int nrGears) {
		// super() se SportCar ha un costruttore diverso da quello default
		this.motorizzazione = motorizzazione;
		this.fuel = carburante;
		this.nrGears = nrGears;
	}
}
