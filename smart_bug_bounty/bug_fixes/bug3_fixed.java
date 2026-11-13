
public class Bug3Fixed {
    public static double finalPrice(double price, double discountPercent) {
        if (price < 0 || discountPercent < 0 || discountPercent > 100) {
            throw new IllegalArgumentException("Invalid input");
        }

        double discount = price * discountPercent / 100;
        return price - discount;
    }

    public static void main(String[] args) {
        assert finalPrice(100.0, 20.0) == 80.0;
        assert finalPrice(50.0, 10.0) == 45.0;
        assert finalPrice(100.0, 0.0) == 100.0;
        assert finalPrice(100.0, 100.0) == 0.0;
        System.out.println("bug3_fixed.java: All 4 tests passed");
    }
}
