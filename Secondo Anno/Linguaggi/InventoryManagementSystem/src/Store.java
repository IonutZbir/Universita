import java.util.ArrayList;
public class Store {
	private ArrayList<Product> cart;
	private ArrayList<Product> inv;
	
	public Store(Inventory inv) {
		this.cart = new ArrayList<>();
		this.inv = inv.getInventory();
	}
	
	public void addToCart(Product newProduct) {
		if(this.inv.contains(newProduct)) {
			this.cart.add(newProduct);
            if (newProduct instanceof PhysicalProduct) {            	
            	PhysicalProduct pd = (PhysicalProduct) newProduct; 
            	pd.updateStock(-1);
            }
		}
	}
	public void viewCart() {
		 for (Product product : cart) {
	            System.out.println(product.getName() + " - " + product.getPrice());
	        }
	}
	public double total() {
		double sum = 0;
		 for (Product product : cart) {
	            sum += product.getPrice();
	        }
		return sum;
	}
}
