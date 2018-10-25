# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

#compute all combinations for two portfolios
def question04(rows, numberMachines):
  result = -1
  for tab in rows:
    for i in range(0, len(tab)-int(numberMachines)):
      if ('X' not in tab[i:i+int(numberMachines)]):
        t = sum(tab[i:i+int(numberMachines)])
        result = t if result == -1 else min(result, t)
  return 0 if result == -1 else result