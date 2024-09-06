public class Main {
    public static void main(String[] args) {

        String path = "src/card.txt";
        Object card = new Factory().readCard(path);
        System.out.println(card);




    }
}