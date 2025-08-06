

public class AdjacencyListGraph {

    public static void main(String[] args) {
        AdjacencyListGraph g = new AdjacencyListGraph();
        g.insertVertex(1);
        g.insertVertex(2);
        g.insertVertex(3);

        // Initialize edges array for each vertex (fix for your Vertex class)
        for (int i = 0; i < vertexIndex; i++) {
            graph[i].edges = new Edges[5]; // max 5 edges per vertex
        }

        g.insertEdges(1, 2, 10);
        g.insertEdges(1, 3, 20);
        g.insertEdges(2, 3, 30);

        g.display();
    }

    static Vertex[] graph=new Vertex[100];
    static int vertexIndex=0;
    public class Vertex {
        int data;
        int edgesIndex=0;
        Edges[] edges=new Edges[edgesIndex];
        Vertex(int element){
            this.data=element;
        }
    }
    class Edges{
        Vertex src;
        Vertex dst;
        int weight;

        Edges(Vertex src,Vertex  dst, int weight){
            this.src=src;
            this.dst=dst;
            this.weight=weight;
        }

    }

    private static int getIndex(int element){
        for(int i=0; i<graph.length; i++){
            if(graph[i].data == element){
                return i;
            }
        }
        return -1;
    }
    
    void insertVertex(int element){
        //Returning the index of the vertex

        if(vertexIndex>=graph.length){
            System.out.println("Cannot add anymore vertex");
            return;
        }
        graph[vertexIndex]=new Vertex(element);
        vertexIndex++;
    }

    void insertEdges(int src, int dst , int weight){

        //Checking if the source/destination exists or not 
        if(getIndex(src)==-1 ){
            System.out.println("Source not found");
            return;
        }
        if(getIndex(dst)==-1 ){
            System.out.println("Destination not found");
            return;
        }
        
        //fetching the source/destination 
        Vertex source= graph[getIndex(src)];
        Vertex destination=graph[getIndex(dst)];

        //Checking if the edges are full or not
        if(source.edgesIndex>=source.edges.length){
            System.out.println("edges are full");
            return;
        }

        //Assigning the edge
        source.edges[source.edgesIndex]=new Edges(source,destination,weight);
        source.edgesIndex++;

    }

    void display() {
        System.out.println("Vertices and their edges:");
        for (int i = 0; i < vertexIndex; i++) {
            Vertex v = graph[i];
            System.out.print("Vertex " + v.data + " -> ");
            for (int j = 0; j < v.edgesIndex; j++) {
                Edges e = v.edges[j];
                System.out.print("[" + e.dst.data + ", w=" + e.weight + "] ");
            }
            System.out.println();
        }
    }

}
