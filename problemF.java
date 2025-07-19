import java.util.Arrays;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class problemF {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int length=Integer.parseInt(br.readLine().trim());
        String[] str2=br.readLine().split(" ");

        int[] nums=new int[length];

        for(int i=0; i<length;i++){
            nums[i]=Integer.parseInt(str2[i]);
        }

        middleElement(nums);

    }

    static void middleElement(int[] arr){
        if(arr.length==1){
            System.out.print(arr[0]+ " ");
            return;
        }
        if(arr.length==2){
            System.out.print(arr[0] +" "+ arr[1]+ " ");
            return;
        }

        int midElement =arr[ arr.length/2 ] ;
        int leftLength= arr.length/2 ;
        int rightLength= arr.length - leftLength -1;

        int[] leftArr = new int[leftLength];
        int[] rightArr = new int[rightLength];

        int l=0,r=0;

        for(int i=0 ; i < arr.length ;i++ ){
            if(i!=arr.length/2){

                if(i < arr.length/2){
                    leftArr[l++]=arr[i];
                }
                else{
                    rightArr[r++]=arr[i];
                }

            }
        }

        System.out.print(midElement+" ");

        middleElement(leftArr);
        middleElement(rightArr);
        
    }
    
}
