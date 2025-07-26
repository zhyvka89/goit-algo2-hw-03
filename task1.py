from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        if v not in self.graph or u not in self.graph[v]:
            self.graph[v][u] = 0

    def bfs(self, source, sink, parent):
        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            u = queue.popleft()
            for v, capacity in self.graph[u].items():
                if v not in visited and capacity > 0:
                    visited.add(v)
                    parent[v] = u
                    if v == sink:
                        return True
                    queue.append(v)
        return False

    def edmonds_karp(self, source, sink):
        parent = {}
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

# Ініціалізація графа
g = Graph()

# Додати джерело та стік
g.add_edge('SOURCE', 'T1', float('inf'))
g.add_edge('SOURCE', 'T2', float('inf'))
g.add_edge('M1', 'SINK', float('inf'))
g.add_edge('M2', 'SINK', float('inf'))
g.add_edge('M3', 'SINK', float('inf'))
g.add_edge('M4', 'SINK', float('inf'))
g.add_edge('M5', 'SINK', float('inf'))
g.add_edge('M6', 'SINK', float('inf'))
g.add_edge('M7', 'SINK', float('inf'))
g.add_edge('M8', 'SINK', float('inf'))
g.add_edge('M9', 'SINK', float('inf'))
g.add_edge('M10', 'SINK', float('inf'))
g.add_edge('M11', 'SINK', float('inf'))
g.add_edge('M12', 'SINK', float('inf'))
g.add_edge('M13', 'SINK', float('inf'))
g.add_edge('M14', 'SINK', float('inf'))

# Додати ребра згідно таблиці
g.add_edge('T1', 'S1', 25)
g.add_edge('T1', 'S2', 20)
g.add_edge('T1', 'S3', 15)
g.add_edge('T2', 'S3', 15)
g.add_edge('T2', 'S4', 30)
g.add_edge('T2', 'S2', 10)

g.add_edge('S1', 'M1', 15)
g.add_edge('S1', 'M2', 10)
g.add_edge('S1', 'M3', 20)
g.add_edge('S2', 'M4', 15)
g.add_edge('S2', 'M5', 10)
g.add_edge('S2', 'M6', 25)
g.add_edge('S3', 'M7', 20)
g.add_edge('S3', 'M8', 15)
g.add_edge('S3', 'M9', 10)
g.add_edge('S4', 'M10', 20)
g.add_edge('S4', 'M11', 10)
g.add_edge('S4', 'M12', 15)
g.add_edge('S4', 'M13', 5)
g.add_edge('S4', 'M14', 10)

# Обчислити максимальний потік
max_flow = g.edmonds_karp('SOURCE', 'SINK')
print(f"Максимальний потік: {max_flow} одиниць")