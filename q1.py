# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING
def findBit(n):
  return sum([1 for i in range(16) if n - 2**i >= 0])-1

def splitTab(portfolios, bitFort):
  tri = sorted(portfolios, reverse = True)
  t = True
  maxList, minList = [],[]
  while(t):
    if (len(tri) > 0):
      if (tri[0] - 2**bitFort >= 0):
        maxList += [tri[0]]
        tri = tri[1:]
      else:
        t = False
    else:
      t = False
  minList = tri
  return maxList, minList

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = -1
  if len(portfolios) < 2 or len(portfolios) > 100 or max(portfolios) >= 2**16 or min(portfolios) < 0:
    return answer
  if min(portfolios) == max(portfolios):
    return 0
  bitFort = findBit(max(portfolios))
  maxList, minList = splitTab(portfolios, bitFort)
  while minList == [] and max(maxList) != 0:
    newMaxList = [i - 2**bitFort for i in maxList]
    bitFort -= 1
    maxList, minList = splitTab(newMaxList, bitFort)
  if maxList == [] and minList == []:
    return 0

  for n1 in maxList:
    for n2 in minList:
      answer = max(answer, n1 ^ n2)
  return answer
  
          
