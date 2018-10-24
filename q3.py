# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

def question03(numNodes, edgeList):
  # modify and then return the variable below
  g = Graph(numNodes)
  for k in range(len(edgeList)):
    i = edgeList[k]["edgeA"] - 1
    j = edgeList[k]["edgeB"] - 1
    g.addEdge(i,j)
  
  coloration = Coloration(g)
  g1 = coloration.startColoration()

  tmp = g1.getMaxOccurColor()
  X = tmp[0]
  Y = 0
  connexe = g1.getNodeColored(tmp[1])
  for i in range(g1.getNumberNodes()):
    if (not i in connexe):
      for j in range(len(connexe)):
        if (g1.getEdge(i, connexe[j]) == 1):
          Y += 1
          break
  return X-Y

class Graph:
  nbNodes = 0
  nbColor = -1
  color = []
  edges = []

  def __init__(self, nodes):
    self.nbNodes = nodes
    self.color = [0 for _ in range(self.nbNodes)]
    self.edges = [[0 for _ in range(self.nbNodes)] for _ in range(self.nbNodes)]
  
  def getNumberNodes(self):
    return self.nbNodes
  
  def getNodes(self, i):
    return self.edges[i]
  
  def getEdge(self, i, j):
    return self.edges[i][j]
  
  def addEdge(self, i, j):
    self.edges[i][j] = 1
    self.edges[j][i] = 1
  
  def removeEdge(self, i, j):
    self.edges[i][j] = 0
    self.edges[j][i] = 0
  
  def isColored(self):
    return False if (min(self.color) == 0) else True
  
  def coloring(self, i, color):
    self.color[i] = color
  
  def getDegreeNode(self, i):
    return self.edges[i].count(1)

  def getMaxOccurColor(self):
    if (self.nbColor == - 1):
      return -1
    else:
      t = [self.color.count(1+i) for i in range(self.nbColor)]
      return [max(t), 1+t.index(max(t))]
  
  def getNodeColored(self, color):
    t = []
    for i in range(len(self.color)):
      if self.color[i] == color:
        t += [i]
    return t


class Coloration:
  graph = Graph(1)

  def __init__(self, graph):
    self.graph = graph
  
  def stepColoration(self, degreNodes, color):
    result = []
    tmpColored = []
    for i in range(len(degreNodes)):
      adjacent = False
      for j in range(len(tmpColored)):
        if self.graph.getEdge(tmpColored[j], degreNodes[i]) == 1:
          adjacent = True
      if (not adjacent):
        self.graph.coloring(degreNodes[i], color)
        tmpColored += [degreNodes[i]]
      else:
        result += [degreNodes[i]]
    return result
  
  def startColoration(self):
    tmp = sorted([[self.graph.getDegreeNode(i), i] for i in range(self.graph.getNumberNodes())], reverse=True, key=lambda l:l[0])
    degreeNodes = [tmp[i][1] for i in range(len(tmp))]
    color = 1
    while (not self.graph.isColored()):
      r = self.stepColoration(degreeNodes, color)
      degreeNodes = r
      color += 1
    self.graph.nbColor = color - 1
    return self.graph

  


