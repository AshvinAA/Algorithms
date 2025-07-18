public class Searches {
    public static void main(String[] args) {
        int[] arr={1,2,3,4};

        System.out.println(binarySearch( arr, 1));
        System.out.println(ternarySearch(arr, 0));
    }
    static boolean binarySearch(int[] arr,int target){
        return binarySearchHelper(arr, 0 , arr.length-1, target);
    }
    static boolean binarySearchHelper(int[] arr, int l , int r , int target){
        if(l>r){
            return false;
        }
        int m= l+ (r-l)/2;
        if(arr[m]== target){
            return true;
        }
        if(target<arr[m]){
           return binarySearchHelper(arr, l, m-1, target);
        }
        else{
          return  binarySearchHelper(arr, m+1, r, target);
        }
        
    }

    static boolean ternarySearch(int[] arr , int target){
        return ternarySearchHelper(arr, 0 , arr.length-1 , target);
    } 
    static boolean ternarySearchHelper(int[] arr , int l , int r , int target ){
        int mid1=l+(r-l)/3;
        int mid2=r-(r-l)/3;

        if(l>r){
            return false;
        }
        if(target==arr[mid1] || target==arr[mid2]){
            return true;
        }
        if(target<arr[mid1]){
            return ternarySearchHelper(arr, l, mid1-1, target);
        }
        else if(target < arr[mid2] ){
            return ternarySearchHelper(arr, 1+ mid1, mid1-1, target);
        }
        else{
            return ternarySearchHelper(arr, mid2+1, r, target);
        }
    }
}
