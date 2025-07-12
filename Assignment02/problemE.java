import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class problemE {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] str1= br.readLine().split(" ");
        String[] str2= br.readLine().split(" ");

        int numbers=Integer.parseInt(str1[0]);
        int target=Integer.parseInt(str1[1]);

        int[] arr= new int[numbers];

        for(int i=0; i<numbers ;i++ ){
            arr[i]=Integer.parseInt(str2[i]);
        }
        
        
        int maxCount=0;
        
        int left=0;
        
        int sum=0;

        for(int right=0; right < numbers;right++){
            
            sum+=arr[right];

            while(sum > target){
                sum-=arr[left];
                left++;
            }
                
            maxCount=Math.max(maxCount, right-left + 1);
                
        }

        System.out.println(maxCount);
        
    }
}
