public enum Costi{

    //costi di mano d'opera, gas e profitto
    MANODOPERA(3),
    GAS(2),
    PROFITTO(7);

    public double costo;

    private Costi(double costo){
        this.costo = costo;
    }
}
