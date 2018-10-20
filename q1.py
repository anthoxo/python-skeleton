# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING


def splitTab(portfolios):
  tri = sorted(portfolios, reverse = True)
  maxElt = tri[0]
  maxList = []
  minList = []
  try:
      indBitFort = bitfield(maxElt).index(1)
  # que des 0 dans bitfield(maxElt) --> que des 0 dans portfolios --> return 0
  except:
      return [],[]
  for elt in tri:
    if 1 in bitfield(elt) and bitfield(elt).index(1) == indBitFort:
      maxList.append(elt)
    else:
      minList.append(elt)
  return maxList, minList

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = -1
  if len(portfolios) < 2 or len(portfolios) > 100 or max(portfolios) >= 2**16 or min(portfolios) < 0:
    return answer
  if min(portfolios) == max(portfolios):
    return 0
  maxList, minList = splitTab(portfolios)
  if maxList == [] and minList == []:
    return 0
  
  while minList == [] and max(maxList) != 0:
    indBitFort = bitfield(maxList[0]).index(1)
    for i in range(len(portfolios)):
      if portfolios[i] in maxList:
        portfolios[i] -= 2**(16-(indBitFort+1))
    maxList, minList = splitTab(portfolios)
    if maxList == [] and minList == []:
      answer = 0
      return answer

  for n1 in maxList:
    for n2 in minList:
      X1 = bitfield(n1)
      X2 = bitfield(n2)
      C = [X1[k] ^ X2[k] for k in range(16)]
      answer = max(answer, intfield(C))
  return answer

def bitfield(n):
  X = [1 if digit=='1' else 0 for digit in bin(n)[2:]]
  Y = [0 for m in range(16-len(X))]
  return Y + X

# intfield([0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]) = 15
def intfield(L):
  counter = 0
  for l in range(16):
    counter += L[15-l] * 2**l
  return counter

print(question01([i for i in range(1,10)]))
  
  # que des 0 dans bitfield(maxElt) --> que des 0 dans portfolios --> return 0

  
          
