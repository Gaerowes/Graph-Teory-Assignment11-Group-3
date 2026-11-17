from collections import deque


class Edge:
    def __init__(self, to, rev, capacity):
        self.to = to
        self.rev = rev
        self.capacity = capacity
        self.original_capacity = capacity


class PushRelabel:
    """Maximum Flow using the Push-Relabel (preflow-push) method."""

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

    def max_flow(self, source, sink):
        if source == sink:
            return 0

        height = [0] * self.n
        excess = [0] * self.n
        current = [0] * self.n
        active = [False] * self.n
        queue = deque()

        def enqueue(v):
            if v != source and v != sink and excess[v] > 0 and not active[v]:
                active[v] = True
                queue.append(v)

        # Initialize the preflow by saturating all outgoing source edges.
        height[source] = self.n

        for edge in self.graph[source]:
            amount = edge.capacity
            if amount <= 0:
                continue

            edge.capacity -= amount
            reverse = self.graph[edge.to][edge.rev]
            reverse.capacity += amount

            excess[source] -= amount
            excess[edge.to] += amount
            enqueue(edge.to)

        # Discharge active vertices until no excess flow remains
        # at any intermediate vertex.
        while queue:
            u = queue.popleft()
            active[u] = False

            while excess[u] > 0:
                if current[u] >= len(self.graph[u]):
                    # No admissible edge: relabel to one more than
                    # the minimum height of a residual neighbor.
                    minimum_height = None
                    for edge in self.graph[u]:
                        if edge.capacity > 0:
                            candidate = height[edge.to]
                            if minimum_height is None or candidate < minimum_height:
                                minimum_height = candidate

                    if minimum_height is None:
                        # This should not occur for a valid preflow state.
                        break

                    height[u] = minimum_height + 1
                    current[u] = 0
                    continue

                edge = self.graph[u][current[u]]

                if edge.capacity > 0 and height[u] == height[edge.to] + 1:
                    # Push as much excess as possible through this edge.
                    amount = min(excess[u], edge.capacity)
                    edge.capacity -= amount
                    reverse = self.graph[edge.to][edge.rev]
                    reverse.capacity += amount

                    excess[u] -= amount
                    excess[edge.to] += amount
                    enqueue(edge.to)
                else:
                    current[u] += 1

            enqueue(u)

        return excess[sink]


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
    print("            PUSH-RELABEL ALGORITHM")
    print("=" * 48)

    n, edges, source, sink = read_input()
    algorithm = PushRelabel(n)

    for u, v, capacity in edges:
        algorithm.add_edge(u, v, capacity)

    result = algorithm.max_flow(source, sink)
    print("\nCalculating Maximum Flow...")
    print(f"Maximum Flow: {result}")
    print("=" * 48)


if __name__ == "__main__":
    main()
