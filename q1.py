# # ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

# # modify this function, and create other functions below as you wish
# def question01(portfolios):
#   # modify and then return the variable below
#   answer = 0
#   l = list(portfolios)

#   if (len(l) < 2):
#     return answer

#   if min(l) == max(l):
#     return answer

#   bitFort = sum([1 for i in range(16) if max(l) - 2**i >= 0]) - 1
#   maxList, minList = splitTab(l, bitFort)

#   while minList == [] and max(maxList) != 0:
#     newMaxList = [i - 2**bitFort for i in maxList]
#     bitFort -= 1
#     maxList, minList = splitTab(newMaxList, bitFort)
#   if maxList == [] and minList == []:
#     return answer
  
#   answer = max([n1 ^ n2 for n1 in maxList for n2 in minList])
#   return answer

# def splitTab(tab, bitFort):
#   maxList, minList = [],[]
#   tri = sorted(tab, reverse = True)
#   t = True
#   while(t):
#     if (len(tri) > 0):
#       if (tri[0] - 2**bitFort >= 0):
#         maxList += [tri[0]]
#         tri = tri[1:]
#       else:
#         t = False
#     else:
#       t = False
#   minList = tri
#   return maxList, minList

def question01(portfolios):
  # modify and then return the variable below
  answer = 0
  if len(portfolios) < 2 or max(portfolios) == 0:
    return answer
  answer = max([portfolios[i] ^ portfolios[j] for i in range(len(portfolios)-1) for j in range(i+1, len(portfolios))])
  return answer
