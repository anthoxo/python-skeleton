# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

#compute all combinations for two portfolios
def question04(rows, numberMachines):
  result = []
  for tab in rows:
    for i in range(0, len(tab)-int(numberMachines)):
      if ('X' not in tab[i:i+int(numberMachines)]):
        result += [sum(tab[i:i+int(numberMachines)])]
  return 0 if result == [] else min(result)