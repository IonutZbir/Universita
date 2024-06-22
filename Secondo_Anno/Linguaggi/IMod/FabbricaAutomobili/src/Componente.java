public class Componente {

    private String name;
    private String country;
    private int ordTime;
    private double cost;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public int getOrdTime() {
        return ordTime;
    }

    public void setOrdTime(int ordTime) {
        this.ordTime = ordTime;
    }

    public double getCost() {
        return cost;
    }

    public void setCost(double cost) {
        this.cost = cost;
    }

    public Componente(String name, String country, int ordTime, double cost) {
        this.name = name;
        this.country = country;
        this.ordTime = ordTime;
        this.cost = cost;
    }

}
