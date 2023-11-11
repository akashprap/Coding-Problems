import heapq

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adj = defaultdict(list)
        self.n = n
        for a, b, c in edges:
            self.adj[a].append((b, c))

    def addEdge(self, edge: List[int]) -> None:
        a, b, c = edge
        self.adj[a].append((b, c))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [float("inf")] * self.n
        dist[node1] = 0
        pq = [(0, node1)]
        visited = set()

        while pq:
            dis, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            for adjnode, weight in self.adj[node]:
                newdist = dis + weight
                if newdist < dist[adjnode]:
                    dist[adjnode] = newdist
                    heapq.heappush(pq, (newdist, adjnode))

        return dist[node2] if dist[node2] != float("inf") else -1
