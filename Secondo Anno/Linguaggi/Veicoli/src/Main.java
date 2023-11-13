import sportCars.*;
public class Main {

	public static void main(String[] args) {
		Lamborghini Huracan = new Lamborghini(5.0f, "benzina", 7);
		Huracan.accelera(5);
		Huracan.accelera(5);
		Huracan.decelera(0.5f);
		Huracan.changeGear(4);
		System.out.println("La velocità è:" + Huracan.getVelocita());
		System.out.println("La marcia corrente è:" + Huracan.getGear());
	}
	
}
