
public class DiscountCalculator {
    public static double finalPrice(double price, double discountPercent) {
        if (price < 0 || discountPercent < 0 || discountPercent > 100) {
            throw new IllegalArgumentException("Invalid input");
        }

        double discount = discountPercent / 100;
        return price - discount;
    }

    public static void main(String[] args) {
        System.out.println(finalPrice(100.0, 20.0));
        System.out.println(finalPrice(50.0, 10.0));
    }
}
