import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class problemG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] str1= br.readLine().split(" ");
        String[] str2= br.readLine().split(" ");

        int num=Integer.parseInt(str1[0]);
        int arr[]=new int[num];
        for(int i=0;i<num; i++){
            arr[i]=Integer.parseInt(str2[i]);
        }
        int loops=Integer.parseInt(str1[1]);


        for(int i=0; i <loops ;i++ ){

            String[] strings=br.readLine().split(" ");

            int start=Integer.parseInt(strings[0]);
            int end=Integer.parseInt(strings[1]);

            int left=0;
            int right=arr.length-1;

            boolean leftStopped=false;
            boolean rightStopped=false;

            
            
        }
    }

    static int lowerBound(int[] arr, int target){
        int left=0,right=arr.length-1;

        while (left<right) {
            int mid = (right-left)/2;

            if(arr[mid] <=target){
                left=mid+1;
            }
        }

        return -1;
    }

}