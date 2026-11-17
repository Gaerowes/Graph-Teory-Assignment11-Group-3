from collections import deque


class Edge:
    def __init__(self, to, rev, capacity):
        self.to = to
        self.rev = rev
        self.capacity = capacity
        self.original_capacity = capacity


class Dinic:
    """Maximum Flow using BFS level graphs and DFS blocking flow."""

    def __init__(self, vertex_count):
        self.n = vertex_count
        self.graph = [[] for _ in range(vertex_count)]

    def add_edge(self, u, v, capacity):
        if capacity < 0:
            raise ValueError("Edge capacity cannot be negative.")

        forward = Edge(v, len(self.graph[v]), capacity)
        backward = Edge(u, len(self.graph[u]), 0)
        self.graph[u].append(forward)
        self.graph[v].append(backward)

    def _build_level_graph(self, source, sink):
        self.level = [-1] * self.n
        self.level[source] = 0
        queue = deque([source])

        while queue:
            u = queue.popleft()
            for edge in self.graph[u]:
                if edge.capacity > 0 and self.level[edge.to] < 0:
                    self.level[edge.to] = self.level[u] + 1
                    queue.append(edge.to)

        return self.level[sink] >= 0

    def _dfs(self, u, sink, pushed):
        if pushed == 0:
            return 0
        if u == sink:
            return pushed

        while self.ptr[u] < len(self.graph[u]):
            edge = self.graph[u][self.ptr[u]]

            if edge.capacity > 0 and self.level[edge.to] == self.level[u] + 1:
                flow = self._dfs(edge.to, sink, min(pushed, edge.capacity))

                if flow > 0:
                    edge.capacity -= flow
                    reverse = self.graph[edge.to][edge.rev]
                    reverse.capacity += flow
                    return flow

            self.ptr[u] += 1

        return 0

    def max_flow(self, source, sink):
        if source == sink:
            return 0

        total_flow = 0
        while self._build_level_graph(source, sink):
            self.ptr = [0] * self.n

            while True:
                pushed = self._dfs(source, sink, float("inf"))
                if pushed == 0:
                    break
                total_flow += pushed

        return total_flow


def read_input():
    print("Enter: number_of_vertices number_of_edges")
    n, m = map(int, input().split())

    print("Enter each edge as: from to capacity")
    edges = []
    for _ in range(m):
        u, v, capacity = map(int, input().split())
        edges.append((u, v, capacity))

    print("Enter: source sink")
    source, sink = map(int, input().split())
    return n, edges, source, sink


def main():
    print("=" * 48)
    print("             DINIC'S ALGORITHM")
    print("=" * 48)

    n, edges, source, sink = read_input()
    algorithm = Dinic(n)

    for u, v, capacity in edges:
        algorithm.add_edge(u, v, capacity)

    result = algorithm.max_flow(source, sink)
    print("\nCalculating Maximum Flow...")
    print(f"Maximum Flow: {result}")
    print("=" * 48)


if __name__ == "__main__":
    main()
