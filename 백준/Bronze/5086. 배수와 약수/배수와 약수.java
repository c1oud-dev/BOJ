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
            if (b % a == 0) { //약수
                System.out.println("factor");
            } else if (a % b == 0) { //배수
                System.out.println("multiple");
            } else { //둘 다 아니면
                System.out.println("neither");
            }
        }
    }
}