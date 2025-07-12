import java.util.Arrays;

public class DivideAndConquerSorting {
    public static void main(String[] args) {
        int[] test1={5,4,3,2,1,-1,-2};

        mergeSort(test1);

        System.out.println("Merge Sorted: " + Arrays.toString(test1));
    }

    static void mergeSort(int[] arr){
        int length= arr.length;

        if(length<=1){
            return;   
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

        mergeSort(leftArray);
        mergeSort(rightArray);
        merge(leftArray, rightArray, arr);
    }

    private static void merge(int[] leftArr, int[] rightArr , int[] arr){
        int leftLength=leftArr.length;
        int rightLength=rightArr.length;

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
    }



}