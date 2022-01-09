def PrimeTime(num):
  i = 2
  j = num
  flag = 0
  
  for i in range(j):
    if i == 0 or i == 1:
      continue
    else:
      if num%i == 0:
        flag = 1

  if flag == 0:
    return "true"
  else:
    return "false"

# keep this function call here
print PrimeTime(raw_input())
