from typing import Dict, List


class Vertex:

    def __init__(self, value) -> None:
        super().__init__()
        self.value = value


class NullVertex(Vertex):
    def __init__(self) -> None:
        super().__init__(None)


class Result:

    def __init__(self) -> None:
        super().__init__()
        self.parent: Dict[Vertex, Vertex] = {}
        self.finished: List[Vertex] = []

    def has_not_parent(self, v: Vertex):
        return self.parent.get(v, None) is None

    def set_parent_of(self, n, v):
        self.parent[n] = v

    def source(self, s):
        self.parent[s] = NullVertex()

    def finish(self, v):
        self.finished.append(v)

    def reverse_finished(self):
        return self.finished[::-1]


class Graph:

    def __init__(self, adj: Dict[Vertex, List]) -> None:
        super().__init__()
        self.adj: Dict[Vertex, List] = adj

    def vertices(self):
        return self.adj.keys()

    def neighbors(self, v: Vertex):
        return self.adj.get(v, [])

    def dfs(self, s: Vertex):
        r: Result = Result()
        r.source(s)
        self.__dfs_visit(s, r)

    def __dfs_visit(self, v: Vertex, r: Result):
        for n in self.neighbors(v):
            if r.has_not_parent(n):
                r.set_parent_of(n, v)
                self.__dfs_visit(n, r)
        r.finish(v)

    def topological_sort(self):
        pass
