# Network-Flow-Algorithms-Group-3

Implementation of two Network Flow Algorithms for the Graph Theory course at Institut Teknologi Sepuluh Nopember (ITS).

This project implements Dinic's Algorithm and Push-Relabel Algorithm to solve the Maximum Flow problem in a directed graph.

---

## 1. Identity

**Informatics ITS Graph Theory Class - Group 3**

| Name | Student ID |
|---|---|
| Padhang Abiyu Fikri | 5025251014 |
| Dzulfiqar Rafi'ussunnah | 5025251011 |
| Aditya Lingga Mardika | 5025251158 |
| Muhammad Faris Alfarrel | 5025251002 |

---

## 2. Short Explanation About Algorithms

This project implements two algorithms for solving the Maximum Flow problem in Network Flow: Dinic's Algorithm and Push-Relabel Algorithm.

Both algorithms aim to determine the maximum amount of flow that can be transported from a source vertex to a sink vertex without exceeding the capacity of any edge.

### 2.1 Dinic's Algorithm

Dinic's Algorithm is a Maximum Flow algorithm that uses a combination of Breadth-First Search (BFS) and Depth-First Search (DFS) to efficiently find the maximum flow in a directed graph.

The algorithm operates using the following concepts:

- **Residual Graph:** Represents the remaining capacity available on each edge, including reverse edges that allow previously assigned flow to be adjusted.
- **Level Graph:** A graph constructed using BFS that assigns levels to vertices based on their distance from the source.
- **Blocking Flow:** A flow that prevents any additional flow from being sent through the current level graph using available source-to-sink paths.

The algorithm works through the following steps:

1. Use BFS to construct a Level Graph from the source vertex.
2. Use DFS to find available paths from the source to the sink within the Level Graph.
3. Send flow through the selected paths while respecting the minimum residual capacity.
4. Update the residual capacities of forward and reverse edges.
5. Repeat the process until no more augmenting paths can be found.

The algorithm terminates when the sink is no longer reachable from the source in the residual graph.

The final result represents the maximum possible flow in the network.

**Time Complexity:** O(V²E) for general directed networks.

### 2.2 Push-Relabel Algorithm

Push-Relabel Algorithm is another approach for solving the Maximum Flow problem. Unlike path-based algorithms, it does not directly search for augmenting paths from the source to the sink.

Instead, it maintains a preflow and uses vertex heights and excess flow to determine how flow should be distributed throughout the network.

The algorithm uses the following concepts:

- **Preflow:** An initial flow condition where intermediate vertices are allowed to receive more flow than they send.
- **Excess Flow:** The difference between the total incoming flow and outgoing flow at a vertex.
- **Height Function:** Assigns a height value to each vertex to determine the direction in which flow can be pushed.
- **Push Operation:** Transfers excess flow from one vertex to an adjacent vertex when the residual capacity and height conditions are satisfied.
- **Relabel Operation:** Increases the height of a vertex when it cannot push its excess flow to any eligible neighboring vertex.

The algorithm works through the following steps:

1. Initialize the height of the source vertex and set the initial preflow by saturating its outgoing edges.
2. Calculate the excess flow for each vertex.
3. Select an active vertex that has positive excess flow.
4. Perform a Push operation if an eligible neighboring vertex is available.
5. Perform a Relabel operation if no eligible neighboring vertex exists.
6. Repeat the process until no active vertices remain.

When the algorithm terminates, the resulting flow represents the maximum flow from the source to the sink.

**Time Complexity:** O(V²E) for the generic Push-Relabel implementation.

---

## 3. Prerequisites to Run the Code

The following software and tools are required to run the implementations:

- Python 3.x
- Git (optional, for cloning the repository).

### Dependencies

The implementation uses Python built-in libraries and does not require additional external dependencies.

---

## 4. Instructions to Run the Code

