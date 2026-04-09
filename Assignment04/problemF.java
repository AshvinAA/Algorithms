import java.io.*;
import java.util.*;

public class problemF {

    public static boolean validMove(int x, int y, int n) {
        if (x < 0 || x >= n || y < 0 || y >= n) {
            return false;
        }
        return true;
    }

    public static List<int[]> moves(int x, int y, int n) {
        List<int[]> turns = new ArrayList<>();

        if (validMove(x - 1, y - 1, n)) turns.add(new int[]{x - 1 + 1, y - 1 + 1});
        if (validMove(x - 1, y, n)) turns.add(new int[]{x - 1 + 1, y + 1});
        if (validMove(x - 1, y + 1, n)) turns.add(new int[]{x - 1 + 1, y + 1 + 1});
        if (validMove(x, y - 1, n)) turns.add(new int[]{x + 1, y - 1 + 1});
        if (validMove(x, y + 1, n)) turns.add(new int[]{x + 1, y + 1 + 1});
        if (validMove(x + 1, y - 1, n)) turns.add(new int[]{x + 1 + 1, y - 1 + 1});
        if (validMove(x + 1, y, n)) turns.add(new int[]{x + 1 + 1, y + 1});
        if (validMove(x + 1, y + 1, n)) turns.add(new int[]{x + 1 + 1, y + 1 + 1});

        return turns;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter output = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

        String line = input.readLine();
        if (line != null && !line.trim().isEmpty()) {
            int n = Integer.parseInt(line.trim());

            StringTokenizer st = new StringTokenizer(input.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            List<int[]> turns = moves(x - 1, y - 1, n);

            output.print(turns.size() + "\n");

            for (int[] row : turns) {
                
                output.print(row[0] + " " + row[1] + "\n");
            }
        }


        output.flush();
    }
}