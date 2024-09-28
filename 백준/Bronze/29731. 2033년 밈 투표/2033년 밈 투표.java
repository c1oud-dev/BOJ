import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt(); // 정수 n 입력 받아서 저장

        String[] pledge = {"Never gonna give you up", "Never gonna let you down",
                "Never gonna run around and desert you", "Never gonna make you cry",
                "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "Never gonna stop"};

        String[] translation = new String[num + 1]; //입력받은 정수만큼 배열을 생성
        for (int i = 0; i < translation.length; i++) {
            translation[i] = sc.nextLine(); //공약 입력받기
        }

        String result = "Yes";
        
        for (int i = 1; i < translation.length; i++) { //앞에 공백 때문에 i = 1 부터 시작
            result = "Yes";
            for (int j = 0; j < pledge.length; j++) {
                if(translation[i].equals(pledge[j]) == true) {
                    result = "No";
                    break;
                }
            }
            if (result.equals("Yes")) {
                break;
            }
        }
        System.out.println(result);
        sc.close();
    }
}