import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        //0을 입력할 때까지 반복
        while (true) {
            String num = br.readLine();
            if (num.equals("0")) {
                break;
            }
            int width = 1; //첫 번째 여백 1
            //숫자 분리하기
            String[] nums = num.split("");
            for (String s : nums) { //다음 여백 포함해서 + 1씩 더하기
                int intNum = Integer.parseInt(s);
                if (intNum == 1) {
                    width += 3;
                } else if (intNum == 0) {
                    width += 5;
                } else {
                    width += 4;
                }
            }
            System.out.println(width);
        }
    }
}