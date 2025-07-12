import java.util.Arrays;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class problemC {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        
        String[] str1 = br.readLine().split(" ");

        
        String[] str2 = br.readLine().split(" ");

        

        int numbers=Integer.parseInt(str1[0]);
        int target=Integer.parseInt(str1[1]);
        Integer[] arr =new Integer[numbers];
        Integer[] clonedArray= new Integer[numbers];

        for(int i=0 ; i< numbers ;i++ ){
            arr[i]=Integer.parseInt( str2[i] );
            clonedArray[i]=arr[i];
        }

       
        Arrays.sort(clonedArray);

        boolean found=false;
        Integer a=0,b=0,c=0;

        for(int i=0; i<numbers-1 && !found ;i++){
            int num= arr[i];
            int l=i+1;
            int r=clonedArray.length-1;
            while (l<r) {
                int sum=num+ clonedArray[l] + clonedArray[r];

                if((sum) == target){
                    found=true;
                    a=num; b=clonedArray[l] ; c=clonedArray[r];
                    break; 
                }
                if(sum< target){
                    l++;
                }
                else{
                    r--;
                }
            }
        }

        if(found){
            for(int i=0;i<numbers;i++){
                if(arr[i].equals(a)){
                    System.out.print(i+1+" ");
                    a=null;
                }
                else if(arr[i].equals(b)){
                    System.out.print(i+1+" ");
                    b=null;
                }
                else if(arr[i].equals(c)){
                    System.out.print(i+1+" ");
                    c=null;
                }
            }
        }
        else{
            System.out.println(-1);
        }
    }
}
