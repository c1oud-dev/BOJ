import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] r1 = new int[3];
        int[] r2 = new int[3];

        for (int i = 0; i < 3; i++) {
            String[] nums = br.readLine().split(" ");
            r1[i] = Integer.parseInt(nums[0]);
            r2[i] = Integer.parseInt(nums[1]);
        }
        int result1 = (r1[0] == r1[1]) ? r1[2] : (r1[0] == r1[2]) ? r1[1] : r1[0];
        int result2 = (r2[0] == r2[1]) ? r2[2] : (r2[0] == r2[2]) ? r2[1] : r2[0];

        System.out.println(result1 + " " + result2);
    }
}