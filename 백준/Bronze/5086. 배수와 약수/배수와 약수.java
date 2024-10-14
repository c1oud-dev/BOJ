import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String[] nums = br.readLine().split(" ");
            int a = Integer.parseInt(nums[0]);
            int b = Integer.parseInt(nums[1]);

            if (a == 0 && b == 0) {
                break;
            }
            int check = 0;
            for (int i = 1; i <= 10000; i++) {
                if (b % i == 0) { //약수 중에서
                    if (i == a) {
                        System.out.println("factor");
                        check = 1;
                        break;
                    }
                } else if (b * i == a) {
                    System.out.println("multiple");
                    check = 1;
                    break;
                }
            }
            if (check == 0) {
                System.out.println("neither");
            }
        }
    }
}