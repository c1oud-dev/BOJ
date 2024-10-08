import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int sum = sc.nextInt();
        int diff = sc.nextInt();

        int mk = 0;
        while(true) {
            int afc = sum - mk;
            if (afc - mk == diff) {
                System.out.println(afc + " " + mk);
                break;
            } else {
                mk += 1;
            }

            if (mk > sum) {
                System.out.println(-1);
                break;
            }
        }
    }
}
/**
 * 반례 : 6 6 or 6 5
 */