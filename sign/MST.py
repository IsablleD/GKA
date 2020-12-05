#!/usr/bin/python3

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]  # 5X5 empty array
                      for row in range(vertices)]

    # function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    # function to return the MST array
    def getMST(self, parent):
        g = [[0 for i in range(self.V)] for j in range(self.V)]  # 5X5 empty array

        for i in range(1, self.V):
            g[parent[i]][i] = g[i][parent[i]] = self.graph[i][parent[i]]

        return g

    def minKey(self, key, mst_set):

        # initialize minimum value for comparision (max size of int)
        mini = 9223372036854775807

        for v in range(self.V):
            if key[v] < mini and mst_set[v] == False:
                mini = key[v]
                min_index = v

        return min_index

    # function to construct and print MST for a graph
    def primMST(self):

        # key values used to pick minimum weight edge
        key = [9223372036854775807] * self.V
        parent = [None] * self.V  # Array to store constructed MST

        key[0] = 0
        mst_set = [False] * self.V

        parent[0] = -1  # First node is always the root

        for cout in range(self.V):

            u = self.minKey(key, mst_set)

            # put the minimum distance vertex in
            # the shortest path tree
            mst_set[u] = True

            for v in range(self.V):

                if (self.graph[u][v] > 0) and (mst_set[v] is False) and (key[v] > self.graph[u][v]):
                    key[v] = self.graph[u][v]
                    parent[v] = u

        # print the edges and weights
        self.printMST(parent)
        # print the MST array
        print(self.getMST(parent))

# initialize the test array (the original tree)
g = Graph(5)
g.graph = [[0, 1, 0, 1, 0],
           [1, 0, 1, 1, 1],
           [0, 1, 0, 0, 1],
           [1, 1, 0, 0, 1],
           [0, 1, 1, 1, 0]]

g.primMST()

