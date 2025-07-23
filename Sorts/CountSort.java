import java.util.Arrays;

public class CountSort{
    public static void main(String[] args){
        int[] arr={5,4,2,1,2};
        System.out.println(Arrays.toString(CountSort(arr)));



    }
    static int[] CountSort(int[] arr){
        int min=findMin(arr);
        int length= findMax(arr) - findMin(arr) +1;
        int[] frequencyCount= new int[length];

        for(int i=0; i<arr.length ;i++){
            int value= arr[i];

            frequencyCount[value-min]++;
        }

        int[] outputArray = new int[arr.length];

        int i = 0;
        int j = 0;

        while(i<length){
            if(frequencyCount[i]!=0){
                outputArray[j]=i+min;
                frequencyCount[i]--;
                j++;
            }
            else{
                i++;
            }
        }

        return outputArray;


    }

    static int findMin(int[] arr){
        int min=arr[0];

        for(int i=0 ;i<arr.length;i++){
            if(arr[i]<min){
                min=arr[i];
            }
        }
        return min;
    }

    static int findMax(int[] arr){
        int max=arr[0];

        for(int i=0 ;i<arr.length;i++){
            if(arr[i]>max){
                max=arr[i];
            }
        }
        return max;
    }

}