### 4.1 Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Gaerowes/Network-Flow-Algorithms-Group-3.git
```

Navigate to the project directory:

```bash
cd Network-Flow-Algorithms-Group-3
```

### 4.2 Prepare the Input

Prepare the input according to the format required by each implementation.

The input represents a directed graph containing vertices, edges, capacities, a source vertex, and a sink vertex.

Example:

```text
6 8
0 1 5
0 2 2
1 2 2
1 3 2
2 4 4
4 3 1
3 5 3
4 5 5
0 5
```

Input format:

- The first line contains the number of vertices (V) and edges (E).
- The following E lines contain the source vertex, destination vertex, and edge capacity.
- The last line contains the source vertex and sink vertex.

In this example:
- Vertex 0 represents the source.
- Vertex 5 represents the sink.
- The remaining vertices represent intermediate nodes.

### 4.3 Run the Dinic's Algorithm

Run the Dinic's Algorithm implementation:

```bash
python dinic.py
```

### 4.4 Run the Push-Relabel Algorithm

Run the Push-Relabel Algorithm implementation:

```bash
python push_relabel.py
```

Both implementations use the same network structure to calculate and demonstrate the Maximum Flow.

---

## 5. Input for Sample Run

This section provides sample inputs used to demonstrate the execution of both algorithms.

### 5.1 Dinic's Algorithm

**Sample Input:**

```text
6 8
0 1 5
0 2 2
1 2 2
1 3 2
2 4 4
4 3 1
3 5 3
4 5 5
0 5
```

**Expected Result:**

```text
Maximum Flow: 6
```

### 5.2 Push-Relabel Algorithm

**Sample Input:**

```text
6 8
0 1 5
0 2 2
1 2 2
1 3 2
2 4 4
4 3 1
3 5 3
4 5 5
0 5
```

**Expected Result:**

```text
Maximum Flow: 6
```

Both algorithms should produce the same maximum flow value because they solve the same network flow problem.

---

## 6. Result of Sample Run

This section presents the execution results of the implemented algorithms.

### 6.1 Dinic's Algorithm

**Sample Output:**

```text
=============================================
             DINIC'S ALGORITHM
=============================================

Number of Vertices: 6
Number of Edges: 8
Source: 0
Sink: 5

Calculating Maximum Flow...

Maximum Flow: 6

=============================================
```

**Execution Screenshot:**

Insert your Dinic's Algorithm execution screenshot here.

### 6.2 Push-Relabel Algorithm

**Sample Output:**

```text
=============================================
            PUSH-RELABEL ALGORITHM
=============================================

Number of Vertices: 6
Number of Edges: 8
Source: 0
Sink: 5

Calculating Maximum Flow...

Maximum Flow: 6

=============================================
```

**Execution Screenshot:**

Insert your Push-Relabel Algorithm execution screenshot here.

---

## 7. AI Tools Usage Disclosure

AI tools were used as an assistance tool during the development and documentation process.

The use of AI included:

- Assisting with the understanding of Network Flow concepts.
- Supporting the understanding of Dinic's Algorithm and Push-Relabel Algorithm.
- Assisting with the preparation and improvement of algorithm documentation.
- Supporting the development and testing of sample cases.

All implementations, algorithm explanations, and execution results were reviewed and verified by the group members.

---

## 8. Conclusion

This project demonstrates the implementation of two different algorithms for solving the Maximum Flow problem in Network Flow.

Dinic's Algorithm uses BFS to construct a Level Graph and DFS to find Blocking Flow, allowing the algorithm to efficiently send flow through available paths in the network.

Meanwhile, Push-Relabel Algorithm uses the concepts of preflow, excess flow, vertex heights, Push operations, and Relabel operations to distribute flow throughout the network without directly searching for augmenting paths.

Both algorithms provide different approaches to solving the Maximum Flow problem while producing the same optimal result for a given network.

Through these implementations, the project provides an opportunity to understand Network Flow concepts and explore different algorithmic approaches to graph optimization.
