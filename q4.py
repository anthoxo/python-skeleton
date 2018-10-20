# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

#compute all combinations for two portfolios
def question04(rows, numberMachines):
  answer = -1
  result = []
  for tab in rows:
    for i in range(0, len(tab)-numberMachines):
      if ('X' not in tab[i:i+numberMachines]):
        result += [sum(tab[i:i+numberMachines])]
  return 0 if result == [] else min(result)