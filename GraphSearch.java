import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class GraphSearch {
    public static void main(String[] args) {
        // Test Adjacency List Graph
        AdjacencyListGraph alGraph = new AdjacencyListGraph();
        alGraph.insertVertex(1);
        alGraph.insertVertex(2);
        alGraph.insertVertex(3);

        // Initialize edges array for each vertex (max 5 edges per vertex)
        for (int i = 0; i < AdjacencyListGraph.vertexIndex; i++) {
            AdjacencyListGraph.graph[i].edges = new AdjacencyListGraph.Edges[5];
        }

        alGraph.insertEdges(1, 2, 10);
        alGraph.insertEdges(1, 3, 20);
        alGraph.insertEdges(2, 3, 30);

        // Test Adjacency Matrix Graph
        AdjacencyMatrixGraph amGraph = new AdjacencyMatrixGraph();
        amGraph.insertVertex(0);
        amGraph.insertVertex(1);
        amGraph.insertVertex(2);

        amGraph.insertEdges(0, 1, 10);
        amGraph.insertEdges(0, 2, 20);
        amGraph.insertEdges(1, 2, 30);

        // Run all algorithms
        System.out.println("BFS for Adjacency List Graph:");
        BFSforALGraph(alGraph, AdjacencyListGraph.graph[0]); // Start from vertex 1

        System.out.println("\nDFS for Adjacency List Graph:");
        DFSforALGraph(alGraph, AdjacencyListGraph.graph[0]); // Start from vertex 1

        System.out.println("\nBFS for Adjacency Matrix Graph:");
        BFSforAMGraph(amGraph, 0); // Start from vertex 0

        System.out.println("\nDFS for Adjacency Matrix Graph:");
        DFSforAMGraph(amGraph, 0); // Start from vertex 0
    }



    static void BFSforALGraph(AdjacencyListGraph Graph , AdjacencyListGraph.Vertex root){
        ArrayList visited =new ArrayList<AdjacencyListGraph.Vertex>();

        Queue <AdjacencyListGraph.Vertex> q=new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            AdjacencyListGraph.Vertex vertex=q.poll();
            if(visited.contains(vertex)){
                continue;
            }
            visited.add(vertex);
            System.out.print(vertex.data+ " -> ");

            for(int i=0 ;i< vertex.edges.length ; i++){
                if(vertex.edges[i]!=null && !visited.contains(vertex.edges[i].dst)){
                    q.add(vertex.edges[i].dst);
                }
            } 
        }    
    }

    static void BFSforAMGraph(AdjacencyMatrixGraph Graph, int start){
        int[][] arr= Graph.graph;
        boolean[] visited= new boolean[arr.length];

        Queue <Integer> q= new LinkedList<>();
        q.add(start); 

        while (!q.isEmpty()) {
            int element= q.poll();

            if(visited[element]){
                continue;
            }
            visited[element]=true;
            System.out.print(element+" -> ");

            for(int i=0 ; i<arr[0].length ; i++ ){
                if(arr[element][i]!=0 && !visited[i]){
                    q.add(i);
                }
            }

        }
    }

    //Depth First Search


    static void DFSforAMGraph(AdjacencyMatrixGraph Graph, int start){
        int[][] arr= Graph.graph;
        boolean[] visited= new boolean[arr.length];

        Stack <Integer> q= new Stack<Integer>();
        q.add(start); 

        while (!q.isEmpty()) {
            int element= q.pop();

            if(visited[element]){
                continue;
            }
            visited[element]=true;
            System.out.print(element+" -> ");

            for(int i=0 ; i<arr[0].length ; i++ ){
                if(arr[element][i]!=0 && !visited[i]){
                    q.add(i);
                }
            }

        }
    }

    static void DFSforALGraph(AdjacencyListGraph Graph , AdjacencyListGraph.Vertex root){
        ArrayList visited =new ArrayList<AdjacencyListGraph.Vertex>();

        Stack <AdjacencyListGraph.Vertex> q= new Stack<AdjacencyListGraph.Vertex>();
        q.add(root);

        while (!q.isEmpty()) {
            AdjacencyListGraph.Vertex vertex=q.pop();
            if(visited.contains(vertex)){
                continue;
            }
            visited.add(vertex);
            System.out.print(vertex.data+ " -> ");

            for(int i=0 ;i< vertex.edges.length ; i++){
                if(vertex.edges[i]!=null && !visited.contains(vertex.edges[i].dst)){
                    q.add(vertex.edges[i].dst);
                }
            } 
        }    
    }

}
