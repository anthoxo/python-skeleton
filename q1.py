# # ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

class BinaryTree:
  left = None
  right = None

  def __init__(self):
    _ = 0
    
  def addNode(self, number):
    if (len(number) != 0):
      if (number[0] == 0):
        if (self.left == None):
          self.left = BinaryTree()
        self.left = self.left.addNode(number[1:])
      else:
        if (self.right == None):
          self.right = BinaryTree()
        self.right = self.right.addNode(number[1:])
    return self
  
  def isInTree(self, number):
    if (len(number) == 0):
      return True
    else:
      if (number[0] == 0):
        if (self.left == None):
          return False
        else:
          return self.left.isInTree(number[1:])
      else:
        if (self.right == None):
          return False
        else:
          return self.right.isInTree(number[1:])

  def maxXor(self, number):
    if (len(number) == 0):
      return []
    else:
      if (number[0] == 0):
        if (self.right != None):
          return [1] + self.right.maxXor(number[1:])
        elif (self.left != None):
          return [0] + self.left.maxXor(number[1:])
        else:
          return []
      else:
        if (self.left != None):
          return [1] + self.left.maxXor(number[1:])
        elif (self.right != None):
          return [0] + self.right.maxXor(number[1:])
        else:
          return []
  
class Number:
  n = 0
  b = []

  def __init__(self, n):
    if(isinstance(n, int)):
      self.n = n
      self.setBinary(n)
    elif (isinstance(n, list)):
      self.b = n
      self.setNumber(n)
  
  def getNumber(self):
    return self.n
  def getBinary(self):
    return self.b
  
  def setNumber(self, b):
    r = 0
    for i in range(16):
      r += b[i] * 2**(15-i)
    self.n = r
  
  def setBinary(self, n):
    tmp = bin(n)[2:]
    self.b = [0 for _ in range(16-len(tmp))] + [int(tmp[i]) for i in range(len(tmp))]

# # modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = 0
  tree = BinaryTree()
  tabIter = [Number(int(portfolios[i])) for i in range(len(portfolios))]

  for i in range(len(tabIter)):
    tmp = tabIter[i]
    tree.addNode(tmp.getBinary())

  for i in range(len(tabIter)):
    tmp = tabIter[i]
    t = Number(tree.maxXor(tmp.getBinary()))
    if (answer < t.getNumber()):
      answer = t.getNumber()
  return answer