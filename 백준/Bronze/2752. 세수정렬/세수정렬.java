/*
정수 세 개를 생각한 뒤에, 이를 오름차순으로 정렬.
#20:37 - 20:46
 */

import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] num = new int[3];
        for(int i = 0; i < 3; i++) {
            num[i] = sc.nextInt();
        }
        Arrays.sort(num);
        for(int i = 0; i < 3; i++) {
            System.out.print(num[i] + " ");
        }
    }
}