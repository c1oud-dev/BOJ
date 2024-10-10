import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            //생성자 생성
            StringTokenizer st = new StringTokenizer(br.readLine()); //매개변수로 들어온 문자열을 공백 기준으로 분리
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            System.out.println("Case " + (i + 1) + ": " + (a + b));
        }
    }
}