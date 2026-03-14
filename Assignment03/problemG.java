import java.io.*;
import java.util.*;

public class problemG {

    public static List<Integer> get_PostOrder(List<Integer> preOrder, List<Integer> inOrder) {
        if (preOrder == null || preOrder.isEmpty() || inOrder == null || inOrder.isEmpty()) {
            return new ArrayList<>();
        }
        
        int root_val = preOrder.get(0);
        
        int root_idx = inOrder.indexOf(root_val);
        
        // splitting InOrder array
        List<Integer> left_inOrder = inOrder.subList(0, root_idx);
        List<Integer> right_inOrder = inOrder.subList(root_idx + 1, inOrder.size());
        
        // splitting PostOrder array (Note: keeping your exact comment, though this splits preOrder)
        int left_len = left_inOrder.size();
        
        List<Integer> left_preOrder = preOrder.subList(1, 1 + left_len);
        List<Integer> right_preOrder = preOrder.subList(1 + left_len, preOrder.size());
        
        // getting right/left PostOrder array
        List<Integer> left_post = get_PostOrder(left_preOrder, left_inOrder);
        List<Integer> right_post = get_PostOrder(right_preOrder, right_inOrder);
        
        // returning post order = L R root
        List<Integer> result = new ArrayList<>();
        result.addAll(left_post);
        result.addAll(right_post);
        result.add(root_val);
        
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
            
            List<Integer> preOrderTree = new ArrayList<>();
            st = new StringTokenizer(input.readLine());
            while (st.hasMoreTokens()) {
                preOrderTree.add(Integer.parseInt(st.nextToken()));
            }
            
            List<Integer> postOrderTree = get_PostOrder(preOrderTree, inOrderTree);
            
            // Output formatting to mimic " ".join(map(str, postOrderTree)) + "\n"
            for (int i = 0; i < postOrderTree.size(); i++) {
                output.print(postOrderTree.get(i));
                if (i < postOrderTree.size() - 1) {
                    output.print(" ");
                }
            }
            output.print("\n");
        }
        
        // Ensure all output is written
        output.flush();
    }
}