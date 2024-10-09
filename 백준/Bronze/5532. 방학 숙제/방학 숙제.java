import java.io.*;

public class Main {
    public static void main(String[]  args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int l = Integer.parseInt(br.readLine());
        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        int c = Integer.parseInt(br.readLine());
        int d = Integer.parseInt(br.readLine());

        double max = 0;
        max = Math.max((double)a/(double)c, (double)b / (double)d);
        max = Math.ceil(max);
        l -= (int)max;
        System.out.print(l);
    }
}