public class AdjacencyMatrixGraph {

    public static void main(String[] args) {
        AdjacencyMatrixGraph g = new AdjacencyMatrixGraph();
        g.insertVertex(0);
        g.insertVertex(1);
        g.insertVertex(2);

        g.insertEdges(0, 1, 10);
        g.insertEdges(0, 2, 20);
        g.insertEdges(1, 2, 30);

        g.display();
    }

    int numberOfVertex=100;
    int numberOfEdges=5;
    int[][] graph = new int[numberOfVertex][numberOfEdges];
    boolean[] vertexAvailable= new boolean[numberOfVertex];

    void insertVertex(int element){
        vertexAvailable[element]=true;
    }

    void insertEdges(int src, int dst , int weight){
        if(vertexAvailable[src] == false ){
            System.out.println("Source not found");
        } 
        if(vertexAvailable[dst] == false ){
            System.out.println("Destination not found");
        }
        
        graph[src][dst]=weight;

    }

    void display() {
        System.out.println("Vertices and their edges:");
        for (int i = 0; i < numberOfVertex; i++) {
            if (vertexAvailable[i]) {
                System.out.print("Vertex " + i + " -> ");
                boolean hasEdge = false;
                for (int j = 0; j < numberOfEdges; j++) {
                    if (graph[i][j] != 0) {
                        System.out.print("[" + j + ", w=" + graph[i][j] + "] ");
                        hasEdge = true;
                    }
                }
                if (!hasEdge) {
                    System.out.print("No edges");
                }
                System.out.println();
            }
        }
    }
    
}
