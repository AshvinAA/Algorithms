import java.io.*;
import java.util.*;

public class problemH {

   
    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }


    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    String line = br.readLine();
                    if (line == null) return null; // End of File
                    st = new StringTokenizer(line);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        Integer nextInt() {
            String str = next();
            if (str == null) return null;
            return Integer.parseInt(str);
        }
    }

    public static void main(String[] args) throws IOException {
        FastScanner input = new FastScanner();
        PrintWriter output = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

        Integer nObj = input.nextInt();
        if (nObj == null) {
            
            return; 
        }
        
        int N = nObj;
        int Q = input.nextInt();

        
        List<Integer>[] graph = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        
        for (int i = 1; i <= N; i++) {
            for (int j = i + 1; j <= N; j++) {
                if (gcd(i, j) == 1) {
                    graph[i].add(j);
                    graph[j].add(i);
                }
            }
        }

        
        for (int i = 0; i < Q; i++) {
            int X = input.nextInt();
            int K = input.nextInt();

            if (K <= graph[X].size()) {
                
                output.print(graph[X].get(K - 1) + "\n");
            } else {
                output.print("-1\n");
            }
        }

        
        output.flush();
    }
}