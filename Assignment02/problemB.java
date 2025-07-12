import java.util.Arrays;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class problemB {
    public static void main(String[] args)  throws IOException{

         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] str1 = br.readLine().split(" ");
        String[] str2 = br.readLine().split(" ");
        String[] str3 = br.readLine().split(" ");
        
        int target=Integer.parseInt(str1[2]);

        int[] arr1= Arrays.stream(str2).mapToInt(Integer::parseInt).toArray();
        int[] arr2= Arrays.stream(str3).mapToInt(Integer::parseInt).toArray();

        int i=0;
        int j=arr2.length-1;

        int diff=Math.abs(arr1[i]+arr2[j]-target);
        int lowestI=i;
        int lowestJ=j;


        while(i<arr1.length && j>=0){
            int innerDiff=Math.abs (arr1[i]+arr2[j]-target);

            if(innerDiff<diff){
                diff=innerDiff;
                lowestI=i;
                lowestJ=j;
            }

            if(diff==0){
                System.out.println((i+1)+" "+(j+1));
                return;
            }

            if((arr1[i] + arr2[j]) > target){
                j--;
            }
            else{
                i++;
            }

            
        }

        System.out.println((lowestI+1)+" "+(lowestJ+1));
    }

}
