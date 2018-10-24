# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

def question06(numServers, targetServer, times):
  # modify and then return the variable below
  g = Graph(numServers, times)
  dijkstra = Dijkstra(g, 0, targetServer)
  return dijkstra.startDijkstra()

class Graph:
  nbNodes = 0
  edges = []

  def __init__(self, nodes, edges):
    self.nbNodes = nodes
    self.edges = edges
  
  def getNumberNodes(self):
    return self.nbNodes
  
  def getNodes(self, i):
    return self.edges[i]
  
  def getEdge(self, i, j):
    return self.edges[i][j]

class Dijkstra:
  graph = Graph(1, [[]])
  alreadySeen = []
  distance = []
  startNode = 0
  finalNode = 0
  
  def __init__(self, graph, startNode, finalNode):
    self.graph = graph
    self.alreadySeen = [False for _ in range(graph.getNumberNodes())]
    self.distance = [-1 for i in range(graph.getNumberNodes())]
    self.startNode = startNode
    self.finalNode = finalNode
    self.distance[self.startNode] = 0

  def findIndexMin(self):
    r, m = -1,-1
    for i in range(len(self.distance)):
      if (self.distance[i] != -1 and (not self.alreadySeen[i])):
        if (m == -1):
          r, m = i, self.distance[i]
        elif (self.distance[i] < m):
          r, m = i, min(self.distance[i], m)
    return r
    
  def stepDijkstra(self):
    ind = self.findIndexMin()
    self.alreadySeen[ind] = True
    if (ind == self.finalNode):
      return self
    else:
      for i in range(self.graph.getNumberNodes()):
        edge = self.graph.getEdge(ind, i)
        if (not self.alreadySeen[i] and edge != -1):
          tmp = self.distance[ind] + edge
          self.distance[i] = tmp if (self.distance[i] == -1) else min(self.distance[i], tmp)
      return self
  
  def startDijkstra(self):
    while (not self.alreadySeen[self.finalNode]):
      self = self.stepDijkstra()
    return self.distance[self.finalNode]