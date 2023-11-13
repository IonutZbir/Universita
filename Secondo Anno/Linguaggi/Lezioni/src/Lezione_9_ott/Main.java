package Lezione_9_ott;

public class Main {
	public static void main(String [] args) {
		Bicycle b1 = new BicycleImpl(); // new: memory allocation
		// b1 è una varibile di tipo Bicycle
		// l' oggetto è un qualcosa in memoria ed è assegnato ad b1
		// b1 punta all' oggetto Bicycle 
		Bicycle b2 = new BicycleImpl();
		Bicycle b3 = b1; // non una copia
		
		// 	b1.printStates();
		//	b3.applyBrakes(10);
		//	b3.printStates();
		
		b1.changeCadence(50);
		b1.speedUp(10);
		b1.changeGear(2);
		b1.printStates();
		
		b2.changeCadence(50);
		b2.speedUp(10);
		b2.changeGear(2);
		b2.changeCadence(40);
		b2.speedUp(10);
		b2.changeGear(3);
		b2.printStates();
		

		
	}
}
