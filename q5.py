# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

def rec_foundsum(n, tab, aux):
  result = []
  if (n == 0):
    return [aux]
  for i in range(len(tab)):
    if (tab[i] <= n):
      result += rec_foundsum(n-tab[i], tab, aux + 1)
  return result
        

def question05(allowedAllocations, totalValue):
  # modify and then return the variable below
  result = rec_foundsum(totalValue, allowedAllocations, 0)
  return min(result)