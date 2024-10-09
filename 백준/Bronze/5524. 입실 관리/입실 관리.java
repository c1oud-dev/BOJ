import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine()); //정수로 형변환
        String[] names = new String[n];
        for (int i = 0; i < n; i++) {
            names[i] = br.readLine().toLowerCase();
        }

        for (String name : names) {
            bw.write(name);
            bw.newLine();
        }

        br.close();
        bw.close();
    }
}