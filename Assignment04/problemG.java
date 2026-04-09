import java.io.*;
import java.util.*;

public class problemG {

    static class Pair {
        int x, y;

        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Pair pair = (Pair) o;
            return x == pair.x && y == pair.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

    public static boolean validMove(int x, int y, int r, int c) {
        if (x < 0 || x >= r || y < 0 || y >= c) {
            return false;
        }
        return true;
    }

    public static boolean conflict(Set<Pair> positions, int r, int c) {
        for (Pair p : positions) {
            int x = p.x;
            int y = p.y;
            
            Pair[] available_moves = new Pair[] {
                new Pair(x - 2, y + 1),
                new Pair(x - 1, y + 2),
                new Pair(x + 2, y + 1),
                new Pair(x + 1, y + 2),
                new Pair(x - 2, y - 1),
                new Pair(x - 1, y - 2),
                new Pair(x + 1, y - 2),
                new Pair(x + 2, y - 1)
            };
            
            for (Pair move : available_moves) {
                if (validMove(x, y, r, c)) {
                    if (positions.contains(move)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
  
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter output = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

        String line = input.readLine();
        if (line != null && !line.trim().isEmpty()) {
            StringTokenizer st = new StringTokenizer(line);
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int numKnights = Integer.parseInt(st.nextToken());

            Set<Pair> positions = new HashSet<>();

            for (int i = 0; i < numKnights; i++) {
                st = new StringTokenizer(input.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                positions.add(new Pair(x, y));
            }

            if (conflict(positions, r, c) == true) {
                output.print("YES\n");
            } else {
                output.print("NO\n");
            }
        }

        output.flush();
    }
}