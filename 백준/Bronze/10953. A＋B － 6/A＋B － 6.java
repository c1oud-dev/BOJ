/*
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
A와 B는 콤마(,)로 구분되어 있다.
#20:30 - 20:51
*/

import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt(); //테스트 케이스
        for (int i = 0; i < t; i++) {
            String num = sc.next(); //nextLine -> next로 변경하니 에러 사라짐
            char a = num.charAt(0);
            char b = num.charAt(2);
            int a1 = a - '0';
            int b1 = b - '0';
            System.out.println(Character.getNumericValue(a) + Character.getNumericValue(b));
        }
    }
}