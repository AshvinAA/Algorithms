import java.util.Arrays;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class problemA {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] str1 = br.readLine().split(" ");
        String[] str2 = br.readLine().split(" ");

        int num = Integer.parseInt(str1[0]);
        int target = Integer.parseInt(str1[1]);

        int[] arr = Arrays.stream(str2).mapToInt(Integer::parseInt).toArray();


        for(int i=0;i<arr.length;i++){
            int y=target-arr[i];

            int result=binarySearch(arr, y, i, arr.length-1);

            if(result!=-1){
                System.out.println((i+1) +" "+(result+1));
                return;
            }
        }

        System.out.println(-1);
        
   }
    static int binarySearch (int[] arr, int target, int l , int r ){
        
        while (l<=r) {
            int m=(l+r)/2;

            if(arr[m]!=target){
                if(arr[m] > target ){
                    r=m-1;
                }
                else{
                    l=m+1;
                }
            }
            else{
                return m;
            }
        }

        return -1;
    }
    
}
