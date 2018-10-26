# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

#compute all combinations for two portfolios
def question04(rows, numberMachines):
  n = int(numberMachines)
  result = -1
  for tab in rows:
    tmp = [] 
    for i in range(0, len(tab)):
      if tab[i] == "X":
        tmp = []
      else:
        tmp += [int(tab[i])]
        if (len(tmp) == n):
          t = sum(tmp)
          result = t if result == -1 else min(result, t)
          tmp = tmp[1:]
  return 0 if result == -1 else result