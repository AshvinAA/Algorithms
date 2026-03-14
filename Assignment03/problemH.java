
import java.io.*;
import java.util.*;

public class problemH {

    public static List<Integer> get_PreOrder(List<Integer> postOrder, List<Integer> inOrder) {
        if (postOrder == null || postOrder.isEmpty() || inOrder == null || inOrder.isEmpty()) {
            return new ArrayList<>();
        }
        
        int root_val = postOrder.get(postOrder.size() - 1);
        
        int root_idx = inOrder.indexOf(root_val);
        
        // splitting InOrder array
        List<Integer> left_inOrder = inOrder.subList(0, root_idx);
        List<Integer> right_inOrder = inOrder.subList(root_idx + 1, inOrder.size());
        
        // splitting postOrder array
        int right_len = right_inOrder.size();
        int left_len = left_inOrder.size();
        
        List<Integer> left_postOrder = postOrder.subList(postOrder.size() - 1 - right_len - left_len, postOrder.size() - 1 - right_len);
        List<Integer> right_postOrder = postOrder.subList(postOrder.size() - 1 - right_len, postOrder.size() - 1);
        
        // getting right/left preOrder array
        List<Integer> left_post = get_PreOrder(left_postOrder, left_inOrder);
        List<Integer> right_post = get_PreOrder(right_postOrder, right_inOrder);
        
        // returning post order = root L R
        List<Integer> result = new ArrayList<>();
        result.add(root_val);
        result.addAll(left_post);
        result.addAll(right_post);
        
        return result;
    }

    public static void main(String[] args) throws IOException {
        // Fast I/O setup
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter output = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        
        String nStr = input.readLine();
        if (nStr != null && !nStr.trim().isEmpty()) {
            int n = Integer.parseInt(nStr.trim());
            
            List<Integer> inOrderTree = new ArrayList<>();
            StringTokenizer st = new StringTokenizer(input.readLine());
            while (st.hasMoreTokens()) {
                inOrderTree.add(Integer.parseInt(st.nextToken()));
            }
            
            List<Integer> postOrderTree = new ArrayList<>();
            st = new StringTokenizer(input.readLine());
            while (st.hasMoreTokens()) {
                postOrderTree.add(Integer.parseInt(st.nextToken()));
            }
            
            List<Integer> preOrderTree = get_PreOrder(postOrderTree, inOrderTree);
            
            // Output formatting to mimic " ".join(map(str, preOrderTree)) + "\n"
            for (int i = 0; i < preOrderTree.size(); i++) {
                output.print(preOrderTree.get(i));
                if (i < preOrderTree.size() - 1) {
                    output.print(" ");
                }
            }
            output.print("\n");
        }
        
        // Ensure all output is written
        output.flush();
    }
}