import java.util.Arrays;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class problemA {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int length=Integer.parseInt(br.readLine().trim());
        String[] str2=br.readLine().split(" ");

        int[] nums=new int[length];

        for(int i=0; i<length;i++){
            nums[i]=Integer.parseInt(str2[i]);
        }

        long inversions=mergeSort(nums);

        StringBuilder str=new StringBuilder();

        for(int i=0 ; i<length ;i++){
            str.append(nums[i]+" ");
        }
        System.out.println(inversions);
        System.out.println(str);

    }
    static long mergeSort(int[] arr){
        int length= arr.length;

        if(length<=1){
            return 0;   
        }

        int midIndex=length/2;
        int[] leftArray=new int[midIndex];
        int[] rightArray=new int[length- midIndex]; 

        int leftIndex=0,rightIndex=0;

        for(int i=0; i<length;i++){
            if(i<midIndex){
                leftArray[leftIndex]=arr[i];
                leftIndex++;
            }
            else{
                rightArray[rightIndex]=arr[i];
                rightIndex++;
            }
        }
        long inversions=0;

        inversions+= mergeSort(leftArray);
        inversions+= mergeSort(rightArray);
        
        inversions+= merge(leftArray, rightArray, arr);

        return inversions;
    }

    private static long merge(int[] leftArr, int[] rightArr , int[] arr){
        int leftLength=leftArr.length;
        int rightLength=rightArr.length;

        int i=0,j=0,k=0;

        long inversions=0;
        while(i<leftLength && j<rightLength){
            if(leftArr[i] <= rightArr[j]){
                arr[k]=leftArr[i];
                k++;
                i++;
            }
            else{
                arr[k]=rightArr[j];
                k++;
                j++;
                inversions+=leftLength - i ;
            }
        }

        while(i<leftLength){
            arr[k]=leftArr[i];
            i++;
            k++;
        }
        while(j<rightLength){
            arr[k]=rightArr[j];
            j++;
            k++;

        }
        return inversions;
    }
}