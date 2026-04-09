import java.io.*;
import java.util.*;

public class problemD {
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
                nodes[u[i] - 1] += 1;
                nodes[v[i] - 1] += 1;
            }
            
            int oddCount = 0;
            
            
            for (int edgeCount : nodes) {
                if ((edgeCount % 2) == 1) {
                    oddCount += 1;
                }
            }
            
            if (oddCount > 2) {
                output.print("NO\n");
            } else {
                output.print("YES\n");
            }
        }
        
        
        output.flush();
    }
}