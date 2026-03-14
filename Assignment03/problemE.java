import java.io.*;
import java.util.*;

public class problemE {

    public static long[] mod_pow_sum(long a, long n, long m) {
        if (n == 0) {
            return new long[]{1, 0};
        }
        if (n == 1) {
            return new long[]{a % m, a % m};
        }
        
        long power = 1, summation = 0;
        long res_pow = 1, res_sum = 0;
        long base_pow = a % m, base_sum = a % m;
        
        while (n > 0) {
            if ((n & 1) == 1) {
                res_sum = (res_sum * base_pow + base_sum) % m;
                res_pow = (res_pow * base_pow) % m;
            }
            base_sum = (base_sum * (1 + base_pow)) % m;
            base_pow = (base_pow * base_pow) % m;
            n >>= 1;
        }
        return new long[]{res_pow, res_sum};
    }

    public static void main(String[] args) throws IOException {
        // Fast I/O setup
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter output = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        StringTokenizer st;

        String line = input.readLine();
        if (line != null && !line.trim().isEmpty()) {
            int T = Integer.parseInt(line.trim());
            
            for (int i = 0; i < T; i++) {
                st = new StringTokenizer(input.readLine());
                long a = Long.parseLong(st.nextToken());
                long n = Long.parseLong(st.nextToken());
                long m = Long.parseLong(st.nextToken());
                
                if (a == 1) {
                    output.print((n % m) + "\n");
                } else {
                    long[] result = mod_pow_sum(a, n, m);
                    // result[0] acts as the ignored '_' variable
                    long total = result[1]; 
                    output.print((total % m) + "\n");
                }
            }
        }
        
        // Ensure all output is written
        output.flush(); 
    }
}