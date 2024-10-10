import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //공백 포함하는 경우의 int형을 입력받고 싶을 때
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        //총 두 줄을 입력

        int min = 0; //민국이의 점수
        int man = 0; //만세의 점수

        while (st1.hasMoreTokens()) {
            min += Integer.parseInt(st1.nextToken());
        }

        while (st2.hasMoreTokens()) {
            man += Integer.parseInt(st2.nextToken());
        }

        System.out.println(Math.max(min, man));
    }
}