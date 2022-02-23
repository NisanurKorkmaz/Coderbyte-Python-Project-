def FibonacciChecker(num):

  fibonacci=[0,1,1]
  flen=len(fibonacci)
  yenisayi=0

  while(num>fibonacci[flen-1]):
    yenisayi=fibonacci[flen-1]+fibonacci[flen-2]
    fibonacci.append(yenisayi)
    flen=len(fibonacci)

  if(fibonacci[flen-1]==num):
    return "yes"
  else :
    return "no"
  

# keep this function call here
print FibonacciChecker(raw_input())
