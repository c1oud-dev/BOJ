import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] x = new int[3];
        int[] y = new int[3];

        for (int i = 0; i < 3; i++) {
            String[] nums = br.readLine().split(" ");
            x[i] = Integer.parseInt(nums[0]);
            y[i] = Integer.parseInt(nums[1]);
        }
        int result1, result2;
        if (x[0] == x[1]) result1 = x[2];
        else if (x[0] == x[2]) result1 = x[1];
        else result1 = x[0];

        if (y[0] == y[1]) result2 = y[2];
        else if (y[0] == y[2]) result2 = y[1];
        else result2 = y[0];

        System.out.println(result1 + " " + result2);
    }
}