def SwapCase(strParam):

  l=len(strParam)
  s=""

  for i in range(l):
    if strParam[i].lower()==strParam[i]:
      s=s+strParam[i].upper()
    elif strParam[i].upper()==strParam[i]:
      s=s+strParam[i].lower()
    else:
      s=s+strParam[i]


  return s

# keep this function call here
print SwapCase(raw_input())
