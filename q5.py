# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

def question05(allowedAllocations, totalValue):
  # modify and then return the variable below
  l = sorted(allowedAllocations, reverse=True)
  n = int(totalValue)
  answer = -1
  for i in range(len(l)):
    j = i
    resultTmp = [l[j]]
    while (j < len(l)) and (sum(resultTmp) < n):
      checkMod = checkModulo(n - sum(resultTmp), l)
      if (checkMod > 0):
        if (answer == -1 or answer > len(resultTmp)+(n - sum(resultTmp))//checkMod):
          answer = len(resultTmp)+(n - sum(resultTmp))//checkMod
      if sum(resultTmp) + l[j] <= n:
        resultTmp += [l[j]]
      else:
        j+=1
    if (n == sum(resultTmp) and (len(resultTmp) < answer or answer == -1)):
      answer = len(resultTmp)
  return answer

def checkModulo(n, tab):
  for i in range(len(tab)):
    if (tab[i] == 0):
      return -1
    if (n//tab[i] > 5):
      return -1
    if (n%tab[i] == 0):
      return i
  return -1
