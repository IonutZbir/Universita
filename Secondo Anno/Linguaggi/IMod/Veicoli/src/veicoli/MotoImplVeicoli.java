package veicoli;
public class MotoImplVeicoli {
	public static final int RUOTE = 2;
	public String fuel; // {"benzina", "elettrico"}
	public float motorizzazione;

	public float velocita = 0;
	public float angoloSterzo = 0;
	public int gear;
	public boolean shift = false; // false: manuale; true: automatico
	public boolean clutch = false; // false; non premuta; true: premuta
	
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
	public void changeGear(int gear) { // override
		if(!this.shift) {
			if(this.clutch)
				this.gear = gear;
			else {
				System.out.println("hrrrrrr");
			}
		}else {
			this.gear = gear;
		}
	}
	
	public String getFuel() {
		return this.fuel;
	}
	
	public float getMotorizzazione() {
		return this.motorizzazione;
	}
	
	public float getVelocita() {
		return this.velocita;
	}
	
	public int getGear() {
		return this.gear;
	}
	

}
