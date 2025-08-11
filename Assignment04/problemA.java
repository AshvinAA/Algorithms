import java.util.Arrays;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class problemA {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        
        String[] str=br.readLine().split(" ");
        int nodes = Integer.parseInt(str[0]);
        int n=Integer.parseInt(str[1]);

        int[][] matrix = new int[nodes][nodes];

        for(int i=0 ; i<n ;  i++){

            String[] input=br.readLine().split(" ");

            int node=Integer.parseInt(input[0]);
            int edge=Integer.parseInt(input[1]);
            int weight=Integer.parseInt(input[2]);

            matrix[node-1][edge-1]=weight;
        
        }

        display(matrix);

    }

    static void display(int[][] matrix ){
        for(int i= 0 ; i< matrix.length; i++){
            for(int j = 0 ; j< matrix.length ;j++){
                System.out.print(matrix[i][j]+" ");
            }
            System.out.println();
        }
    }
    
}