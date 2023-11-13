package it.uniroma2.info.lmp;

public class LMP {
	public static void main(String[] args) {
		Person p1 = new StudenteImpl("Adriano", "Porzia", "0304524");
		System.out.println(p1);
		p1.saluta();
		((StudenteImpl) p1).getMatricola();
	}
}
