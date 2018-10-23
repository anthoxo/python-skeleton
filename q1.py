# # ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

# # modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = 0
  l = sorted(portfolios, reverse = True)
  if (len(l) < 2 or max(l) == 0):
    return answer

  if min(l) == max(l):
    return answer
  
  bitFort = bitPoidsFort(l)
  n = bitFort
  ind = 0
  while(bitFort != 0):
    j = swapping(ind, l[ind:], bitFort)
    if (j == -1):
      bitFort -= 1
    else:
      if (j != ind):
        tmp = l[j]
        l[j] = l[ind]
        l[ind] = tmp
      l = xoring(ind, l, bitFort)
      bitFort -= 1
      ind += 1
  return xor_result(l, n)

def swapping(indDeb, tab, bitFort):
  for i in range(indDeb, len(tab)):
    if tab[i] >= 2**bitFort:
      return i
  return -1

def xoring(ind, tab, bitFort):
  for i in range(len(tab)):
    if (i != ind):
      t1 = [int(i) for i in bin(tab[i])[2:]]
      t = [0 for i in range(16 - len(t1))] + t1
      if (t[15-bitFort] == 1):
        tab[i] = tab[i] ^ tab[ind]      
  return tab

def xor_result(tab, n):
  result = tab[0]
  for i in range(1, len(tab)):
    result = result ^ tab[i]
  return result

def bitPoidsFort(tab):
  return sum([1 for i in range(16) if max(tab) - 2**i >= 0])-1

def question01bis(portfolios):
  # modify and then return the variable below
  answer = 0
  if len(portfolios) < 2 or max(portfolios) == 0:
    return answer
  answer = max([portfolios[i] ^ portfolios[j] for i in range(len(portfolios)-1) for j in range(i+1, len(portfolios))])
  return answer

print(question01([i for i in range(1000)]))
print(question01bis([i for i in range(1000)]))