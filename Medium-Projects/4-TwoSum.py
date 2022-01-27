def TwoSum(arr):

  l=len(arr)
  first = arr[0]
  couple =[]
  flag=0

  for i in range(1,l):
    for j in range(i+1,l):
      t=arr[i]+arr[j]
      if t==first :
        flag=1
        couple.append(arr[i])
        couple.append(arr[j])

  c=""
  if flag==0:
    return -1
  else :
    k=0
    while k<(len(couple)):
      c=c+str(couple[k])+","+str(couple[k+1])+" "
      k=k+2
    return c

    


  

# keep this function call here
print TwoSum(raw_input())
