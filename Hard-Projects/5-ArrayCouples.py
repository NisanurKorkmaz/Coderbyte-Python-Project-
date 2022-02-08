def ArrayCouples(arr):

  firstPair=[0,0]
  secondPair=[0,0]
  yedek=arr
  
  i=0
  while i<len(arr):
    firstPair[0]=arr[i]
    firstPair[1]=arr[i+1]
    j=i+2
    
    while j<len(arr):
      secondPair[0]=arr[j]
      secondPair[1]=arr[j+1]
      #print(firstPair, secondPair)
      if(firstPair[0]==secondPair[1] and firstPair[1]==secondPair[0]):
        yedek.remove(firstPair[0])
        yedek.remove(firstPair[1])
        yedek.remove(secondPair[0])
        yedek.remove(secondPair[1])
      j=j+2
  i=i+2

    

  if len(yedek)==0:
    return "yes"
  else :
    s=""
    for i in range (len(yedek)):
      if i!=(len(arr)-1):
        s=s+str(yedek[i])+","
      else:
        s=s+str(yedek[i])
    return s


  

# keep this function call here
print ArrayCouples(raw_input())
