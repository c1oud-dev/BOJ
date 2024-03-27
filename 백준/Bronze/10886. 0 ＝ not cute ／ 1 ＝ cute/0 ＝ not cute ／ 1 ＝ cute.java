/*
다음 N개의 줄에는 각 줄마다 각 사람이 설문 조사에 어떤 의견을 표명했는지를 나타내는 정수가 주어진다.
0은 준희가 귀엽지 않다고 했다는 뜻이고, 1은 준희가 귀엽다고 했다는 뜻이다.
준희가 귀엽지 않다는 의견이 더 많을 경우 "Junhee is not cute!"를 출력하고 
귀엽다는 의견이 많을 경우 "Junhee is cute!"를 출력하라.
#21:23 - 21:24
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int one = 0, zero = 0;
        for (int i = 0; i < n; i++) {
            int survey = scanner.nextInt();
            if (survey == 1){
                one++;
            }
            else{
                zero++;
            }
        }
        if(one > zero){
            System.out.println("Junhee is cute!");
        }else {
            System.out.println("Junhee is not cute!");
        }

    }
}