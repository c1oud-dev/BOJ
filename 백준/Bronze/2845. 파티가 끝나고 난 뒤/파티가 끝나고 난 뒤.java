import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //사람 수와 넓이 입력받기
        int people = sc.nextInt();
        int width = sc.nextInt();

        int totalWidth = people * width;

        int[] result = new int[5];
        //기사에 실려있는 참가자 수 입력과 동시에 연산
        for (int i = 0; i < 5; i++) {
            int participant = sc.nextInt();
            result[i] = participant - totalWidth;
        }
        for (int i : result) {
            System.out.printf("%d ", i);
        }

        sc.close();
    }
}
/**
 * 1m^2당 사람의 수와 넓이를 곱하면 넓이당 몇 명의 사람이 수용되는지 알 수 있음
 * 단순한 연산 문제이다.
 * 참가자 수를 하나씩 입력받고 바로 연산 후 결과 배열에 저장
 *
 * 자바는 연속된 정수를 한줄에 입력하고 싶을 때 스페이스만으로도 가능
 * 파이썬과는 다른 점이다.
 */