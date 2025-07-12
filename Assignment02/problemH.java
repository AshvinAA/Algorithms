import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class problemH {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num=Integer.parseInt(br.readLine());


        for (int i = 0; i<num ;i++ ){
            String str[]=br.readLine().split(" ");
            Long k=Long.parseLong(str[0]);
            Long x=Long.parseLong(str[1]);

            Long answer= k + (k-1)/(x-1);
            System.out.println(answer);
        }
    }
}
