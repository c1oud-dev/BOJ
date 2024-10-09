import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 입력 선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)); // 출력 선언

        int n = Integer.parseInt(br.readLine()); //String으로 리턴 값이 고정되어 있으므로 형변환(예외 처리 필요)

        String[] names = new String[n];
        //입력받은대로 바로 출력? 아니면 한 번에 출력?
        for (int i = 0; i < n; i++) {
            String name = br.readLine();
            names[i] = (i + 1) + ". " + name;
        }

        for (String result : names) {
            bw.write(result); //출력
            bw.newLine(); // 줄바꿈
        }

        bw.close();
    }
}