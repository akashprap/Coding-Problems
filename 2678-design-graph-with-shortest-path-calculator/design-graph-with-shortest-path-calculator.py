class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adj=defaultdict(list)
        self.n=n
        self.dist=[float("inf")]*n
        for a,b,c in edges:
            self.adj[a].append((b,c))

    def addEdge(self, edge: List[int]) -> None:
        a,b,c=edge
        self.adj[a].append((b,c))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        self.dist=[float("inf")]*self.n
        self.dist[node1]=0
        pq=deque()
        pq.append((0,node1))
        while pq:
            dis,node =pq.popleft()
            for adjnode,weight in self.adj[node]:
                newdist=dis+weight
                if newdist<self.dist[adjnode]:
                    self.dist[adjnode]=newdist
                    pq.append((newdist,adjnode))
        if self.dist[node2]==float("inf"):
            return -1
        else:
            return self.dist[node2]
                
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)