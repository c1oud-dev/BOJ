import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        //length() 이용
        int cnt = 0;
        for (int i = 0; i < word.length(); i++) {
            System.out.print(word.charAt(i));
            cnt += 1;
            if (cnt == 10) {
                cnt = 0;
                System.out.println();
            }
        }
    }
}