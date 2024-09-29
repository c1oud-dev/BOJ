import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] pledge = {"Never gonna give you up", "Never gonna let you down",
                "Never gonna run around and desert you", "Never gonna make you cry",
                "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "Never gonna stop"};

        int num = sc.nextInt(); //정수 n 입력 받기
        String[] s = new String[num + 1]; //검사할 공약을 담을 그릇

        //검사할 공약을 num만큼 입력 받기
        for (int i = 0; i < num + 1; i++) { //nextLine 개행 문자 때문에 +1
            s[i] = sc.nextLine();
        }

        int check = 0;
        for (int i = 1; i < s.length; i++) {
            check = 0; //초기화
            for (int j = 0; j < pledge.length; j++) {
                if (s[i].equals(pledge[j])) { //검사할 것과 공약이 같으면
                    check = 1; //1로 표시
                    break; //현재 반복문을 빠져 나오고 다음 문장 확인
                }
            }
            if (check == 0) { //check가 0이면 공약이 바뀐 것이므로 다음 문장을 볼 필요가 없다.
                break; //따라서 반복문을 중단시킴
            }
        }
        //바뀐 공약이 없므면 check가 1, 있으면 0
        if (check == 1) {
            System.out.println("No");
        } else {
            System.out.println("Yes");
        }
    }
}