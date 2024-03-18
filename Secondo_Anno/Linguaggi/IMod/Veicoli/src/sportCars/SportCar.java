package sportCars;
import veicoli.AutomobiliImlpVeicoli;

public class SportCar extends AutomobiliImlpVeicoli{
	
	public boolean shift = false;  // false: manuale; true: automatico
	public boolean paddle = false; // false: non ha i paddle; true: hai i paddle
	public boolean clutch = false; // false; non premuta; true: premuta
	
	public static final int porte = 3;
	
	public void changeGear(int gear) {
		if(!this.shift) { // cambio manuale
			if(this.clutch)
				this.gear = gear;
			else {
				System.out.println("hrrrrrr");
			}
		}else{
			if(this.paddle) {
				System.out.println("Cambio la marcia usando i paddle");
			}
			else {
				System.out.println("Ci pensa il cambio automatico");
			}
			this.gear = gear;
		}
	}
	
	
	
}
