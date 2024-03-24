/*
자동차 10부제는 자동차 번호의 일의 자리 숫자와 날짜의 일의 자리 숫자가 일치하면
해당 자동차의 운행을 금지하는 것이다.
10부제를 위반하는 자동차의 대수를 출력하면 된다.
#19:52 - 19:58
*/

import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int digit = 0; //일의 자리 숫자
        int car = 0; //자동차 번호의 일의 자리 숫자
        int ans = 0; //위반하는 자동차의 수

        digit = sc.nextInt(); //일의 자리 숫자 입력
        for (int i = 0; i < 5; i++) { 
            car = sc.nextInt(); //자동차 번호의 일의 자리 숫자 입력
            if (car == digit) { //자동차 번호와 일의 자리 숫자가 같으면 카운트
                ans += 1;
            }
        }
        System.out.println(ans);
    }
}