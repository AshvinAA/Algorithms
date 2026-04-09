import java.io.*;
import java.util.*;

public class problemE {
    public static void main(String[] args) throws IOException {
        
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter output = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        
        String line = input.readLine();
        if (line != null && !line.trim().isEmpty()) {
            StringTokenizer st = new StringTokenizer(line);
            int N = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
            
            
            int[] nodes = new int[N];
            
            
            st = new StringTokenizer(input.readLine());
            int[] u = new int[st.countTokens()];
            for (int i = 0; i < u.length; i++) {
                u[i] = Integer.parseInt(st.nextToken());
            }
            
            st = new StringTokenizer(input.readLine());
            int[] v = new int[st.countTokens()];
            for (int i = 0; i < v.length; i++) {
                v[i] = Integer.parseInt(st.nextToken());
            }
            
            
            for (int i = 0; i < E; i++) {
                nodes[u[i] - 1] -= 1;
                nodes[v[i] - 1] += 1;
            }
            
            
            for (int i = 0; i < N; i++) {
                output.print(nodes[i]);
                if (i < N - 1) {
                    output.print(" ");
                }
            }
            output.print("\n");
        }
        
     
        output.flush();
    }
}