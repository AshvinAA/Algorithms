import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class problemC {
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String str1[]= reader.readLine().split(" ");
        String str2[]= reader.readLine().split(" ");

        int elements=Integer.parseInt(str1[0]);
        int target=Integer.parseInt(str1[1]);
        int[] nums= new int[elements];
        for(int i=0;i<elements;i++){
            nums[i]=Integer.parseInt(str2[i]);
        }

        Node[] nodes= new Node[elements];

        for(int i=0; i<elements ;i++){
            nodes[i]= new Node(nums[i] , i);
        }

        Arrays.sort(nums);
        Integer a=0,b=0,c=0;

        boolean found=false;

        for(int i=0;i<elements ;i++){
            a=nums[i];

            int left=i+1;
            int right=elements-1;

            while (left<right && !found){
                int sum= nums[left] + nums[right] + a;

                if(sum==target){
                    b=nums[left];c=nums[right];
                    found=true;
                }
                if(sum<target){
                    left++;
                }else {
                    right--;
                }

            }
            if(found){
                break;
            }
        }
        if(found){
            for(int i=0;i<elements;i++){
                if(nodes[i].data.equals(a)){
                    System.out.print(nodes[i].index+1 +" ");
                    a=null;
                }
                else if(nodes[i].data.equals(b)){
                    System.out.print(nodes[i].index+1 +" ");
                    b=null;
                }
                else if(nodes[i].data.equals(c)){
                    System.out.print(nodes[i].index+1 +" ");
                    c=null;
                }
            }
        }
        else {
            System.out.println(-1);
        }


    }

    private static class Node{
        Integer data;
        Integer index;

        Node(Integer data, Integer index){
            this.data=data;
            this.index=index;
        }
    }
}
