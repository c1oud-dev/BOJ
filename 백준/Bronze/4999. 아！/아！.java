/*
재환이는 집에서 자신이 얼마나 길게 "aah"를 낼 수 있는지 알아냈고,
자기가 소리낼 수 있는 길이의 "aah"를 요구하는 의사를 방문하려고 한다.
입력은 두 줄로 이루어져 있다.
첫째 줄은 재환이가 가장 길게 낼 수 있는 "aaah"이다.
둘째 줄은 의사가 듣기를 원하는 "aah"이다.
두 문자열은 모두 a와 h로만 이루어져 있다. 항상 h는 마지막에 하나만 주어진다.
재환이가 그 병원에 가야하면 "go"를, 아니면 "no"를 출력한다.
#22:20 - 20:23
 */

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String jae = sc.next();
        String doctor = sc.next();

        if(jae.length() >= doctor.length()){
            System.out.println("go");
        }else {
            System.out.println("no");
        }
    }
}