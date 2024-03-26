/*
별 찍기
#20:55 - 21:12
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int star = scanner.nextInt();

        for(int i = 0; i < star; i++) {
            for (int j = star - i; j < star; j++) {
                System.out.print(" ");
            }
            for (int k = i; k < star; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}