# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

#compute all combinations for two portfolios
def question04(rows, numberMachines):
  n = int(numberMachines)
  result = -1
  for tab in rows:
    for i in range(0, len(tab)-n):
      if ('X' not in tab[i:i+n]):
        t = sum(tab[i:i+n])
        result = t if result == -1 else min(result, t)
  return 0 if result == -1 else result