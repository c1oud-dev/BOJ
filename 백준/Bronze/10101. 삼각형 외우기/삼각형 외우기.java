/*
세 각의 크기가 모두 60이면, Equilateral
세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
세 각의 합이 180이 아닌 경우에는 Error
를 출력하는 프로그램을 작성하시오.
#13:02 - 13:09
 */

import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b, c;
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();

        if (a + b + c != 180) {
            System.out.println("Error");
        } else if (a != b && b != c && a != c) {
            System.out.println("Scalene");
        } else if (a != b || b != c || a != c) {
            System.out.println("Isosceles");
        }else{
            System.out.println("Equilateral");
        }

    }
}