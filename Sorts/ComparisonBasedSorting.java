import java.util.Arrays;

public class ComparisonBasedSorting{
    public static void main(String[] args) {
        c

        System.out.println("BubbleSorted: "+ Arrays.toString(bubbleSort(arr)));

        System.out.println("SelectionSorted: "+ Arrays.toString(selectionSort(arr)));

        System.out.println("InsertionSorted: "+ Arrays.toString(insertionSort(arr)));



    }
    //BubbleSort

    static int[] bubbleSort(int[] arr){
        int array[] =arr.clone();
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<array.length-i-1;j++){
                if(array[j] > array[j+1]){
                    swap(array, j, j+1);
                }
            }
        }

        return array;
    }

    //SelectionSort

    static int[] selectionSort(int[] arr){
        int array[] =arr.clone();
        for(int i=0;i<arr.length;i++){
            int minIndex=i;

            for(int j=i;j<array.length;j++){
                if(array[j] < array[minIndex]){
                    minIndex=j;
                }
            }
            if(i!=minIndex){
                swap(array, i, minIndex);
            }
        }

        return array;
    }

    //InsertionSort

    static int[] insertionSort(int[] arr){
        int array[] =arr.clone();
        for(int i=1;i<arr.length;i++){
            

            for(int j=i;j>0;j--){
                if(array[j-1] > array [j]){
                    swap(array, j-1, j);
                }
            }
            
        }

        return array;
    }
    

    static void swap(int[] arr , int a , int b){
        int temp= arr[a];
        arr[a]=arr[b];
        arr[b]=temp;
    }
}