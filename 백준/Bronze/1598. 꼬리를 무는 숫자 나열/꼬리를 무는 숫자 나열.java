import java.io.*;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int num1 = Integer.parseInt(input[0]);
        int num2 = Integer.parseInt(input[1]);
        num1 -= 1;
        num2 -= 1;
        int result = 0;
        result += Math.abs(num1 / 4 - num2 / 4);
        result += Math.abs(num1 % 4 - num2 % 4);

        System.out.println(result);
    }
}