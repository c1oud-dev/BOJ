import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            String[] member = sc.nextLine().split(" "); //회원 정보 입력 받고 공백 기준으로 분리
            //마지막 줄 처리
            if (member[0].equals("#")) {
                break;
            }
            int age = Integer.parseInt(member[1]);
            int weight = Integer.parseInt(member[2]);
            if (age > 17 || weight >= 80) { //17세 이상이거나 80kg 이상
                System.out.println(member[0] + " Senior");
            } else { //17세 미만, 80kg 이하
                System.out.println(member[0] + " Junior");
            }
        }
        sc.close();
    }
}
/**
 * 나이가 18세 이상이거나, 몸무게가 80kg 이상이면 성인부. 그 외에는 청소년부
 * 입력받은 대로 바로 결과 출력
 * 1. 입력은 String으로 받되, 공백 기준으로 분리해서 배열에 저장
 * 2. 나이와 몸무게는 int형으로 변환 필요
 * - java.lang.Integer 클래스의 parseInt()와 valueOf() 메소드를 사용
 * 주의할 점 : 동일한 걸 찾으려고 할 때 == 말고 무조건 eqauls
 */