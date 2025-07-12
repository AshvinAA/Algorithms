import java.util.Arrays;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class problemD {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n1 = Integer.parseInt(br.readLine().trim());
        String[] str1 = br.readLine().split(" ");
        int[] arr1= new int[n1];

        for(int i=0;i<n1;i++){
            arr1[i]=Integer.parseInt(str1[i]);
        }

        int n2 = Integer.parseInt(br.readLine().trim());
        String[] str2 = br.readLine().split(" ");
        int[] arr2= new int[n2];

        for(int i=0;i<n2;i++){
            arr2[i]=Integer.parseInt(str2[i]);
        }
      

        int[] arr=merge(arr1, arr2);

        StringBuilder sb = new StringBuilder();

        for (int i : arr) {
            sb.append(i).append(" ");
        }

        System.out.println(sb.toString().trim());

        
    }
    static int[] merge(int[] leftArr, int[] rightArr){
        int leftLength=leftArr.length;
        int rightLength=rightArr.length;

        int[] arr=new int[leftLength+rightLength];

        int i=0,j=0,k=0;

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
        return arr;
        
    }
}
