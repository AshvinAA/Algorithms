import java.util.Arrays;

public class DivideAndConquerSorting {
    public static void main(String[] args) {
        int[] test1={4, 2, 4, 1, 3};

        quickSort(test1);

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

    static void quickSort(int[] arr){
        quickSortHelper(arr, 0, arr.length-1);
    }
    static void quickSortHelper(int[] arr , int low, int high){
        if(low<high){
            int pivotIndex=partition(low, high, arr);
            quickSortHelper(arr,low, pivotIndex-1);    
            quickSortHelper(arr,pivotIndex+1,high);
        }
    }

    static int partition (int low, int high, int[] arr){
        int pivot = arr[high];

        int l=low-1;
        for(int i=low ; i< high ; i++){
            if(arr[i] < pivot) {
                l++;
                if(arr[l] > arr[i]){
                    swap(arr, i, l);
                }
            }
        }

        swap(arr, l + 1, high);

        return l+1;


    }

    static void swap(int[] arr , int indexA, int indexB ){
        int temp=arr[indexA];
        arr[indexA]=arr[indexB];
        arr[indexB]=temp;
    }

}
