package veicoli;
public class AutomobiliImlpVeicoli implements Veicoli {
	
	public static final int RUOTE = 4;
	public String fuel; // {"benzina", "diesel", "hybrid", "elettrico"}
	public float motorizzazione;
	public boolean guida = false; // true: destra, false: sinistra
	
	public float velocita = 0;
	public float angoloSterzo = 0;
	public int gear;
	
	public void accelera(float valore) {
		this.velocita += valore;
	}
	public void decelera(float valore) {
		this.velocita -= valore;
	}
	public void sterzaDx(float gradi) {
		this.angoloSterzo -= gradi;
	}
	
	public void sterzaSx(float gradi) {
		this.angoloSterzo += gradi;
	}
	public void changeGear(int gear) {
		this.gear = gear;
	}
	
	public String getFuel() {
		return this.fuel;
	}
	
	public float getMotorizzazione() {
		return this.motorizzazione;
	}
	
	public boolean getGuida() {
		return this.guida;
	}
	
	public float getVelocita() {
		return this.velocita;
	}
	
	public float getSterzo() {
		return this.angoloSterzo;
	}
	
	public int getGear() {
		return this.gear;
	}
	
	
}
