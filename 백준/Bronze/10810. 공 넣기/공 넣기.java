import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = br.readLine().split(" ");
        int n = Integer.parseInt(nm[0]); //바구니 개수
        int m = Integer.parseInt(nm[1]); //바구니에 공을 몇 번 넣을지
        int[] bowl = new int[n]; //바구니 생성

        int[] mInt = new int[3]; //문자열을 정수형으로 변환하고 담을 그릇

        for (int i = 0; i < m; i++) {
            String[] mStr = br.readLine().split(" ");

            for (int j = 0; j < 3; j++) {
                mInt[j] = Integer.parseInt(mStr[j]);
            }
            //계산
            for (int k = mInt[0] - 1; k < mInt[1]; k++) {
                bowl[k] = mInt[2]; //바구니에 공 넣기
            }
        }
        for (int i : bowl) {
            System.out.printf("%d ", i);
        }
    }
}