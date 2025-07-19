
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class problemC {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str=br.readLine().split(" ");
        

        long num=1;


        long a=Long.parseLong(str[0]);
        long b=Long.parseLong(str[1]);
        int mod=107;
        while (b>0) {
            if(b%2==1){
                num=(num * a) % mod;
            }
            a= (a*a) % mod;
            b/=2;
        }
        System.out.println(num);
    }
}

