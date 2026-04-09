import java.io.*;
import java.util.*;

public class problemC {
    public static void main(String[] args) throws IOException {
        // Fast I/O setup
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter output = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        
        String nStr = input.readLine();
        if (nStr != null && !nStr.trim().isEmpty()) {
            int N = Integer.parseInt(nStr.trim());
            
            
            int[][] matrix = new int[N][N]; 
            
            for (int i = 0; i < N; i++) {
                String line = input.readLine();
                if (line == null) break;
                
                
                StringTokenizer st = new StringTokenizer(line);
                int[] u = new int[st.countTokens()];
                for (int j = 0; j < u.length; j++) {
                    u[j] = Integer.parseInt(st.nextToken());
                }
                
                if (u.length > 0 && u[0] == 0) {
                    continue;
                }
                
                for (int j = 1; j < u.length; j++) {
                    matrix[i][u[j]] = 1;
                }
            }
            
            
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    output.print(matrix[i][j]);
                    if (j < N - 1) {
                        output.print(" ");
                    }
                }
                output.print("\n");
            }
        }
        
        
        output.flush();
    }
}