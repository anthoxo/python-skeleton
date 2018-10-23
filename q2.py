# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

#compute all combinations for two portfolios
def question02(cashFlowIn, cashFlowOut):
  # modify and then return the variable below
  answer = 1000
  if (len(cashFlowIn) > 10 and len(cashFlowOut) > 10):
    return 0
  else:
    cashFlowIn = sorted(cashFlowIn, reverse=True)
    cashFlowOut = sorted(cashFlowOut, reverse=True)
    maxList = cashFlowIn if (len(cashFlowIn) > len(cashFlowOut)) else cashFlowOut
    minList = cashFlowIn if (maxList == cashFlowOut) else cashFlowOut
    for i in range(len(minList)):
      tmp1 = minList[i:]
      tmp2 = maxList
      j = i
      sumList1, sumList2 = [tmp1[0]], [tmp2[0]]
      tmp1 = tmp1[1:]
      tmp2 = tmp2[1:]
      t = True
      while(tmp1 != [] and tmp2 != []):
        s1,s2 = sum(sumList1), sum(sumList2)
        if (s1 > s2):
          if (s1-s2 in tmp2):
            return 0
          else:
            sumList2 += [tmp2[0]]
            answer = min(answer, abs(s1-s2-tmp2[0]))
            tmp2 = tmp2[1:]
        elif (s1 < s2):
          if (s2-s1 in tmp1):
            return 0
          else:
            sumList1 += [tmp1[0]]
            answer = min(answer, abs(s2-s1-tmp1[0]))
            tmp1 = tmp1[1:]
        else:
          return 0
  return answer
