package veicoli;
public interface Veicoli {
	// interfaccia veicoli
	// solo la dichiarazione dei metodi
	public void accelera(float valore);
	public void decelera(float valore);
	public void sterzaDx(float gradi);
	public void sterzaSx(float gradi);
	public void changeGear(int gear);
}
