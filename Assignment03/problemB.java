import java.io.*;
import java.util.*;

public class problemB {
    static class FenwickTree {
        private int[] tree;
        private int n;
        
        public FenwickTree(int size) {
            n = size;
            tree = new int[n + 1];
        }
        
        public void update(int i, int delta) {
            for (++i; i <= n; i += i & -i) {
                tree[i] += delta;
            }
        }
        
        public int query(int i) {
            int sum = 0;
            for (++i; i > 0; i -= i & -i) {
                sum += tree[i];
            }
            return sum;
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(input[i]);
        }
        
        // Collect all unique squares and sort them
        long[] squares = new long[n];
        for (int i = 0; i < n; i++) {
            squares[i] = (long) a[i] * a[i];
        }
        
        Arrays.sort(squares);
        
        // Remove duplicates
        int uniqueCount = 1;
        for (int i = 1; i < n; i++) {
            if (squares[i] != squares[i-1]) {
                squares[uniqueCount++] = squares[i];
            }
        }
        
        FenwickTree ft = new FenwickTree(uniqueCount);
        long count = 0;
        
        // Process from right to left
        for (int i = n - 1; i >= 0; i--) {
            long currentSquare = (long) a[i] * a[i];
            
            // Binary search to find compressed index of current square
            int compressedIndex = Arrays.binarySearch(squares, 0, uniqueCount, currentSquare);
            
            // Binary search to find how many squares are less than a[i]
            int left = 0, right = uniqueCount - 1;
            int pos = -1;
            
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (squares[mid] < a[i]) {
                    pos = mid;
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
            
            // Count elements to the right with square < a[i]
            if (pos >= 0) {
                count += ft.query(pos);
            }
            
            // Add current element's square to the Fenwick tree
            ft.update(compressedIndex, 1);
        }
        
        System.out.println(count);
        br.close();
    }
}