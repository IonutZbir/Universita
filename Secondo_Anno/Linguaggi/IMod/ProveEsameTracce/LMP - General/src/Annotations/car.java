package Annotations;

@Author(
        author = "John Doe",
        date = "3/17/2002",
        version = "1.0"
)

public class car {

    String color = "red";
    String targa = "AA123BB";
    int speed = 100;

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getTarga() {
        return targa;
    }

    public void setTarga(String targa) {
        this.targa = targa;
    }

    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }
}
